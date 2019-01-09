import argparse
import os
import model_process
import data_process
import torch
from torch import nn
from torch import optim
from torch.autograd import Variable

def train(model, trainloader, validloader, epochs, criterion, optimizer, device='cpu'):
    if device == 'gpu':
        device = 'cuda'

    model.to(device)
    print_every = 40
    steps = 0

    for e in range(epochs):
        running_loss = 0
        model.train()
        for i, (inputs, labels) in enumerate(trainloader):
            steps += 1

            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()

            outputs = model.forward(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if steps % print_every == 0:
                print("Epoch: {}/{}... ".format(e + 1, epochs),
                      "Train Loss: {:.4f}".format(running_loss / print_every))
                model.eval()
                correct = 0
                total = 0
                valid_loss = 0
                with torch.no_grad():
                    for data in validloader:
                        images, labels = data
                        outputs = model(Variable(images).to(device))
                        loss = criterion(outputs, Variable(labels).to(device))
                        valid_loss += loss.item()
                        _, predicted = torch.max(outputs.data, 1)
                        total += labels.size(0)
                        correct += (predicted == Variable(labels).to(device)).sum().item()
                print("Valid Loss: {:.4f}".format(valid_loss / len(validloader)))
                print('Accuracy of the network on the valid images: %d %%' % (100 * correct / total))

                running_loss = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process train parameters')
    parser.add_argument('data_directory', metavar='d', type=str, nargs='+', help='data directory')
    parser.add_argument('--save_dir', type=str, nargs='?', help='save directory')
    parser.add_argument('--learning_rate', type=float, nargs='?', help='learning rate')
    parser.add_argument('--hidden_units', type=int, nargs='+', help='hidden units')
    parser.add_argument('--epochs', type=int, nargs='?', help='epoch numbers')
    parser.add_argument('--arch', type=str, nargs='?', help='model select')
    parser.add_argument('--gpu', action='store_true', help='use gpu')
    args = parser.parse_args()
    
    ## 数据路径
    data_directory = os.path.abspath(args.data_directory[0])
    
    ## 加载数据
    class_to_idx, dataloaders = data_process.load_data(data_directory)
    
    save_directory = "."
    if args.save_dir:
        save_directory = args.save_dir
    if not os.path.isabs(save_directory):
        save_directory = os.path.abspath(save_directory)
    if not os.path.exists(save_directory):
        raise Exception("Save directory not exist")
    ## 模型名
    model_name = 'vgg16'
    if args.arch:
        model_name = args.arch
    
    ## 创建分类器
    input_size = 25088
    output_size = 102
    hidden_layers = [4096, 1000]
    drop_p = 0.5
    if args.hidden_units:
        hidden_layers = args.hidden_units
    
    device = 'cpu'
    if args.gpu:
        device = 'gpu'
    
    epochs = 10
    if args.epochs:
        epochs = args.epochs
    
    learning_rate = 0.001
    if args.learning_rate:
        learning_rate = args.learning_rate
        
    trainloader = dataloaders[data_process.train_key]
    validloader = dataloaders[data_process.valid_key]
    
    ## 创建分类器
    classifier = model_process.create_classifier(input_size, output_size, hidden_layers, drop_p)
    
    ## 创建模型
    model = model_process.create_model(model_name, classifier)
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), lr=learning_rate)
    train(model, trainloader, validloader, epochs, criterion, optimizer, device)
    model_process.save_model(save_directory, model, model_name, input_size, output_size, hidden_layers, drop_p, class_to_idx)

    
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torch.autograd import Variable
from torchvision import datasets, transforms, models


## 创建分类器
def create_classifier(input_size, output_size, hidden_layers, drop_p):
    layers = [nn.Linear(input_size, hidden_layers[0]), nn.ReLU(), nn.Dropout(p=drop_p)]
    if len(hidden_layers) > 1:
        layer_sizes = zip(hidden_layers[:-1], hidden_layers[1:])
        for h1, h2 in layer_sizes:
            layers.append(nn.Linear(h1, h2))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(p=drop_p))
        
    layers.append(nn.Linear(hidden_layers[-1], output_size))
    layers.append(nn.LogSoftmax(dim=1))
    classifier = nn.Sequential(*layers)
    
    return classifier


## 创建模型
def create_model(model_name, classifier):
    model_list = ['vgg16', 'vgg13', 'vgg11', 'vgg19']
    if not (model_name in model_list):
        raise Exception("Don`t support this model")
    
    model = eval('models.' + model_name)(pretrained=True)
    
    for param in model.parameters():
        param.required_grad = False
    
    model.classifier = classifier
    return model

## 保存模型
def save_model(save_directory, model, model_name, input_size, output_size, hidden_layers, drop_p, class_to_idx):
    checkpoint = {'input_size': input_size,
              'output_size': output_size,
              'hidden_layers': hidden_layers,
              'dropout': drop_p,
              'class_to_idx': class_to_idx,
              'model_name': model_name,
              'state_dict': model.classifier.state_dict()}
    file_name = save_directory + '/checkpoint.pth'
    torch.save(checkpoint, 'checkpoint.pth')
    return file_name

## 加载模型
def load_model(path):
    model_info = torch.load(path)
    input_size = model_info['input_size']
    hidden_layers = model_info['hidden_layers']
    output_size = model_info['output_size']
    drop_p = model_info['dropout']
    model_name = model_info['model_name']
    classifier = create_classifier(input_size, output_size, hidden_layers, drop_p)
    classifier.load_state_dict(model_info['state_dict'])
    model = eval('models.' + model_name)(pretrained=True)
    model.classifier = classifier
    model.class_to_idx = model_info['class_to_idx']
         
    return model
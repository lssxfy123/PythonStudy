import argparse
import os
import model_process
import data_process
import torch
from torch.autograd import Variable

def predict(image_path, model, topk, device):
    np_image = data_process.process_image(image_path)
    image = torch.from_numpy(np_image)
    if device == 'gpu':
        device = 'cuda'
    image = Variable(image).to(device).unsqueeze(0).float()
    model.to(device)
    output = model(image)
    output = torch.exp(output)
    probs, classes = torch.topk(output, topk)
    probs = probs.cpu()[0].data.numpy()
    classes = classes.cpu()[0].data.numpy()
    classes = [key for key, value in model.class_to_idx.items() for i in classes if i == value]
    return probs, classes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process predict parameters')
    parser.add_argument('input', metavar='i', type=str, nargs='+', help='input name')
    parser.add_argument('checkpoint', metavar='c', type=str, nargs='+', help='model path')
    parser.add_argument('--top_k', type=int, nargs='?', help='Top k')
    parser.add_argument('--category_names', type=str, nargs='?', help='category names')
    parser.add_argument('--gpu', action='store_true', help='use gpu')
    args = parser.parse_args()
    input_image = args.input[0]
    input_image = os.path.abspath(input_image)
    if not os.path.exists(input_image):
        raise Exception('{} not exist'.format(input_image))

    checkpoint = args.checkpoint[0]
    checkpoint = os.path.abspath(checkpoint)
    if not os.path.exists(checkpoint):
        raise Exception('{} not exist'.format(checkpoint))

    top_k = 5
    if args.top_k:
        top_k = args.top_k

    device = 'cpu'
    if args.gpu:
        device = 'gpu'
    
    model = model_process.load_model(checkpoint)
    probs, classes = predict(input_image, model, top_k, device)
    if args.category_names:
        category_names = args.category_names
        if not os.path.exists(category_names):
            raise Exception('{} not exist'.format(category_names))
        cat_to_name = data_process.load_category_names(category_names)
        classes = [value for key, value in cat_to_name.items() if key in classes]
    
    print('names: ', classes)
    print('probabilities: ', probs)
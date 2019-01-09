import os
import json
import torch
from torchvision import datasets, transforms, models

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

train_key = 'train'
valid_key = 'valid'
test_key = 'test'

## 加载数据
## 返回class_to_idx, dataloaders
def load_data(data_directory):
    if not os.path.isabs(data_directory):
        data_directory = os.path.abspath(data_directory)
    if not os.path.exists(data_directory):
        raise Exception('Data directory not exist')
    train_dir = data_directory + '/' + train_key
    valid_dir = data_directory + '/' + valid_key
    test_dir = data_directory + '/' + test_key
    
    data_transforms = {train_key: transforms.Compose([transforms.RandomRotation(30),  # train_transform
                                       transforms.RandomResizedCrop(224),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
                       valid_key: transforms.Compose([transforms.Resize(256),  # validation_transform and test_transform
                                       transforms.CenterCrop(224),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])}

    image_datasets = {train_key: datasets.ImageFolder(train_dir, transform=data_transforms[train_key]),  # train_dataset
                      valid_key: datasets.ImageFolder(valid_dir, transform=data_transforms[valid_key]),  # valid_dataset
                      test_key: datasets.ImageFolder(test_dir, transform=data_transforms[valid_key])}  # test_dataset

    dataloaders = {train_key: torch.utils.data.DataLoader(image_datasets[train_key], batch_size=64, shuffle=True),
                   valid_key: torch.utils.data.DataLoader(image_datasets[valid_key], batch_size=32),
                   test_key: torch.utils.data.DataLoader(image_datasets[test_key], batch_size=32)} 
    
    return image_datasets[train_key].class_to_idx, dataloaders

def load_category_names(json_name):
    with open(json_name, 'r') as f:
        catetory_names = json.load(f)
    return catetory_names

## 预处理图片
def process_image(image):
    pil_image = Image.open(image)
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')
    width, height = pil_image.size
    if width > height:
        size = (width / height * 256,256)
    else:
        size = (256, height / width * 256)
    pil_image.thumbnail(size)
    width, height = pil_image.size
    pil_image = pil_image.crop(((width - 224) // 2, (height - 224) // 2, (width + 224) // 2, (height + 224) // 2))
    np_image = np.array(pil_image) / 255
    np_image = (np_image - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
    np_image = np_image.transpose((2, 0, 1))
    return np_image
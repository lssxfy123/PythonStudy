from keras.preprocessing import image 
from keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm
from PIL import ImageFile 
import numpy as np
import os

train_path = 'dogs-vs-cats/train1/'
test_path = 'dogs-vs-cats/test1/'
valid_path = 'dogs-vs-cats/valid1/'
if not os.path.exists(valid_path):
    os.mkdir(valid_path)
    

batch_size = 16

    
def path_to_tensor(img_path, target_size):
    # 用PIL加载RGB图像为PIL.Image.Image类型
    img = image.load_img(img_path, target_size=target_size)
    x = image.img_to_array(img)   
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths, target_size):
    list_of_tensors = [path_to_tensor(img_path, target_size) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)


def move_data(names, divide_train_path, divide_valid_path):
    os.mkdir(divide_train_path)
    os.mkdir(divide_valid_path)      
    valid_names = random.sample(names, int(len(names) * 0.2))
    train_names = [name for name in names if name not in valid_names]
    [shutil.move(train_path + name, divide_train_path + name) for name in train_names]
    [shutil.move(train_path + name, divide_valid_path + name) for name in valid_names]

    
def divide_images():
    # 训练集
    train_dog_path = train_path + 'dog/'
    train_cat_path = train_path + 'cat/'
    valid_dog_path = valid_path + 'dog/'
    valid_cat_path = valid_path + 'cat/'
    
    if not os.path.exists(train_dog_path):
        names= os.listdir(train_path)
        cat_names = [name for name in names if name.startswith('cat')]
        dog_names = [name for name in names if name.startswith('dog')]
        move_data(cat_names, train_cat_path, valid_cat_path)
        move_data(dog_names, train_dog_path, valid_dog_path)
    
    divide_test_path = test_path + 'test/'
    if not os.path.exists(divide_test_path):
        names = os.listdir(test_path)
        os.mkdir(divide_test_path)
        [shutil.move(test_path + name, divide_test_path + name) for name in names]

        
def data_generator(target_size):
    train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=30,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
    valid_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(train_path, target_size=target_size,
                                                    batch_size=batch_size, class_mode='binary')
    valid_generator = valid_datagen.flow_from_directory(valid_path, target_size=target_size,
                                                    batch_size=batch_size, class_mode='binary')
    
    return train_generator, valid_generator
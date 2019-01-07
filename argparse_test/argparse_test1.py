# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2019.1.6
# 命令行测试
import argparse
import os

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
    print(args)
    
    data_director = os.path.abspath(args.data_directory[0])
    if not os.path.exists(data_director):
        print('路径不存在')

    if args.gpu:
        print('use gpu')

    if args.hidden_units:
        hidden_layers = args.hidden_units
        layers = zip(hidden_layers[:-1], hidden_layers[1:])

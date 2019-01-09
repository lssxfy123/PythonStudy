# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2019.1.6
# 命令行测试
import argparse
import os

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

    if args.category_names:
        category_names = args.category_names
        if not os.path.exists(category_names):
            raise Exception('{} not exist'.format(category_names))
        cat_to_names = {}
    


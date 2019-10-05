#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def main():
    # 一次性读取整个文件内容
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件！')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()

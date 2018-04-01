#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 13:53
# @Author  : LiuShaoheng


def func(x):
    if x > 0:
        func(x-1)
        print(x, end=' ')


def func1(x):
    if x > 0:
        print(x, end=' ')
        func(x-1)


def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)


if __name__ == '__main__':
    func(6)
    print(' ')
    func1(6)
    print(' ')
    print(fib(6))
















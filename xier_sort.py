# !bin/even
# -*- coding:utf-8 -*-
# author:pzq
# HierSort
# version: 3.6.5
import random


def show(num_l):
    result = [num_l[0]]
    for i in range(1, len(num_l)):
        for k in range(len(result)):
            if num_l[i] <= result[k]:  # 将最小值放入
                result.insert(k, num_l[i])
                break
            if result[k - 1] < num_l[i] <= result[k]:  # 中间值放入
                result.insert(k - 1, num_l[i])
                break
            if result[len(result) - 1] < num_l[i]:  # 最大值放入
                result.append(num_l[i])
                break


if __name__ == '__main__':
    # 生成随机测试结果
    for _ in range(10):
        num_list = [random.randint(1, 99) for _ in range(6)]
        show(num_list)

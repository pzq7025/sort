import random

"""
冒泡排序
"""


def bubble_sort(data):
    length = len(data)
    for l in range(length):
        for i in range(length - l - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


if __name__ == '__main__':
    data_list = [random.randint(1, 40) for x in range(random.randint(5, 10))]
    print(data_list)
    result = bubble_sort(data_list)
    print(result)

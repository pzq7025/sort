import random

"""
快速排序
"""


def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data) // 2]
        left, right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                left.append(num)
            else:
                right.append(num)
        return quick_sort(right) + [mid] + quick_sort(left)
    else:
        return data


if __name__ == '__main__':
    data_list = [random.randint(1, 40) for x in range(random.randint(5, 10))]
    print(data_list)
    result = quick_sort(data_list)
    print(result)

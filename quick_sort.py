import random

"""
快速排序
20230519：:已修改，结合了快排的思想。
参考的讲解：https://www.bilibili.com/video/BV1at411T75o/?spm_id_from=333.337.search-card.all.click&vd_source=1f83a43974d81c3e83a94712b9af0cf5
"""


# def quick_sort(data):
# 这里存在问题
#     if len(data) >= 2:
#         mid = data[len(data) // 2]
#         left, right = [], []
#         data.remove(mid)
#         for num in data:
#             if num >= mid:
#                 left.append(num)
#             else:
#                 right.append(num)
#         return quick_sort(right) + [mid] + quick_sort(left)
#     else:
#         return data


def quick_sort(arr, left, right):
    if left < right:
        # 找到分割点
        pivot_index = partition(arr, left, right)

        # 对左右两部分分别进行快速排序
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)

    return arr


def partition(arr, left, right):
    # 选择最右边的元素作为分割点
    pivot = arr[right]
    i = left - 1

    # 将小于分割点的元素交换到左边，大于分割点的元素交换到右边
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将分割点移动到正确的位置上
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1

if __name__ == '__main__':
    data_list = [random.randint(1, 40) for x in range(random.randint(5, 10))]
    print(data_list)
    result = quick_sort(data_list)
    print(result)

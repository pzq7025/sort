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


def partition(nums, left, right):
    # 对分割的部分进行排序
    # 选取了最右边，因此小于的时候指针不动，大于的时候指针移动，如果选取最左边，后面的代码反过来。
    pivot_num = nums[right]
    i = left
    j = right
    # 没重合指针调整没结束。
    while i < j:
        if nums[i] <= pivot_num:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
    # 将选取的结果放到重合的位置。
    nums[i] = pivot_num
    # 返回重合的位置
    return i


def quick_sort(nums, left, right):
    if left < right:
        # 当分割的位置没有重叠就继续递归
        pivot = partition(nums, left, right)
        quick_sort(nums, left, pivot - 1)
        quick_sort(nums, pivot + 1, right)
    return nums

if __name__ == '__main__':
    data_list = [random.randint(1, 40) for x in range(random.randint(5, 10))]
    print(data_list)
    result = quick_sort(data_list)
    print(result)

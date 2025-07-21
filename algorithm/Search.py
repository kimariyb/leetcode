"""
常见的搜索算法：
    1. 顺序搜索
    2. 二分搜索
"""
from typing import List


def SequentialSearch(arr: List[int], target: int) -> int:
    r"""
    顺序搜索（Sequential Search）基本思想：
    从数组的第一个元素开始，依次比较每个元素与目标值是否相等，直到找到目标值或遍历完整个数组。

    Parameters
    ----------
    arr : List[int]
        待搜索的整数列表
    target : int
        目标值
    Returns
    -------
    int
        目标值在列表中的索引，如果不存在则返回 -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


def BinarySearch(arr: List[int], target: int) -> int:
    r"""
    二分搜索（Binary Search）基本思想：
    假设数组是按升序排列的，将数组中间位置的元素与目标值进行比较，
    如果相等，则返回该位置的索引；如果目标值小于中间元素，则在左侧子数组中继续查找；
    如果目标值大于中间元素，则在右侧子数组中继续查找。
    重复以上步骤，直到找到目标值或子数组为空。

    Parameters
    ----------
    arr : List[int]
        待搜索的整数列表
    target : int
        目标值
    Returns
    -------
    int
        目标值在列表中的索引，如果不存在则返回 -1
    """
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(BinarySearch(arr, 10))
    print(SequentialSearch(arr, 10))
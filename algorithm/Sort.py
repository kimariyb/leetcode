"""
常见的排序算法包括：

1. 冒泡排序：通过相邻元素比较和交换，将最大元素逐步"冒泡"到数组末尾
2. 选择排序：每次从未排序区间选择最小元素，放到已排序区间末尾
3. 插入排序：将未排序区间的元素插入到已排序区间的合适位置
4. 快速排序：选择一个基准元素，将数组分为两部分，递归排序
5. 归并排序：将数组分成两半，分别排序后合并
6. 堆排序：利用堆这种数据结构进行排序
7. 计数排序：统计每个元素出现的次数，按顺序输出  (不考虑)
8. 桶排序：将元素分到有限数量的桶中，对每个桶单独排序
9. 基数排序：按照元素的位数进行排序
"""
import heapq

from typing import List


def BubbleSort(arr: List[int]) -> List[int]:
    r"""
    冒泡排序（Bubble Sort）基本思想：
    经过多次迭代，通过相邻元素之间的比较与交换，使值较小的元素逐步从后面移到前面，值较大的元素从前面移到后面。

    Parameters
    ----------
    arr : List[int]
        待排序的整数列表

    Returns
    -------
    List[int]
        升序排序后的整数列表（原地排序，并返回同一个列表，方便链式调用）
    """
    n = len(arr)

    # 外层循环控制“冒泡”轮次，共 n-1 轮
    for i in range(n - 1):
        swapped = False  # 优化：若一轮下来没有交换，说明已经有序，可提前结束
        # 从数组中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较
        for j in range(0, n - 1 - i):
            # 相邻两个元素进行比较，如果前者大于后者，则交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换相邻元素
                swapped = True
        if not swapped:
            break  # 提前退出，优化时间复杂度
    return arr


def SelectionSort(arr: List[int]) -> List[int]:
    r"""
    选择排序（Selection Sort）基本思想：
    将数组分为两个区间：左侧为已排序区间，右侧为未排序区间。
    每趟从未排序区间中选择一个值最小的元素，放到已排序区间的末尾，从而将该元素划分到已排序区间。

    Parameters
    ----------
    arr : List[int]
        待排序的整数列表

    Returns
    -------
    List[int]
        排序后的整数列表（原地排序并返回同一列表）。
    """
    n = len(arr)
    for i in range(n - 1):
        # 记录未排序区间中最小值的位置
        min_idx = i
        # 在 [i+1, n-1] 中寻找真正的最小值索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # 找到最小值对应的索引
                min_idx = j
        # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def InsertionSort(arr: List[int]) -> List[int]:
    r"""
    插入排序（Insertion Sort）基本思想：
    将数组分为两个区间：左侧为有序区间，右侧为无序区间。
    每趟从无序区间取出一个元素，然后将其插入到有序区间的适当位置

    Parameters
    ----------
    arr : List[int]
        待排序的整数列表

    Returns
    -------
    List[int]
        排序后的整数列表（原地排序并返回同一列表）
    """
    n = len(arr)
    # 遍历无序区间，无序区间从第 2 个元素开始（索引 1）
    for i in range(1, n):
        temp = arr[i]  # 当前待插入元素
        j = i
        # 从右至左遍历有序区间
        while j > 0 and arr[j - 1] > temp:
            # 将有序区间中插入位置右侧的元素依次右移一位
            arr[j] = arr[j - 1]
            j -= 1
        # 找到插入位置
        arr[j] = temp

    return arr


def QuickSort(arr: List[int]) -> List[int]:
    r"""
    快速排序（Quick Sort）基本思想：
    采用经典的分治策略，选择数组中某个元素作为基准数，通过一趟排序将数组分为独立的两个子数组，
    一个子数组中所有元素值都比基准数小，另一个子数组中所有元素值都比基准数大。
    然后再按照同样的方式递归的对两个子数组分别进行快速排序，以达到整个数组有序。

    Parameters
    ----------
    arr : List[int]
        待排序的整数列表（原地排序）

    Returns
    -------
    List[int]
        排序后的同一列表对象，方便链式调用
    """
    def partition(nums: List[int], low: int, high: int) -> int:
        """
        以 nums[low] 为基准值，将区间 [low, high] 划分为：
            [low, p-1]  <  pivot
            [p]        == pivot
            [p+1, high] >  pivot
        返回划分后 pivot 的最终下标 p。
        """
        pivot = nums[low]
        i, j = low, high
        while i < j:
            # 从右向左找第一个 < pivot 的元素
            while i < j and nums[j] >= pivot:
                j -= 1
            # 从左向右找第一个 > pivot 的元素
            while i < j and nums[i] <= pivot:
                i += 1
            # 交换找到的两个元素
            nums[i], nums[j] = nums[j], nums[i]

        # 把基准元素放到最终位置
        nums[low], nums[i] = nums[i], nums[low]
        return i

    def quick_sort(nums: List[int], low: int, high: int) -> None:
        """在区间 [low, high] 上递归地进行快速排序（原地）。"""
        if low < high:
            p = partition(nums, low, high)
            quick_sort(nums, low, p - 1)
            quick_sort(nums, p + 1, high)

    quick_sort(arr, 0, len(arr) - 1)

    return arr


def HeapSort(arr: List[int]) -> List[int]:
    r"""
    堆排序（Heap sort）基本思想：
    借用「堆结构」所设计的排序算法。
    将数组转化为大顶堆，重复从大顶堆中取出数值最大的节点，并让剩余的堆结构继续维持大顶堆性质。

    Parameters
    ----------
    arr : List[int]
        待排序整数列表

    Returns
    -------
    List[int]
        排序后的整数列表（返回新列表，不改变原列表）
    """
    # 1. 把 arr 所有元素压入最小堆
    heapq.heapify(arr)  # 原地建堆，O(n)
    # 2. 依次弹出最小值，放入结果列表
    return [heapq.heappop(arr) for _ in range(len(arr))]


def MergeSort(arr: List[int]) -> List[int]:
    r"""
    归并排序（Merge Sort）基本思想：
    采用经典的分治策略，先递归地将当前数组平均分成两半，然后将有序数组两两合并，最终合并成一个有序数组。

    Parameters
    ----------
    arr : List[int]
        待排序整数列表

    Returns
    -------
    List[int]
        排序后的整数列表（返回新列表，不改变原列表）
    """
    def merge(left: List[int], right: List[int]) -> List[int]:
        """合并两个已排序列表"""
        merged = []
        i = j = 0
        len_left, len_right = len(left), len(right)

        # 按序取较小者放入 merged
        while i < len_left and j < len_right:
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # 将剩余部分直接追加
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sort(nums: List[int]) -> List[int]:
        """递归分治"""
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left_sorted = sort(nums[:mid])
        right_sorted = sort(nums[mid:])
        return merge(left_sorted, right_sorted)

    return sort(arr)


def BucketSort(arr: List[int], bucket_size: int) -> List[int]:
    r"""
    桶排序（Bucket Sort）基本思想：
    桶排序是一种非比较排序算法，它将待排序的元素分配到有限数量的桶中，每个桶再分别进行排序，最后将所有桶中的元素依次取出，即可得到有序序列。

    Parameters
    ----------
    arr : List[int]
        待排序整数列表
    bucket_size : int
        桶的数量

    Returns
    -------
    List[int]
        排序后的整数列表（返回新列表，不改变原列表）
    """
    if not arr or bucket_size <= 0:
        return arr[:]  # 空输入或非法桶数，直接返回拷贝

        # 1. 求数组长度、最小值、最大值
    n = 0
    min_val = max_val = None
    for num in arr:
        n += 1
        if min_val is None or num < min_val:
            min_val = num
        if max_val is None or num > max_val:
            max_val = num

    # 2. 计算桶宽
    span = max_val - min_val + 1
    bucket_width = (span + bucket_size - 1) // bucket_size  # 向上取整

    # 3. 创建桶
    buckets: List[List[int]] = [[] for _ in range(bucket_size)]

    # 4. 分配元素到桶
    for num in arr:
        idx = (num - min_val) // bucket_width
        if idx >= bucket_size:  # 边界保护
            idx = bucket_size - 1
        buckets[idx].append(num)

    # 5. 对每个桶内部使用插入排序（也可替换成其他排序）
    for bucket in buckets:
        InsertionSort(bucket)

    # 6. 合并所有桶
    result: List[int] = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def RadixSort(arr: List[int]) -> List[int]:
    r"""
    基数排序（Radix Sort）基本思想：
    将整数按位数切割成不同的数字，然后从低位开始，依次到高位，逐位进行排序，从而达到排序的目的

    Parameters
    ----------
    arr

    Returns
    -------

    """
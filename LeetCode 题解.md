# LeetCode 175 题解

## 一、哈希表

### 1.1 [两数之和](https://leetcode.cn/problems/two-sum/)

**问题描述：** 给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个 hash map 用于存储
        # {'num': 'index'}
        mapping = defaultdict(int)

        # 遍历数组
        for i, num in enumerate(nums):
            # 计算差值
            diff = target - num
            # 如果差值在 hash map 中，则返回
            if diff in mapping:
                return [mapping[diff], i]
            # 否则将当前值和索引存入 hashmap
            mapping[num] = i

        return []

```

### 1.2 [字母异位词分组](https://leetcode.cn/problems/group-anagrams/)

**问题描述：** 给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

**字母异位词** 是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 初始化一个 hashmap 用于存储
        # {'sorted string': ['anagrams']}
        mapping = defaultdict(list)

        # 遍历字符串数组
        for s in strs:
            # 对字符串排序
            sorted_s = "".join(sorted(s))
            # 将排序后的字符串和原字符串存入 hashmap
            mapping[sorted_s].append(s)

        # 返回 hashmap 的值
        return list(mapping.values())
```

### 1.3 [最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/)

**问题描述：** 给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 初始化一个集合
        nums_set = set(nums)

        # 初始化最长连续序列长度
        longest_streak = 0

        # 遍历数组
        for num in nums_set:
            # 如果当前数字的前一个数字不在集合中，则说明当前数字是连续序列的起点
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # 继续寻找连续序列
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # 更新最长连续序列长度
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

```

### 1.4 [找出两数组的不同](https://leetcode.cn/problems/find-the-difference-of-two-arrays/)

**问题描述：** 给你两个下标从 `0` 开始的整数数组 `nums1` 和 `nums2` ，请你返回一个长度为 `2` 的列表 `answer` ，其中：

- `answer[0]` 是 `nums1` 中所有 **不** 存在于 `nums2` 中的 **不同** 整数组成的列表。
- `answer[1]` 是 `nums2` 中所有 **不** 存在于 `nums1` 中的 **不同** 整数组成的列表。

**注意：**列表中的整数可以按 **任意** 顺序返回。

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 利用集合运算即可实现
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = list(set1 - set2)
        list2 = list(set2 - set1)
        return [list1, list2]
```

### 1.5 [独一无二的出现次数](https://leetcode.cn/problems/unique-number-of-occurrences/)

**问题描述：** 给你一个整数数组 `arr`，如果每个数的出现次数都是独一无二的，就返回 `true`；否则返回 `false`。

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 使用 Counter 计数器
        arr_count = Counter(arr)
        arr_set = set(arr_count.values())
        return len(arr_count) == len(arr_set)
```

### 1.6 [确定两个字符串是否接近](https://leetcode.cn/problems/determine-if-two-strings-are-close/)

**问题描述：** 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 **接近** ：

- 操作 1：交换任意两个 **现有** 字符。
  - 例如，`abcde -> aecdb`
- 操作 2：将一个 **现有** 字符的每次出现转换为另一个 **现有** 字符，并对另一个字符执行相同的操作。
  - 例如，`aacabb -> bbcbaa`（所有 `a` 转化为 `b` ，而所有的 `b` 转换为 `a` ）

你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，`word1` 和 `word2` 。如果 `word1` 和 `word2` **接近** ，就返回 `true` ；否则，返回 `false` 。

 ```python
 class Solution:
     def closeStrings(self, word1: str, word2: str) -> bool:
         # 边界条件：如果两个字符串长度不同，则不可能通过交换字符得到
         if len(word1) != len(word2):
             return False
         
         # 统计每个字符出现的次数
         freq1 = Counter(word1)
         freq2 = Counter(word2)
 
         # 条件 1：两个字符串必须包含相同的字符集合
         # 因为操作 2 只能在现有字符间转换，不能引入新字符
         if set(freq1.keys()) != set(freq2.keys()):
             return False
         
         # 条件 2：两个字符串的字符频率集合必须相同
         # 因为操作 1 可以重排字符顺序，操作 2 可以交换字符频率
         if sorted(freq1.values()) != sorted(freq2.values()):
             return False
         
         return True
 ```

### 1.7 [相等行列对](https://leetcode.cn/problems/equal-row-and-column-pairs/)

**问题描述：** 给你一个下标从 **0** 开始、大小为 `n x n` 的整数矩阵 `grid` ，返回满足 `Ri` 行和 `Cj` 列相等的行列对 `(Ri, Cj)` 的数目*。*

如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 统计所有行模式的频率
        row_patterns = Counter(
            tuple(row) for row in grid
        )

        # 统计所有列模式的频率
        col_patterns = Counter(
            tuple(grid[i][j] for i in range(n)) for j in range(n)
        )

        # 计算匹配的对数
        count = 0
        for pattern, row_freq in row_patterns.items():
            col_freq = col_patterns.get(pattern, 0)
            count += row_freq * col_freq

        return count
```

## 二、双指针

### 2.1 [移动零](https://leetcode.cn/problems/move-zeroes/)

**问题描述：** 给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意** ，必须在不复制数组的情况下原地对数组进行操作。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # 指向下一个 0 应该被替换的位置

        # 第一步：将所有非零元素移动到前面
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # 第二步：将剩余位置设为0
        while left < len(nums):
            nums[left] = 0
            left += 1
```

### 2.2 [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

**问题描述：** 给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # 计算当前容器面积
            # 面积 = 宽度 × 高度(取较短的一边)
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            max_area = max(area, max_area)

            # 移动较短的那根线，因为这样才能可能找到更大的面积
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

### 2.3 [三数之和](https://leetcode.cn/problems/3sum/)

**问题描述：** 给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 边界情况
        if len(nums) < 3:
            return []

        # 对数组进行排序
        nums.sort()

        # 初始化结果列表
        res = []

        # 遍历数组
        for i in range(len(nums) - 2):
            # 如果最小值都大于 0，则跳出
            if nums[i] > 0:
                break

            # 如果当前值与前一个值相同，则跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 初始化左右指针
            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # 移动左右指针，跳过重复值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return res
```

### 2.4 [接雨水](https://leetcode.cn/problems/trapping-rain-water/)

**问题描述：** 给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if len(height) < 3 or not height:
            return 0

        # 初始化左右指针和结果
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        # 遍历数组
        while left < right:
            # 更新左右最大值
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 根据左右最大值决定移动方向
            if left_max < right_max:
                # 左边较小，计算左边位置的雨水
                res += left_max - height[left]
                left += 1
            else:
                # 右边较小，计算右边位置的雨水
                res += right_max - height[right]
                right -= 1

        return res
```

### 2.5 [判断子序列](https://leetcode.cn/problems/is-subsequence/)

问题描述：给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 如果 s 为空，则空字符串永远为 t 的子序列
        if not s:
            return True
        # 如果 t 为空，则 s 永远不为 t 的子序列
        if not t:
            return False

        i = 0  # s 的指针
        j = 0  # t 的指针

        while i < len(s) and j < len(t):
            # 如果 s[i] == t[j] 说明有匹配字符
            if s[i] == t[j]:
                i += 1
            # t 的指针永远后移
            j += 1

        # 如果 s 的所有字符都被匹配，则 s 是 t 的子序列
        return i == len(s)
```

### 2.6 [K 和数对的最大数目](https://leetcode.cn/problems/max-number-of-k-sum-pairs/)

**问题描述：** 给你一个整数数组 `nums` 和一个整数 `k` 。

每一步操作中，你需要从数组中选出和为 `k` 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 统计每个数字的出现次数
        count = defaultdict(int)
        operations = 0

        for num in nums:
            need = k - num  # 我们需要的配对数字

            if count[need] > 0:
                # 找到了配对，执行一次操作
                operations += 1
                count[need] -= 1  # 减少配对数字的计数
            else:
                # 没有配对，将当前数字加入等待配对
                count[num] += 1

        return operations
```

## 三、滑动窗口

### 3.1 [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

**问题描述：** 给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串** 的长度。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 边界条件
        if not s:
            return 0

        # 初始化滑动窗口和结果
        window = set()
        left, max_len = 0, 0

        for right, char in enumerate(s):
            # 如果字符在窗口中，则移动左指针
            while char in window:
                window.remove(s[left])
                left += 1
            # 更新窗口和结果
            window.add(char)
            max_len = max(max_len, right - left + 1)

        return max_len
```

### 3.2 [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

**问题描述：** 给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 **异位词** 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 边界条件
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []

        res = []

        # 初始化统计 p 中每个字符的频次
        p_count = Counter(p)

        # 初始化窗口的字符频次
        window_count = Counter(s[:p_len])

        # 检查初始窗口
        if window_count == p_count:
            res.append(0)

        # 滑动窗口
        for i in range(p_len, len(s)):
            # 添加新字符
            window_count[s[i]] += 1

            # 移除旧字符
            window_count[s[i - p_len]] -= 1
            if window_count[s[i - p_len]] == 0:
                del window_count[s[i - p_len]]

            # 检查当前窗口
            if window_count == p_count:
                res.append(i - p_len + 1)

        return res
```

### 3.3 [子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)

**问题描述：** 给你一个由 `n` 个元素组成的整数数组 `nums` 和一个整数 `k` 。

请你找出平均数最大且 **长度为 `k`** 的连续子数组，并输出该最大平均数。

任何误差小于 `10-5` 的答案都将被视为正确答案。

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 计算第一个窗口的和
        window_sum = sum(nums[:k])
        max_sum = window_sum
        # 滑动窗口：移除左边元素，添加右边元素
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

```

### 3.4 [定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

**问题描述：** 给你字符串 `s` 和整数 `k` 。

请返回字符串 `s` 中长度为 `k` 的单个子字符串中可能包含的最大元音字母数。

英文中的 **元音字母** 为（`a`, `e`, `i`, `o`, `u`）。

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        # 计算第一个窗口中的元音字母数
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # 滑动窗口
        for i in range(k, len(s)):
            # 移除窗口左边的字符
            if s[i - k] in vowels:
                current_vowels -= 1
            # 添加窗口右边的新字符
            if s[i] in vowels:
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)

        if max_vowels == k:
            return k

        return max_vowels
```




import bisect

nums = [1, 1, 2, 3, 3, 3, 5, 8, 10]
"""
- bisect用法:
p = bisect.bisect_left(a, x, lo, hi) # 第一个大于等于x的元素位置
p = bisect.bisect_right(a, x, lo, hi) # 第一个大于x的元素的位置

"""
print(bisect.bisect_left(nums, 3, lo=0, hi=len(nums)-1))
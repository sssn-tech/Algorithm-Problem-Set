#
# @lc app=leetcode.cn id=2513 lang=python3
#
# [2513] 最小化两个数组中的最大值
#

# @lc code=start
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:

        def can_do(k):
            """
            - 可以被d1整除, 不能被d2整除: 只能放在arr2
            - 可以被d2整除, 不能被d1整除: 只能放在arr1
            - 不能被d1, d2整除: 可以放在arr1, arr2
            """
            z = k // math.lcm(divisor1, divisor2) # 同时被d1, d2整除
            
            a = k // divisor1 - z
            b = k // divisor2 - z
            if a >= uniqueCnt2 and b >= uniqueCnt1:
                return True
            else:
                gap = max(0, uniqueCnt2 - a) + max(0, uniqueCnt1 - b)
                return k - a - b - z >= gap

        l, r = 1, 10**10
        while l < r:
            mid = (l + r) >> 1
            print(mid, can_do(mid))
            if not can_do(mid):
                l = mid + 1
            else:
                r = mid 
        return l
        
# @lc code=end


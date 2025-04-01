class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # 答案是最长的0区块(容忍中间有一段1)的长度
        import bisect
        if len(s) == 1:
            return int(s[0])
        
        s = '1' + s + '1'
        n = len(s)
        prefix_sums = []
        for ch in s:
            prefix_sums.append(int(ch) + (prefix_sums[-1] if prefix_sums else 0))
        # print(prefix_sums)
        if prefix_sums[-1] == 2:
            return 0
        
        lo = 0
        ans = 0
        while lo < n:
            lo_r = lo
            while lo_r + 1 < n and s[lo_r + 1] != '0':
                lo_r += 1
            val = prefix_sums[lo_r]
            hi = bisect.bisect_left(prefix_sums, val + 2)
            if hi < n and hi - lo_r > 3:
                while hi < n and s[hi] == '1':
                    hi += 1
                hi -= 1
                if hi - lo > ans:
                    minus = 0
                    if lo == 0 and hi == n - 1:
                        minus += 1
                    if hi - lo - minus > ans:
                        print('can do', lo, hi)
                        ans = hi - lo - minus
            lo += 1
            while lo < n and s[lo] == '0':
                lo += 1

            lo = 1
            n -= 1
            if ans == 0: 
                return prefix_sums[-2] - 1
             
        return ans
            
            
print(Solution().maxActiveSectionsAfterTrade('01'))
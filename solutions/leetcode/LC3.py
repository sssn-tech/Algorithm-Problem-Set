from collections import Counter

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n == 0 or n == 1:
        return n
    counter = Counter()
    lo, hi, ans = 0, 0, 0
    # 区间[lo, hi)是已知的无重复字符的最长子串
    while lo < n and hi < n:
        # print(lo, hi)
        while hi < n and counter[s[hi]] < 1:
            counter[s[hi]] += 1
            hi += 1
        ans = max(ans, hi - lo)
        while lo < hi and hi < n and counter[s[hi]] > 0:
            counter[s[lo]] -= 1
            lo += 1
    return ans 
print(lengthOfLongestSubstring('abcabcbb'))
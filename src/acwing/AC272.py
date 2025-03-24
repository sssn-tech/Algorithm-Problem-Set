from typing import *

def lcis(A: List[int], B: List[int]) -> int:
    """
    求最长公共上升子序列(LCIS)
    用dp[j]表示以B[j]结尾的LCIS长度
    遍历A的每个元素a, 对于每个a, 我们关心所有的b属于B, b<=a
    用current_max维护对于当前的a和b, 以b结尾的最长lcis长度
    当a == b时, 可以将current_max转移给b[j]
    if b < a:
        current_max = max(current_max, dp[j])
    if b == a:
        dp[j] = max(dp[j], current_max + 1)
    """
    dp = [0] * len(B)
    for a in A:
        current_max = 0
        for j, b in enumerate(B):
            if b < a:
                current_max = max(current_max, dp[j])
            if b == a:
                dp[j] = max(dp[j], current_max + 1)
    return max(dp) if dp else 0

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(lcis(A, B))




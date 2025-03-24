from typing import *
from functools import *
from itertools import permutations

def get_all_permute() -> List[List[int]]:
    # 返回1-9的全排列
    vis = [False] * 10
    all_permute = []
    def dfs(curr: List[int], p: int) -> None:
        if p >= 10:
            all_permute.append(curr.copy())
            return 
        for i in range(1, 10):
            if not vis[i]:
                curr.append(i)
                vis[i] = True
                dfs(curr, p + 1)
                vis[i] = False
                curr.remove(i)
    dfs([], 1)
    return all_permute

# all_permute = get_all_permute()
n = int(input())

# @cache
def list2num(ls: List[int]) -> int:
    return int(''.join(map(str, ls)))

# print(list2num([1, 2, 3, 6, 6]))
# 0 1 2 3 4 5 6 7 8
# 7 8 9 6 5 4 3 1 2

ans = 0
for permute in permutations('123456789'):
    # i 和 j 枚举分割位置, 后方分割
    # 分割出来的三个数是闭区间[0,i], [i+1,j], [j+1, 8]
    for i in range(7):
        for j in range(i + 1, 8):
            # print(i, j)
            a = list2num(permute[0:i+1])
            b = list2num(permute[i+1:j+1])
            c = list2num(permute[j+1:9])
            if a + b / c == n:
                ans += 1

print(ans)

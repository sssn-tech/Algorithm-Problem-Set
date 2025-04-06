from functools import cmp_to_key

n = int(input())
nums = list(map(int, input().split()))

get_cnt = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
def comp(x: int, y: int) -> bool:
    # 按照封闭图形的个数排序, 如果相同, 则按值排序
    # python的排序返回 负数, 0, 正数, 分别对应x在前, 相等, y在前
    x_cnt, y_cnt = 0, 0
    x_cp, y_cp = x, y
    while x_cp != 0:
        x_cnt += get_cnt[x_cp % 10]
        x_cp //=  10
    while y_cp != 0:
        y_cnt += get_cnt[y_cp % 10]
        y_cp //= 10
    if x_cnt != y_cnt:
        return x_cnt - y_cnt
    return x - y
     

nums.sort(key=cmp_to_key(comp))
for num in nums:
    print(num, end=' ')

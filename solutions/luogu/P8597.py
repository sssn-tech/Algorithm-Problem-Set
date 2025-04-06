# 因为一个同一个位置连续翻转两次等于没翻, 所以考虑贪心
# 从左到右遍历, 发现不一样的就翻

str1 = list(input())
str2 = list(input())

def get_reverse(c: chr) -> chr:
    if c == '*':
        return 'o'
    else:
        return '*'

ans = 0
for i in range(len(str1) - 1):
    if str1[i] != str2[i]:
        str1[i] = get_reverse(str1[i])
        str1[i + 1] = get_reverse(str1[i + 1])
        ans += 1
print(ans)

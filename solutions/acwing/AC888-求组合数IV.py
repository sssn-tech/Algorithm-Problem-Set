


n, k = map(int, input().split())

# C(n, k) = n! / k!(n-k)!
def C(n: int, k: int) -> int:
    res = 1
    b, c = 1, 1
    for i in range(n, 0, -1):
        res *= i
        if i <= k:
            res //= i 
        if i <= n-k:
            res //= i
    return res

print(C(n, k))
    

from math import *

def phi(x: int, MOD: int) -> int:
    # 欧拉函数的定义: 1-x中与x互质的数的个数
    # phi(x) = x * (1-1/p_1) * (1-1/p_2)*..., p是质因数
    if x == 0:
        return 0
    x %= MOD
    res = x
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            res = res * (i - 1) // i
            res %= MOD
            while x % i == 0:
                x //= i 
    if x > 1:
        res = res * (x - 1) // x
        res %= MOD
    return res 

def quick_pow(a: int, b: int, MOD: int) -> int:
    # 快速幂 a^b % MOD
    res = 1
    while b != 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res


a, b = map(int, input().split())
MOD = 998244353
# phi(a^b) = phi(a) * a^{b-1}
print((phi(a, MOD) * quick_pow(a, b-1, MOD)) % MOD)


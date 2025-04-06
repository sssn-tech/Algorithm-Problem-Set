
def quick_pow(a: int, b: int, p: int) -> int:
    # 快速幂返回a**b % p
    res = 1
    while b != 0:
        if b & 1:
            res = (res * a) % p
        a = (a * a) % p 
        b >>= 1
    return res 

n_max = int(1e5)
mod = int(1e9+7)
fact = [0 for _ in range(n_max+1)]
fact_inv = [0 for _ in range(n_max+1)]

fact[0] = fact_inv[0] = 1
for i in range(1, n_max + 1):
    fact[i] = (i * fact[i - 1]) % mod 
    fact_inv[i] = (fact_inv[i - 1] * quick_pow(i, mod-2, mod)) % mod

def combination(n: int, k: int) -> int:
    # C(n, k) = n! / k!(n-k)!
    return ((fact[n] * fact_inv[k]) % mod * fact_inv[n-k]) % mod

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(combination(n, k))



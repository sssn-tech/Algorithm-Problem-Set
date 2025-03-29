def qmi(a, k, p):
    res  = 1
    while k:
        if k & 1:
            res = res * a % p
        a = a * a % p
        k >>= 1
    return res

def C(n,k,p):
    res = 1
    j = n
    for i in range(1, k+1):
        res = res * j % p
        res = res * qmi(i, p-2, p) % p
        j-=1
    return res

def lucas(n,k,p):
    if n < p and k < p: return C(n,k,p)
    return C(n%p, k%p, p) * lucas(n//p , k//p, p) % p

for i in range(int(input())):
    n, k, p = map(int,input().split())
    print(lucas(n,k,p))

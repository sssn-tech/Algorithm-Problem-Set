# 基础算法

## 快速排序

非原地快速排序的优点是特别好写, 但是空间复杂度$O(NlogN)$到$O(N^2)$

```python
def quick_sort(nums: List[int]) -> List[int]:
    # 对一个数组快速排序, 返回排序后的数组
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2] # 选择中间数作为基准
    left = [num for num in nums if num < pivot]
    mid = [num for num in nums if num == pivot]
    right = [num for num in nums if num > pivot]
    
    return quick_sort(left) + mid + quick_sort(right)
```

## 快速选择

```python
def q_select(arr: List[int], k: int) -> int:
    # 返回arr中第k小的数
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left): # 第k小数在左边
        return q_select(left, k)
    elif k <= len(left) + len(middle): # 第k小数在中间
        return  pivot
    else: # 第k小数在右边
        return q_select(right, k - len(left) - len(middle))
```

## 归并排序

```python
def merge_sort(nums: List[int], l: int, r: int) -> None:
    # 原地归并排序[l, r)
    if r - l < 2: # 不足两个数不需要排序
        return 
    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid, r)
    
    temp = []
    i, j = l, mid
    while i < mid and j < r:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    if i >= mid:
        temp.extend(nums[j:r])
    else:
        temp.extend(nums[i:mid])
    nums[l:r] = temp
```

## 归并排序求逆序对数量

```python
def merge_sort(arr: List[int], l: int, r: int) -> int:
    # 统计[l, r)的逆序对数量
    # 逆序对数量 = 左半部分内部的 + 右半部分内部的 + 跨越左右的
    if r - l <= 1:
        return 0
    mid = (l + r) // 2
    left_cnt = merge_sort(arr, l, mid)
    right_cnt = merge_sort(arr, mid, r)
    cross_cnt = 0
    
    i, j = l, mid
    temp = []
    while i < mid and j < r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            cross_cnt += mid - i
    if i >= mid:
        temp.extend(arr[j:r])
    else:
        temp.extend(arr[i:mid])
    arr[l:r] = temp
    
    return left_cnt + right_cnt + cross_cnt
```

## 字符串编辑距离

```python
def edit_distance(s1: str, s2: str) -> int:
    """
    - 用dp[i][j]表示s1[:i]和s2[:j]的最小编辑距离, 注意不包括s1[i]和s2[j]
    - 不对其下标是因为我们需要考虑空子串的情况
    - if s1[i - 1] == s2[j - 1], dp[i][j] = dp[i - 1][j - 1]
    - else dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    - 要使s1向s2靠拢, 3种对i的操作法, 插入, 删除, 修改
    - 边界条件dp[i][0] = i, dp[0][j] = j, 代表空字符串的编辑距离
    """
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j 
            if j == 0:
                dp[i][j] = i 
            if i > 0 and j > 0:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

    return dp[n][m]
```

# 数论算法

## 快速幂

```python
def quick_pow(a: int, b: int, MOD: int) -> int:
    # 快速幂 a^b % MOD
    res = 1
    while b != 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res
```

## 辗转相除法

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
```

## 欧拉函数

```python
def phi(x: int) -> int:
    # 欧拉函数phi(x)的定义是[1, x]中与x互质的数的个数
    # phi(x) = x * (1 - 1/p_1) * (1 - 1/p_2) * ... 其中p_i是x的质因数
    res = x
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            res = res * (i - 1) // i
            while x % i == 0:
                x //= i
    if x > 1:
        res = res * (x - 1) // x # 如果最后x不是0, 则x本身是一个较大的质数
    return res
```

## 线性筛素数

```python
def get_primes(n: int) -> List[int]:
    # 欧拉筛返回n以内的所有质数(包括n)
    primes = []
    is_prime = [True] * (n + 1)
    if n < 2:
        return primes
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for prime in primes:
            if prime * i > n:
                break
            is_prime[prime * i] = False
            if i % prime == 0: # 欧拉筛核心: 每个合数只被自己的最小质因数筛去
                break
    return primes
```

## 筛法求欧拉函数

```python
def get_phis(n: int) -> List[int]:
    # 将n以内(包含)的欧拉函数以列表返回
    phi = [0] * (n + 1)
    for i in range(n + 1):
        phi[i] = i
    for i in range(2, n + 1):
        if phi[i] == i:  # i 是质数
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi
```

## 四种组合数求法: $C_n^k$

### 普通求法

```python
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
```

### DP出所有查询

$$C_n^k = C_{n-1}^k + C_{n-1}^{k-1}$$

#### 记忆化

```python
mem = {}  # 用字典记忆化
mod = int(1e9+7)
def combination(n: int, k: int):
    # 返回C(n, k), n选k
    token = (n, k)
    if token in mem:
        return mem[token]
    # 处理无效情况
    if k < 0 or n < k or n < 0:
        res = 0
    elif k == 0 or n == k:
        res = 1
    else: # C(n, k) = C(n-1, k) + C(n-1, k-1)
        res = (combination(n-1, k) + combination(n-1, k-1)) % mod
    mem[token] = res % mod
    return res % mod
```

#### 递推

```python
n_max = 2000
mod = int(1e9+7)
c = [[0 for _ in range (n_max + 1)] for _ in range(n_max + 1) ]  

# 递推建表
# c(n, k) = c(n-1, k) + c(n-1, k-1)
for i in range(0, n_max + 1):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = (c[i-1][j] + c[i-1][j-1]) % mod
```

### 预处理阶乘和阶乘逆元(要求p为质数)

```python
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
```

### Lucas定理(p为质数, n, k过大无法预处理)

```python
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
```

## 扩展欧几里德算法

```python
def extended_gcd(a, b):
    """
    扩展欧几里得算法
    返回 gcd, x, y 使得 ax + by = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
```

## 扩展欧求乘法逆元

```python
# 上面的扩展欧不变
def mod_inverse(a, m):
    """
    计算 a 在模 m 意义下的逆元
    返回 x，使得 a * x ≡ 1 (mod m)
    如果逆元不存在（即 gcd(a, m) ≠ 1），返回 None
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # 不存在逆元
    else:
        return x % m  # 保证结果为正数
```

## 高斯消元求线性方程组

```python
def gaussian_elimination(matrix: List[float]):
    # matrix是n行n+1列的线性方程组
    # 返回解的情况, 如果有唯一解, 返回具体的解
    import copy

    EPS = 1e-8
    n = len(matrix)
    m = len(matrix[0]) - 1  # number of variables
    mat = copy.deepcopy(matrix)

    rank = 0
    where = [-1] * m

    for col in range(m):
        sel = rank
        for i in range(rank, n):
            if abs(mat[i][col]) > abs(mat[sel][col]):
                sel = i
        if abs(mat[sel][col]) < EPS:
            continue
        mat[rank], mat[sel] = mat[sel], mat[rank]
        where[col] = rank
        # Eliminate column
        for i in range(n):
            if i != rank and abs(mat[i][col]) > EPS:
                factor = mat[i][col] / mat[rank][col]
                for j in range(col, m + 1):
                    mat[i][j] -= factor * mat[rank][j]
        rank += 1

    for i in range(rank, n):
        if abs(mat[i][-1]) > EPS:
            return "No solution"
    if rank < m:
        return "Infinite group solutions"

    # Unique solution
    ans = [0] * m
    for i in range(m):
        if where[i] != -1:
            ans[i] = mat[where[i]][-1] / mat[where[i]][i]
    return ans
```

# 图论算法

## Dijkstra: 单源最短路首选

需要注意的是**Dijkstra不能用于含有负权边的图**

直接用堆优化版本

```python
from typing import *
import heapq

INF = float('inf')
def dijkstra(graph: List[List[Tuple[int, int]]], root: int) -> List[int]:
    # dijkstra求以root为起点的单源最短路径
    n = len(graph)
    dist = [INF] * (n + 1)
    dist[root] = 0
    
    pq = [(0, root)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: # 如果弹出的距离大于已知的最短, 那这条信息没用
            continue
        
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[u] + w, v))
        
    return dist
```

## SPFA: 含有负权的单源最短路

**不要在SPFA里用List[]当作队列! List的头部操作复杂度是$O(N)$的!**

```python
from typing import *
import heapq
from collections import deque
INF = float('inf')
def spfa(graph: List[List[Tuple[int, int]]], root: int) -> List[int]:
    # spfa求以root为起点的单源最短路径
    n = len(graph)
    dist = [INF] * (n + 1)
    dist[root] = 0
    
    queue = deque([root])
    inque = [False] * (n + 1)
    inque[root] = True
    while queue:
        u = queue.popleft()
        inque[u] = False
        
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w 
                if not inque[v]:
                    queue.append(v)
                    inque[v] = True
    return dist
```

## Bellman-Ford: 最多经过k条边的单源最短路

Bellman-Ford算法是枚举边的算法, 因此需要用edges存图, 这点需要记清楚

```python
from typing import *

INF = float('inf')
n, m, k = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    
def bellman_ford_k(edges: List[Tuple[int, int, int]], n: int, k: int, src: int) -> List[int]:
    # 最多经过k条边的最短路
    dist = [INF for _ in range(n + 1)]
    dist[src] = 0
    
    for _ in range(k):
        dist_copy = dist.copy()
        for u, v, w in edges:
            if dist[v] > dist_copy[u] + w:
                dist[v] = dist_copy[u] + w
    
    return dist

dist = bellman_ford_k(edges, n, k, 1)
print(dist[n] if dist[n] != INF else 'impossible')
```

## Floyed: 多源最短路

```python
from typing import *
INF = 10**18

n, m, k = map(int, input().split())
graph = [[INF for j in range(n + 1)] for i in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)

for i in range(1, n + 1):
    graph[i][i] = 0

for t in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
          	# 这个判断INF的的地方值得注意: 如果不判断INF, 可能会被负权边更新
            if graph[i][t] < INF and graph[t][j] < INF:
                graph[i][j] = min(graph[i][j], graph[i][t] + graph[t][j])

for _ in range(k):
    u, v = map(int, input().split())
    print(graph[u][v] if graph[u][v] != INF else 'impossible')

```

## Prim: 稠密图最小生成树

```python
def primMST(graph: List[List[Tuple[int, int]]], n: int) -> int:
    # prim最小生成树, 返回MST长度
    dist = [INF for _ in range(n + 1)] # 每个点到MST的距离
    MSTnodes = set() 
    MSTlen = 0
    heap = []

    dist[1] = 0 # 令1为起始点
    heapq.heappush(heap, (0, 1)) 

    while heap:
        d, u = heapq.heappop(heap)
        if u in MSTnodes:
            continue
        MSTnodes.add(u)
        MSTlen += d 
        
        for v, w in graph[u]:
            if v not in MSTnodes and dist[v] > w:
                dist[v] = w
                heapq.heappush(heap, (w, v))
                
    return MSTlen if len(MSTnodes) == n else INF
```

## 最近公共祖先(LCA)

### Tarjan求最近公共祖先

```python
def tarjan_lca(adj_list: List[List[int]], root: int, queries: List[Tuple[int, int]]) -> List[int]:
    """
    adj_list: 树的临接表, 以无向图形式存储
    root: 树根, queries: 元组列表, 每个元素(u, v)代表一次查询
    """
    parent = {}
    ancestor = {}
    visited = set()
    uf_parent = {}
    result = {}
    # 初始化查询映射
    query_map = defaultdict(list)
    for idx, (u, v) in enumerate(queries):
        query_map[u].append((v, idx))
        query_map[v].append((u, idx))

    def find(u):
        if uf_parent[u] != u:
            uf_parent[u] = find(uf_parent[u])
        return uf_parent[u]
      
    def union(u, v):
        uf_parent[find(u)] = find(v)
        
    def dfs(u, parent_node):
        uf_parent[u] = u
        ancestor[u] = u
        for v in adj_list[u]:
            if v == parent_node:
                continue  # 跳过父节点
            if v not in visited:
                dfs(v, u)  # 传递当前节点作为父节点参数
                union(v, u)
                ancestor[find(u)] = u
        visited.add(u)
        for v, idx in query_map[u]:
            if v in visited:
                result[idx] = ancestor[find(v)]

    dfs(root, None)  # 根节点的父节点设为None

    # 返回结果列表
    return [result[i] for i in range(len(queries))]
```

### 倍增法求LCA

```python
def bin_lifting_lca(adj_list: List[List[int]], root: int, queries: List[Tuple[int, int]]) -> List[int]:
    n = len(adj_list)
    LOG = math.ceil(math.log2(n)) + 1  # 最大倍增层数, math.ceil是向上取整
    parent = [[-1] * LOG for _ in range(n)]  # parent[node][k] 表示 node 的 2^k 级祖先
    depth = [0] * n
    visited = [False] * n

    def dfs(u: int, p: int):
        visited[u] = True
        parent[u][0] = p
        for v in adj_list[u]:
            if not visited[v]:
                depth[v] = depth[u] + 1
                dfs(v, u)

    # Step 1: DFS 初始化 parent[0] 和 depth
    dfs(root, -1)
    # Step 2: 预处理所有 2^k 级祖先
    for k in range(1, LOG):
        for v in range(n):
            if parent[v][k - 1] != -1:
                parent[v][k] = parent[parent[v][k - 1]][k - 1]
                
    def get_lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u
        # Step 3: 将 u 提升到和 v 同一深度
        for k in reversed(range(LOG)):
            if parent[u][k] != -1 and depth[parent[u][k]] >= depth[v]:
                u = parent[u][k]
        if u == v:
            return u
        # Step 4: 同时向上跳，直到找到 LCA
        for k in reversed(range(LOG)):
            if parent[u][k] != -1 and parent[u][k] != parent[v][k]:
                u = parent[u][k]
                v = parent[v][k]
        return parent[u][0]

    # Step 5: 处理所有查询
    return [get_lca(u, v) for u, v in queries]
```

## 染色法判断二分图

```python
def is_bipartite(graph: List[List[int]]) -> bool:
    n = len(graph) - 1 # 0-base 和 1-base转换, 我的graph是1-base的, 所以实际节点数得-1
    colors = [0 for _ in range(n + 1)] # 0是无颜色, 1和-1是两种颜色
    
    def bfs(graph: List[List[int]], src: int):
        colors[src] = 1 
        que = deque([src])
        
        while que:
            u = que.popleft()
            for v in graph[u]:
                if colors[v] == colors[u]:
                    return False
                if colors[v] == 0:
                    colors[v] = -colors[u]
                    que.append(v)
                    
        return True
    
    for src in range(1, n + 1):
        if colors[src] == 0 and not bfs(graph, src):
            return False
    return True
```

## 匈牙利算法: 二分图最大匹配

```python
def hungarian_match_count(graph: List[List[int]], n1: int, n2: int) -> int:
    # 匈牙利算法二分图最大匹配
    # 左半部[1-n1], 右半部[1-n2], 编号可以重叠, 因为graph只存了左到右的边
    match = [0 for _ in range(n2 + 1)]
    
    def find(state: List[bool], match: List[int], u: int) -> bool:
        for v in graph[u]:
            if not state[v]:
                state[v] = True
                if match[v] == 0 or find(state, match, match[v]):
                    match[v] = u
                    return True
        return False

    res = 0
    for u in range(1, n1 + 1):
        state = [False for _ in range(n2 + 1)]
        if find(state, match, u):
            res += 1
    return res
```

# 常用工具总结

## python读入优化sys.read()



## 时间逃课工具datetime

```python
from datetime import datetime
from datetime import timedelta

# 新建一个时间, 1970年1月1日0时0分0秒
t1 = datetime(1970, 1, 1, 0, 0, 0)

# 从字符串分析出时间 str-parse-time
str = '2002-3-1-19-00-00'
t2 = datetime.strptime(str, '%Y-%m-%d-%H-%M-%S')

# 将时间导出为字符串, str-formate-time
str = t2.strftime('year: %Y month: %m day: %d:: %H:%M:%S')

# 日期不能相加, 但是可以相减得到timedelta
# d = t1 + t2
d:timedelta = t2 - t1
# 日期可以加减timedelta
t2 = t2 - timedelta(seconds=200)

# 日期可以修改任意成员变量
t2 = t2.replace(year=1999, day=1)
```

## 自定义排序规则

### 用key=给出排序主键

```python
arr = [(1, 2, 3), (1, 8, 9), (9, -2, 0)]
arr.sort(key=lambda x:  x[2]) # 用一元lambda函数直接给出key
```

### functools.cmp_to_key()函数

functools.cmp_to_key()函数是类似C++风格的写法, 可以自己写一个排序函数

```python
arr = [(1, 2, 3), (1, 8, 9), (9, -2, 0)]
arr.sort(key=cmp_to_key(lambda x, y: x[2] - x[2])) # 二元lambda函数
```

```python
# 写一个具有C++风格的排序比较函数
arr = [(1, 2, 3), (1, 8, 9), (9, -2, 0)]
def cmp(x, y) -> int:
    # 在python中, cmp函数的返回值有三种
    # 正数代表x在前, 相等代表相同优先级, 负数代表y在前
    return x[2] - y[2]
arr.sort(key=cmp_to_key(cmp))
```

### 自定义\_\_lt\_\_(), \_\_gt\_\_()等比较函数

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        """小于运算符 `<`"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __gt__(self, other):
        """大于运算符 `>`"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age
```

结合functools的total_odering, 可以通过实现lt()和eq()两个函数来自动定义出剩余的比较

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

# 这样就自动支持 <=, >=, >, <, ==, !=
```

## 优先队列heapq

几个基本操作

```python
import heapq

nums = [5, 1, 8, 3, 2]

heapq.heapify(nums) # 转换为最小堆（原地操作）
print(nums)  # 输出：[1, 2, 8, 3, 5]（堆的结构可能不同，但堆顶一定是最小值）

heapq.heappush(nums, 0) # 插入元素
num = heapq.heappop(nums) # 弹出元素
```

在元素为复杂元素时, heapq默认使用元组的第一个元素排序

```python
# (priority, item) 形式
tasks = [(3, "Task C"), (1, "Task A"), (2, "Task B")]

heapq.heapify(tasks)

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Processing {task} with priority {priority}")
```

## 双端队列collections.deque

**不要用List模拟队列! List头部操作的复杂度是$O(N)$的!**

append和pop有点难记, 只需记住deque只有left需要强调, 没有right的方法就对了

```python
from collections import deque

# 创建一个双端队列
dq = deque([1, 2, 3, 4])

# 右侧添加元素
dq.append(5)  # [1, 2, 3, 4, 5]

# 左侧添加元素
dq.appendleft(0)  # [0, 1, 2, 3, 4, 5]

# 右侧删除元素
dq.pop()  # 删除 5 -> [0, 1, 2, 3, 4]

# 左侧删除元素
dq.popleft()  # 删除 0 -> [1, 2, 3, 4]

```

## 整数二分bisect

### 二分查找

```python
import bisect
# lo, hi可以省略, 默认查找整个有序列表
p = bisect.bisect_left(a, x, lo, hi) # 第一个大于等于x的元素位置
p = bisect.bisect_right(a, x, lo, hi) # 第一个大于x的元素的位置
```

### 维护有序数组

```python
a = [1, 3, 3, 5, 7]
bisect.insort_right(a, 3) # 将3插入到有序数组中
```

## 排列组合: 迭代工具itertools

```python
import itertools

# 生成排列
perms = list(itertools.permutations([1, 2, 3]))
print(perms)  # [(1,2,3), (1,3,2), (2,1,3), ...]

# 生成组合
combs = list(itertools.combinations([1, 2, 3], 2))
print(combs)  # [(1,2), (1,3), (2,3)]
```

## 集合运算Set

```python
# 集合可以用花括号初始化, 但是空花括号不是集合, 而是字典
# 如果要创建空集, 只能用set()
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}

intersection_result = set1 & set2 # 交集1
intersection_result = set1.intersection(set2) # 交集2

union_result = set1 | set2 # 并集1
union_result = set1.union(set2) # 并集2

difference_result = set1 - set2 # 差集1
difference_result = set1.difference(set2) # 差集2

symmetric_difference_result = set1 ^ set2 # 对称差集1
symmetric_difference_result = set1.symmetric_difference(set2) # 对称差集1

```

## 类型检查: isinstance()与type()

```python
x = 10
print(isinstance(x, int))  # True
print(isinstance(x, float))  # False
print(type(x) == int)        # True

# isinstance() 会考虑继承关系, 而type()不会
```

## python的格式化输出

### .format方法(python3)

```python
print("My name is {0}, and I am {1} years old.".format(name, age))
print("My name is {n}, and I am {a} years old.".format(n=name, a=age))
pi = 3.14159
print("Pi is {:.2f}".format(pi))  # 输出 Pi is 3.14
```

### f-string方法(python3.6+), 最方便

```python
name = "Charlie"
age = 28
print(f"My name is {name}, and I am {age} years old.")
pi = 3.14159
print(f"Pi rounded to 2 decimals: {pi:.2f}")
```

### 对齐

```python
print(f"{'Python':^10}")  # 居中
print(f"{'Python':<10}")  # 左对齐
print(f"{'Python':>10}")  # 右对齐
```


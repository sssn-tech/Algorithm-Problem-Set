# python算法板子与技巧总结



# 算法模板

## 快速排序

### 非原地快排

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

### 原地快排

```python
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
def gcd(a, b):
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

## 欧拉筛素数

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

python的Set提供的基本的集合运算

```python
# 集合可以用花括号初始化, 但是空括号不是集合, 而是字典
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


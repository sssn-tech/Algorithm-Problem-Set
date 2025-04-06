# 算法题分类题单与思路总结

又开一新坑, 记录一下最近重新刷题的历程

所有题会按照主要知识点分类, 难度递增, 适合按模块集中练习, 并总结经验, 内化为自己的知识. 

每道题我会简评两句, 并尝试总结出每类题型的特征. 简评点到为止, 起到暗示作用, 适合学习过数据结构的同学参考. 

题目来源: Leetcode, Luogu, Acwing, 蓝桥杯官网. 

我会记录我个人认为有价值, 可以带来思考的题目. 不会记录偏难怪题. 

## 贪心

贪心题最难的是看出来这是贪心题

很多题的贪心策略听起来匪夷所思, 让人听了之后也觉得: 好像有道理, 但是为什么这就是最优?

#### [Leetcode2712-使字符相等的最小成本](https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal/description/)

给一个01串, 每次你可以选择将一个前缀全部反转, 或将一个后缀全部反转, 反转的花费是前后缀长度

问使这个串统一的最小成本是多少

> 先从数据范围猜到是O(N)级别做法
>
> 然后用双指针找贪心策略, 双指针是lo, hi, 当s[lo] != s[lo - 1]的时候, 无论如何是得翻的, 显然此时就翻[0-lo]代价最小
>
> 然后思考双指针撞车时候的处理, 三种情况讨论一下, 讨论完发现lo<=hi是一样的

## 前缀和

蓝桥杯最爱考的题型之一, 板子很简单, 但是考法可以比较巧妙

特征是频繁的区间求和, 求异或和, 求或和, 甚至是求区间的一些函数

#### [Leetcode560-和为K的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/description/)

给一个有正有负的数组, 求里面有多少个连续子数组和为K

> 看到"和为K的子数组"很难不想到前缀和, 但之后怎么办? n = 2e4, 明显不能枚举区间起点和终点
>
> 这里要借鉴"两数之和"的思想

#### [Leetcode42-接雨水](https://leetcode.cn/problems/trapping-rain-water/description/)

经久不衰的经典面试题

<img src="https://pic.cirno.fun/sssn-blog-pics/rainwatertrap-20250324175419632.png" alt="img" style="zoom:67%;" />

给一个这样的数组, 问能接多少个单位的雨水?

> 实际上, 一个下标i处可以接到的雨水量是取决于左右区间最高点的较低的那个: min(max(height[:i], height[i+1:]))
>
> 此外, 这种题还可以用**枚举右, 维护左**的方式, 优化一次遍历的复杂度

#### [Leetcode2680-最大或值](https://leetcode.cn/problems/maximum-or/description/)

有一个整数数组nums, 你有k次操作机会, 每次操作可以任选一个数乘2, 求能得到的最大或和(nums[0] | nums[1] | nums[2] | ...)

> 两个思维点: 
>
> 1. 所有的k次操作操作必须施加在一个数上 (如何证明?)
> 2. 可以枚举所有的数, 尝试对他操作, 用前后缀和更新答案
>
> 可以**枚举右, 维护左**优化

#### [Leetcode135-分发糖果](https://leetcode.cn/problems/candy/description/)

有一排小孩, 每一个小孩有一个评分, 所以你拿到了一个评分数组ratings[]

你必须给每个孩子至少发一个糖果, 并保证如果相邻的孩子中, 评分更高的那个拿到更多糖果(相邻但相同评分孩子可以不一样), 求最少发多少糖果

> 我觉得这也是前缀和
>
> 维护两个数组left[], right[], 分别记录只看左边(右边), 一个孩子最少发多少糖果, 则这个孩子应该发max(left[i], right[i])
>
> 同样的, 可以**枚举右, 维护左**来优化

#### [Leetcode2874-有序三元组中的最大值II](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/description/)

有一个数组nums, 规定三元组i < j < k, 令val = (nums[i] - nums[j]) * nums[k], 求val最大值

> 不用求前缀和了, 换成前缀最大值, 总之还是前后缀的那一套

## 哈希表

#### [Leetcode2829-k-avoiding 数组的最小和](https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description/)

> 和"两数之和"一摸一样, 双倍经验
>
> 不知道给个n<=50的数据范围是闹哪样, 搞得我以为是搜索, 其实没啥关系

#### [Leetcode560-和为K的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/description/)

> 参见前缀和中的本题

## 差分数组

没太在竞赛里见过

差分数组是前缀和的逆运算, 题目特征是**对一个点的操作会映射到区间上**

## 滑动窗口

Leetcode与互联网面试非常爱出各种滑动窗口

#### [Leetcode3-无重复字符的最大子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

给定一个字符串, 求最长的连续子串, 满足没有重复字符

> 滑动窗口板子题, 先延展右边, 再退缩左边, 注意处理边界
> 虽然简单, 但要体会这个思想

#### [Leetcode438-找到字符串中所有的异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

给定一个长字符串s和一个短字符串p, 求s中所有p的异位词的开始下标

异位词: 长度相同, 所有字母出现频次相同

> 可以用定长滑动窗口, 也可以用不定长的
>
> 不要每次重新统计字母出现频率, 太慢了

## 搜索

#### [Acwing187-导弹拦截系统](https://www.acwing.com/problem/content/189/)

给定一个数组, 求他最少可以被分解成多少个严格单调子序列

比如[3, 5, 2, 4, 1]最少被分解为[3, 4]和[5, 2, 1]两个

> 搜索+剪枝+LIS的题, 有点难度
>
> Acwing的数据卡的很死, python容易T掉一个点
>
> 依次枚举每个数, 他只可能被append到一个递增子序列后, 或者一个递减子序列后
>
> 用LIS的NlogN做法那个数组来维护所有的系统处理的导弹序列

## 动态规划

### 线性DP(走楼梯模型)

- 有非常明显的线性依赖关系 
- 和方案数, 排列组合数强相关

#### [Leetcode70-爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)

大部分人学DP的第一道

> 所有爬楼梯模型的母题, 后面再变, 思维底层就在这

#### [Leetcode2466-统计构造好字符串的方案数](https://leetcode.cn/problems/count-ways-to-build-good-strings/description/)

你要从空串开始构造字符串, 每次可以append n个0或者m个1

问可以构造出多少个长度在[lo, hi]区间的字符串

> 还是爬楼梯, 一次爬n个台阶或者m个台阶
>
> 注意了, 这种统计方案数的dp不要随便+1
>
> 假设到a状态有na种方案, a状态可以去b状态, 则nb累加na就行, 不要+1

#### [Leetcode377-排列总和IV](https://leetcode.cn/problems/combination-sum-iv/)

给你一个数组nums, 一个目标整数target, 问有多少种总和为target的选法

- 注意, [1, 3]和[3, 1]算两种选法

> 上面这个注意一出, 就要想到DP
>
> 和2466太像了, 延续累加的思想

#### [Leetcode2266-统计打字方案数](https://leetcode.cn/problems/count-number-of-texts/description/)

> 只要能想到走楼梯, 这题就很简单
>
> 把字符串切开, 弄一个走楼梯就行
>
> 还有一个重要优化, 要意识到走楼梯问题的本质是(长度, 方案), 所以处理切开的字符串的函数是(int, int)的, 并且方案只有3种, 4种两类

#### [Leetcode2140-解决智力问题](https://leetcode.cn/problems/solving-questions-with-brainpower/description/)

有一个有序二元组, 每个元素是(收益, 代价), 代价cost是你不能选择接下来的cost个元素

问你最大收益多少

> 可以用记忆化搜索, 也可以dp
>
> 用dp[i]表示从i开始到结尾的最大收益, 则dp[i]依赖于dp[i+1]和dp[i + cost]

### 我和我的子序列朋友们

给一个整数数组, 然后各种花样的子序列

#### [Leetcode300-最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description/)

每个人学DP避不开的一道题

给定一个nums, 求最长上升子序列(LIS)长度, 这个子序列是可以断的, 比如[1, 3, 5]是[1, 2, 3, 4, 5]的子序列

> 两种解法, N^2, NlogN
> 学完之后记得看一下二分库,C++ STL里的lower_bound, python的bisect, 都很好用

#### [LuoguP1439-最长公共子序列](https://www.luogu.com.cn/problem/P1439)

给定两个长度为n的数组, 求最长公共子序列(LCS)长度

> 用哈希表映射数组的下标, 将LCS问题转化成LIS

#### [Acwing272-最长公共递增子序列](https://www.acwing.com/problem/content/description/274/)

给定两个长度为n的数组, 求最长公共递增子序列(LCIS)长度

> 既要公共, 又要递增? 别被这么简单的描述骗了, 这题不简单

#### [LuoguP1020-导弹拦截 | NOIP 1999提高组](https://www.luogu.com.cn/problem/P1020)

给一个数组, 求他的**最长不升子序列**, 再求他最少能分解出几个不升子序列

> 1. 求最长不升子序列
> 2. 根据Dilworth定理, 分解出不升子序列的最小个数等于最长上升子序列的长度
>
> 这个Dilworth定理也太搞人心态了, 我不知道如果不知道这个定理怎么做这题, 能自己推出这种逆天结论

#### [Acwing187-导弹拦截系统](https://www.acwing.com/problem/content/189/)

> 参见 搜索-Acwing187-导弹拦截系统

### 字符串编辑DP

字符串DP有自己的套路: 增删改, 编辑距离; 一般两个字符串, 二维一拼, 推转移方程, ij开滚

如果是纯板子, 可以用滚动数组优化

#### [Acwing902-最短编辑距离](https://www.acwing.com/problem/content/904/)

> 纯板子题, 两个注意的点
>
> 1. dp\[i][j]表示的是s1\[:i]和s2\[:j]的最短编辑距离, 即, 不包含s1\[i], s2\[j]
>     - 这是因为我们要考虑空字符串的情况, dp\[0][j]=j, 代表i是空字符串
>     - 更新dp\[i][j]的时候, 看的是s1[i-1], s2[j-1]
> 2. 状态转移方程的增加和删除具有对称性, 为什么?
>     - s1删除一个字符变成s2, 和s2添加一个字符是等价的
>     - 可以证明, 如果增加和删除的开销不同, 则大开销的操作永远不会使用

#### [Acwing899-编辑距离](https://www.acwing.com/problem/content/904/)

#### [Leetcode1143-最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/description/)

虽然叫子序列, 但其实和字符串编辑有关

给你两个字符串s1, s2, 问最长公共子序列长度, 可以跳, 比如abcd, abeced=len(abcd)=4

> 参考板子题推状态转移方程

### 走格子模型

给一个二维棋盘, 每个位置有一个价值, 一般是左上角走到右下角, 取走路径上的元素价值, 状态转移就是上面和左面

如果允许走回头路, 则不适用dp

#### [Acwing1017-摘花生](https://www.acwing.com/problem/content/1017/)

纯板子题

#### [Acwing898-数字三角形](https://www.acwing.com/problem/content/900/)

一个数字三角形, 一个位置可以往下走或者往右下走

问从最上面走到最下面的最大收益是多少

> 除了起点, 其他的点不能初始化为本点的价值, 他的价值只能来自转移

#### [Acwing1018-最低通行费](https://www.acwing.com/problem/content/1020/)

题目虽然可以上下左右走, 但是分析得到只能往下和往右走. 

> 同样的, 除了起点, 一个点的状态只能通过转移得到, 不能想当然的初始化
> 这样理解: 某点的价值不能白拿, 他必须付出来的代价(上面和左面的状态转移)

#### [LuoguP1002-过河卒 | NOIP 2002普及组T4](https://www.luogu.com.cn/problem/P1002)

一个棋盘格, 一个卒要从左上角走到右下角, 其中有一些点不能走

> 板子+不能走的点方案数=0, 除了马踩的地方不能走, 马本身的位置也不能走

#### [LuoguP1004-方格取数 | NOIP 2000提高组T4](https://www.luogu.com.cn/problem/P1004)

继续给一个棋盘格, 继续要从左上走到右下, 继续只能往右和往下

不同的是, 这次可以**走两次**, 求能拿到的最大价值

> 贪心做两次是错误的, 为什么?
>
> 第一次取数的结果会影响到第二次决策:
> 设想这样的情况, 如果第一次跑的时候最优路径有多条, 贪心并不会处理, 这些不同的路径就会影响到第二次的决策

#### [LuoguP1006-传纸条 | NOIP 2008提高组T3](https://www.luogu.com.cn/problem/P1006)

给一个数字矩阵, 每个位置代表一个同学的价值, 同学A在左上角, B在右下角, 他们两个要传纸条

- A给B的纸条只能往右, 往下传
- B给A的纸条走能往左, 往上传
- 一个位置的同学**最多帮一次忙**, 这意味着A和B的纸条路径不能交叉
- 求传一次纸条(两条不交叉路径)的最大价值

> 和方格取数异曲同工, 以下是思维链: 
>
> 1. **A给B, B给A是等价的**, 即传纸条没有方向性, 所以我们分析A给B传两次纸条, 路径不重叠即可
> 2. **路径不重叠意味着一定有一高一低两条路径**, 我们枚举低路径, 高路径只可能在他的上面范围
> 3. **因为路径不重合, 终点是不可达的**, 我们的答案是终点的上侧和左侧代价和

### 背包DP

背包DP关注在一定限制内取物品的问题

一般来说可以抽象为, 给定背包容量V和一些物品, 每个物品有收益和代价(占用空间), 求最大收益

总体来说, 背包DP都关注"拿与不拿"的问题

#### [Acwing2-01背包问题](https://www.acwing.com/problem/content/2/)

你有$N$ 个物品和一个容量为$V$ 的背包, 每个物品都有空间代价$c_i$ 和收益$w_i$ , 

求在最大容量限制下的最大收益

> 先写二维, 再写一维

#### [Acwing3-完全背包问题](https://www.acwing.com/problem/content/3/)

你有$N$ 种物品和一个容量为$V$ 的背包, 每个物品都有空间代价$c_i$ 和收益$w_i$ , 并且每种物品都有无限件可用

求在最大容量限制下的最大收益

> 先写朴素的枚举拿几个的
>
> 再写正序O(VN)的
>
> 注意完全背包问题的两层循环可以互换, 这有助于我们用走楼梯模型理解他

#### [Acwing5-多重背包问题-II](https://www.acwing.com/problem/content/5/)

你有$N$ 种物品和一个容量为$V$ 的背包, 每个物品都有空间代价$c_i$ 和收益$w_i$ , 每种物品都有$m_i$件可用

求在最大容量限制下的最大收益

> 当然可以用k枚举拿几个
>
> 更好的方法是用二进制拆分每种物品, 分离出1, 2, 4, 8, ...然后用0-1背包处理

#### [Acwing9-分组背包问题](https://www.acwing.com/problem/content/9/)

你有$N$ 组物品和一个容量为$V$ 的背包, 每组物品有$m_i$件物品每件物品都有空间代价$c_i$ 和收益$w_i$ , 每组物品最多选一种

求在最大容量限制下的最大收益

> 枚举顺序是: 分组-容量-组内物品
>
> 先枚举容量, 再枚举物品, 才可以保证物品只能拿一件

#### 关于初始化的细节

有的题会要求背包必须装满, 有的不要求装满, 这个差异可以在初始化实现

- 如果不要求装满, 则dp初始化为全0, **代表所有状态下, 什么都不选也不失为一种合法方案**
- 如果要求装满, dp[0] = 0, 其他初始化为-inf
    - 先理解其他情况, 因为不能不选, 所以是未定义状态
    - dp[0] = 0 很有趣, 可以理解为: **只有容量为0的情况下可以什么都不选还恰好装满**

### 区间DP

#### [Acwing282-石子合并](https://www.acwing.com/problem/content/description/284/)

和哈夫曼那道石子合并非常像, 同样给了一排石子, 每堆有一个重量, 每次需要选两堆合并, 代价是重量和

新条件: 每次只能选择相邻的两堆, 显然, 合并完了之后, 会产生新的相邻关系

问合并的最小代价

> 标准做法: 枚举区间长度, 枚举起点, 确定重点, 枚举划分点,  用前缀和更新

#### [LuoguP1880-石子合并 | NOI 1995](https://www.luogu.com.cn/problem/P1880)

和上面一摸一样, 但是换成了环形

我在做上一道的时候就想到了这题可以改环形, 然后就看到这道

> 虽然环形做法老生常谈, 但是还是需要注意起点的范围: 起点可以>=n
>
> 为什么不造成重复? 答: 虽然环形数组的两部分数值相同, 但是dp的两部分并不相同: dp依赖于具体的合并顺序

#### [LuoguP1063-能量项链 | NOIP 2006 提高组T1](https://www.luogu.com.cn/problem/P1063)

一个环形的项链, 每个珠子写着两个数字, 首尾相连, 相连处数字一样

你可以合并两个珠子, 得到的收益是三个数字的乘积, 问合并到**0个**珠子的最大收益是多少

> 在上一题的基础上, 修改了收益方程
>
> 除了需要注意k的范围, 还需要观察样例, 注意最后一次合并

## 记忆化搜索

记忆化搜索和动态规划一直坐一桌吃饭的

#### [LuoguP1005-矩阵取数游戏 | NOIP 2007 提高组T3](https://www.luogu.com.cn/problem/P1005)

给一个矩阵, 每次操作你需要从每一行的行首或者行尾取一个数, 第i次操作的收益是$2^i \times (num_1 + nums_2 + ...)$ 

问把矩阵取完的最大收益是多少

> 这道题题解全是区间dp, 我却觉得记忆化搜索的思路简单太多太多
>
> 用dfs(lo, hi)表示闭区间lo-hi的收益, 则如果lo==hi, 可以返回收益, 否则是区间, 返回两种取法的最大值

#### [Leetcode2140-解决智力问题](https://leetcode.cn/problems/solving-questions-with-brainpower/description/)

有一个有序二元组, 每个元素是(收益, 代价), 代价cost是你不能选择接下来的cost个元素

问你最大收益多少

> 打家劫舍题, 在位置p可以选或不选 
>
> dfs(p) -> int: return max(选+收益+代价, 不选)
>
> 答案就是dfs(0)
>
> 当然也可以线性DP

## 并查集

### 带权并查集

#### [LuoguP2024-食物链 | NOI 2001](https://www.luogu.com.cn/problem/P2024)

有一个生态圈, 内有三种动物, 他们的食物链呈环形: A吃B, B吃C, C吃A

现在给出K条断言, 每条断言的形如"X 吃 Y"或者 "X和Y是同类"

如果断言和已有真话的不冲突, 他就是真的, 否则是假的, 求这K条断言里面有多少假话

>  非常经典的带权并查集! 按照次序考虑以下的问题:
>
> 1. 如何写find函数的路径压缩?
> 2. 如何写union函数?
> 3. 如何判断在同一个集合的两个动物关系?
>
> 上面的问题, 不要画图画的满纸都是, 请用向量的角度思考(并查集的边是有向的)

## 数学相关

### 找规律

蓝桥杯真的很喜欢考找规律, 基本上在第四题这个位置



## 树形数据结构

### 哈夫曼树

哈夫曼树对**种类+计数**, **合并**, **操作两个对象代价是加和**, 这样的字眼很敏感

#### [LuoguP1090-合并果子 | NOIP 2004提高组](https://www.luogu.com.cn/problem/P1090)

地上有n堆果子, 每堆果子有重量, 每次你可以合并两堆果子, 代价是两堆果子的重量和

显然经过n-1次合并就能得到一整堆果子, 你需要计算最小代价

> 从贪心的角度想, 越早搬的果子搬的次数就越多
>
> 当然, 直接从哈夫曼树的角度想直接就有了
>
> 如何构造哈夫曼树? 弄一个小根堆, 每次取出两个合并, 再塞进去



## 拓扑排序

#### [Leetcode2360-图中的最长环](https://leetcode.cn/problems/longest-cycle-in-a-graph/description/)

给了一个图, **每个点最多只有一个出度**, 求最长环长度

> 分析条件, 每个点最多只能在一个环上
>
> 这样的图叫做基环树, 有基环树的做法
>
> 也可以用拓扑排序

## 最近公共祖先

### 二叉树的LCA

#### [Leetcode236-二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/)

给你一个二叉树和两个节点p, q, 求他们两个的LCA

> 假设我们站在树上的一个节点
>
> - 如果当前节点的左子树和右子树分别找到了p, q, 则当前节点是LCA
> - 如果左子树找到了p, q, 则LCA在左子树
> - 如果右子树找到了p, q, 则LCA在右子树

#### [Leetcode1123-最深叶节点的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/description/)

给你一个二叉树, 求最深叶节点的LCA, 如果只有一个, 就是他自己, 如果有多个, 则是他们共同的

> 如果一个节点的左子树最大深度(全局深度) == 右子树最大深度 == 全局最大深度, 则它是答案候选
>
> 在dfs加深的时候, 维护每个节点的深度和全局最大深度
>
> 在dfs回溯的时候, 维护每个节点的左右子树最大深度, 并更新答案

### 多叉树的LCA

## 综合题

#### [Acwing5722-十滴水 | 第33次CSP T4](https://www.acwing.com/problem/content/5725/)

`链表`, `离散化`, `排序`, `DFS`

> 不标记死亡节点的话, DFS会重复处理哦


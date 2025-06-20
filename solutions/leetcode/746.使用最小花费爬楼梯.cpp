/*
 * @lc app=leetcode.cn id=746 lang=cpp
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])
        int n = cost.size();
        vector<int> f(3, 0);
        for (int i = 2; i <= n; i++)
            f[i % 3] = min(f[(i + 1) % 3] + cost[i - 2], f[(i + 2) % 3] + cost[i - 1]);
        return f[n % 3];
    }
};
// @lc code=end


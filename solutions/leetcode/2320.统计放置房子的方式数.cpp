/*
 * @lc app=leetcode.cn id=2320 lang=cpp
 *
 * [2320] 统计放置房子的方式数
 */

// @lc code=start
class Solution {
public:
    int countHousePlacements(int n) {
        vector<int> f(n + 2);
        const int MOD = 1e9 + 7;
        f[0] = 1;
        f[1] = 2;
        for (int i = 2; i <= n; i++) {
            f[i] = f[i - 1] + f[i - 2];
            f[i] %= MOD;
        }
        return (long long)f[n] * f[n] % MOD;
    }
};
// @lc code=end


/*
 * @lc app=leetcode.cn id=2466 lang=cpp
 *
 * [2466] 统计构造好字符串的方案数
 */

// @lc code=start
/*
用f[i]表示构造长度为i的字符串的方案数
f[i] = f[i - zero] + f[i - one]
*/
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<int> f(high + 1);
        const int MOD = 1e9 + 7;
        f[0] = 1;
        int ans = 0;
        for (int i = 1; i <= high; i++) {
            if (i >= zero)
                f[i] += f[i - zero];
            if (i >= one)
                f[i] += f[i - one];
            f[i] %= MOD;
            if (i >= low) {
                 ans += f[i];
                 ans %= MOD;
            }
        }
        return ans;
    }
};
// @lc code=end


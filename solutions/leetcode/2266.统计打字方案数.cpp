/*
 * @lc app=leetcode.cn id=2266 lang=cpp
 *
 * [2266] 统计打字方案数
 */

// @lc code=start
class Solution {
public:
    static const int MOD = 1e9 + 7;
    int count(string& s) {
        char c = s[0];
        int k = (c == '7' || c == '9') ? 4 : 3;
        int n = s.size();
        vector<int> f(n + 1, 0);
        f[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                if (i - j >= 0) {
                    f[i] += f[i - j];
                    f[i] %= MOD;
                } 
            }
        }
        return f[n] % MOD;
    }
    int countTexts(string pressedKeys) {
        int n = pressedKeys.size();
        long long ans = 1;

        for (int i = 0; i < n; i++) {
            int j = i + 1;
            for (; j < n && pressedKeys[j] == pressedKeys[i]; j++);
            string sub = pressedKeys.substr(i, j - i);
            ans *= count(sub);
            ans %= MOD;
            i = j - 1;
        }
        return ans % MOD;
    }
};
// @lc code=end


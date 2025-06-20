/*
 * @lc app=leetcode.cn id=377 lang=cpp
 *
 * [377] 组合总和 Ⅳ
 */

// @lc code=start
/*
用f[i]表示构成数字i的方案数
如果i属于nums，初始值为1，否则为0
f[i] += f[i - num]
*/
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<long long> f(target + 1, 0);
        sort(nums.begin(), nums.end());
        const long long MOD = INT_MAX + 1;
        for (int i = 1; i <= target; i++) {
            for (auto& num : nums) {
                if (num == i) {
                    f[i]++;
                    f[i] %= MOD;
                }
                if (i > num) {
                    f[i] += f[i - num];
                    f[i] %= MOD;
                }
                else
                    break;
            }
        }
        // for (auto & num : f)
        //     cout << num << ' ';
        return f[target];
    }
};
// @lc code=end


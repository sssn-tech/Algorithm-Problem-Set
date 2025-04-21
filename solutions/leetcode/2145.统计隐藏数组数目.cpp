/*
 * @lc app=leetcode.cn id=2145 lang=cpp
 *
 * [2145] 统计隐藏数组数目
 */

// @lc code=start
class Solution {
    public:
        int numberOfArrays(vector<int>& differences, int lower, int upper) {
            // 假设nums的第一个数是0, 算出nums的max和min, 再算出极差range
            // ans = max(0, upper - lower - range + 1)
            // const int INF = (1 << 30);
            long long curr = 0, max_in_nums = 0, min_in_nums = 0;
            for (const auto& diff : differences) {
                curr += diff;
                max_in_nums = max(curr, max_in_nums);
                min_in_nums = min(curr, min_in_nums);
            }
            return (int)max((long long)0, (long long)upper - lower - max_in_nums + min_in_nums + 1);
        }
    };
// @lc code=end


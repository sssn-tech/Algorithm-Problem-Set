/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */

// @lc code=start
class Solution {
    public:
        static bool comp(vector<int>& intA, vector<int>& intB) {
            return intA[0] < intB[0];
        }
        vector<vector<int>> merge(vector<vector<int>>& intervals) {
            sort(intervals.begin(), intervals.end(), comp);
            vector<vector<int>> ans;
            int l = intervals[0][0], r = intervals[0][1];
            for (auto& interval : intervals) {
                if (interval[0] > r) {
                    ans.push_back({l, r});
                    l = interval[0];
                    r = interval[1];
                } else {
                    r = max(r, interval[1]);
                }
            }
            ans.push_back({l, r});
            return ans;
        }
    };
// @lc code=end


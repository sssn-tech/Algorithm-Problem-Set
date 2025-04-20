/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
 */

// @lc code=start
class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_set<int> st; 
            for (const auto& num: nums) 
                st.insert(num);
            
            int ans = 0;
            for (const auto& x: st) {
                if (st.find(x - 1) != st.end()) 
                    continue;
                int l = 1;
                for (; l <= 1e5 && st.find(x + l) != st.end(); l++);
                ans = max(ans, l);
            }
            return ans;
        }
    };
// @lc code=end


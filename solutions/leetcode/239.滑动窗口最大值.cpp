/*
 * @lc app=leetcode.cn id=239 lang=cpp
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class Solution {
    public:
        vector<int> maxSlidingWindow(vector<int>& nums, int k) {
            if (nums.empty() || k == 0) 
                return {};
            int n = nums.size();
            vector<int> ans;
            deque<int> dq;
            for (int lo = 1 - k, hi = 0; hi < n; lo++, hi++) {
                if (lo > 0 && dq.front() == nums[lo - 1]) 
                    dq.pop_front();
                while (!dq.empty() && dq.back() < nums[hi])
                    dq.pop_back();
                dq.push_back(nums[hi]);
                if (lo >= 0)
                    ans.push_back(dq.front());
            }
            return ans;
        }
    };
// @lc code=end


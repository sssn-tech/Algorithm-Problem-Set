/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> num2pos;
            for(int i = 0; i < nums.size(); i++) {
                int num = nums[i];
                if (num2pos.find(target - num) != num2pos.end()) {
                    return vector<int>({num2pos[target - num], i});
                }
                num2pos[num] = i;
            }
            return vector<int>({-1, -1});
        }
    };
// @lc code=end


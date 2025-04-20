/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            map<vector<int>, vector<string>> hash_table;
            for (string s: strs) {
                vector<int> char_counter(26, 0);
                for (char c: s) {
                    char_counter[c - 'a']++;
                }
                hash_table[char_counter].push_back(s); 
            }
            vector<vector<string>> ans;
            for (auto pii: hash_table) {
                ans.push_back(pii.second);
            }
            return ans;
        }
    };
// @lc code=end


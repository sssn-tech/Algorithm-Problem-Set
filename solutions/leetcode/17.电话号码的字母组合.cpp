/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
class Solution {
public:
    void dfs(int p, string& digits, string& path, vector<string>& ans, unordered_map<int, string>& button) {
        // 现在要枚举digits[p]
        if (p >= digits.size()) {
            if (path.size() > 0)
                ans.push_back(path);
            return ;
        }
            
        int curr = digits[p] - '0';
        string s = button[curr];
        for (int i = 0; i < s.size(); i++) {
            path = path + s[i];
            dfs(p + 1, digits, path, ans, button);
            path = path.substr(0, path.size() - 1);
        }
    }
    vector<string> letterCombinations(string digits) {
        unordered_map<int, string> button = {
            {2, "abc"}, {3, "def"}, {4, "ghi"}, {5, "jkl"}, {6, "mno"}, {7, "pqrs"}, {8, "tuv"}, {9, "wxyz"}
        };
        string path;
        vector<string> ans;
        dfs(0, digits, path, ans, button);
        return ans;
    }
};
// @lc code=end


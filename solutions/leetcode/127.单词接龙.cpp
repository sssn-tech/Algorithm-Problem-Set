/*
 * @lc app=leetcode.cn id=127 lang=cpp
 *
 * [127] 单词接龙
 */

// @lc code=start
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord) && beginWord != endWord)
            return 0;
        unordered_set<string> q1{beginWord}, q2{endWord}, vis{beginWord};
        int ans = 0;
        while (!q1.empty() && !q2.empty()) {
            if (q1.size() > q2.size()) // 总是扩展小集合
                swap(q1, q2);
            unordered_set<string> ne;
            ans++;
            for (auto& ss : q1) {
                string s = ss;
                for (int i = 0; i < s.size(); i++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        char temp = s[i];
                        s[i] = c; // 为什么不能直接修改
                        if (dict.count(s)) {
                            if (q2.count(s)) 
                                return ans + 1;
                            if (!vis.count(s)) {
                                vis.insert(s);
                                ne.insert(s);
                            }
                        }
                        s[i] = temp;
                    }
                }
            }
            q1 = ne;
        }
        return 0;
    }
    
};
// @lc code=end


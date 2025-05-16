/*
 * @lc app=leetcode.cn id=838 lang=cpp
 *
 * [838] 推多米诺
 */

// @lc code=start
class Solution {
    public:
        string pushDominoes(string dominoes) {
            dominoes = "L" + dominoes + "R";
            int n = dominoes.size(), pre = 0;
            for (int i = 1; i < n; i++) {
                if (dominoes[i] == 'L') {
                    if (dominoes[pre] == 'L') {
                        for (int j = pre + 1; j < i; j++)
                            dominoes[j] = 'L';
                    } else { // pre是R
                        for (int l = 1; l <= (i - pre) / 2; l++) {
                            if (pre + l != i - l) {
                                dominoes[pre + l] = 'R';
                                dominoes[i - l] = 'L';
                            } 
                        }
                    }
                    pre = i;
                }
                if (dominoes[i] == 'R') { 
                    if (dominoes[pre] == 'R') {
                        for (int j = pre + 1; j < i; j++)
                            dominoes[j] = 'R';
                    }
                    pre = i;
                }
            }
            return dominoes.substr(1, n - 2);
        }
    };
// @lc code=end


/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class Solution {
    public:
        bool contained(int* s_cnt, int* t_cnt) {
            for (int i = 'a'; i <= 'z'; i++) 
                if (s_cnt[i] < t_cnt[i])
                    return false;
            for (int i = 'A'; i <= 'Z'; i++) 
                if (s_cnt[i] < t_cnt[i])
                    return false;
            return true;
        }
        string minWindow(string s, string t) {
            int s_cnt[128] = {0}, t_cnt[128] = {0}, 
                s_len = s.size(), t_len = t.size();
            for (const auto& ch: t)
                t_cnt[ch]++;
            int lo = 0, hi = 0;
            int ans_lo = -1, ans_hi = -1;
            while (hi < s_len) {
                // cout << lo << ' ' << hi << endl;
                while (hi < s_len && !contained(s_cnt, t_cnt)) {
                    s_cnt[s[hi]]++;
                    hi++;
                }
                while (lo < hi && contained(s_cnt, t_cnt)) {
                    if (ans_lo == -1 || hi - lo < ans_hi - ans_lo) {
                        ans_lo = lo;
                        ans_hi = hi;
                    }
                    s_cnt[s[lo]]--;
                    lo++;
                }
            }
            return ans_lo == -1 ? "" : s.substr(ans_lo, ans_hi - ans_lo);
        }
    };
// @lc code=end


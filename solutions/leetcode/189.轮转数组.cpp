/*
 * @lc app=leetcode.cn id=189 lang=cpp
 *
 * [189] 轮转数组
 */

// @lc code=start

class Solution {
    public:
        void rotate(vector<int>& nums, int k) {
            int n = nums.size();
            k %= n;
            if (n == 0 || k == 0) return ;
    
            int round = gcd(n, k);
            for (int i = 0; i < round; i++) {
                int cast = nums[0 + i], ne = k + i; // 现在要把数字cast覆盖到ne位置上
                do{
                    ne %= n;
                    int t = nums[ne];
                    nums[ne] = cast;
                    cast = t;
                    ne += k; ne %= n;
                } while (ne != k + i); 
            }
        }
    };
// @lc code=end


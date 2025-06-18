/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size())
            swap(nums1, nums2);
        int n = nums1.size(), m = nums2.size();
        const int INF = (1 << 30);
        nums1.insert(nums1.begin(), -INF);
        nums2.insert(nums2.begin(), -INF);
        nums1.insert(nums1.end(), INF);
        nums2.insert(nums2.end(), INF);

        int i = 0, j = (n + m + 1) / 2;
        while (true) {
            int max1 = max(nums1[i], nums2[j]);
            int min2 = min(nums1[i+1], nums2[j+1]);
            if (max1 <= min2) {
                return (m + n) % 2 ? max1 : (max1 + min2) / 2.0;
            }
            i++;
            j--;
        }
    }
};
// @lc code=end


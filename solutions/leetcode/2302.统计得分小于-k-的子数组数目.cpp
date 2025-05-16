class Solution {
    public:
        long long countSubarrays(vector<int>& nums, long long k) {
            vector<long long> prefix_sums = {0};
            for (const auto& num : nums) {
                long long last = prefix_sums[prefix_sums.size() - 1];
                prefix_sums.push_back(last + num);
            }
            
            long long ans = 0;
            for (int i = 0; i < nums.size(); i++) {
                int num = nums[i];
                int l = i, r = nums.size() - 1;
                while (l < r) {
                    int mid = (l + r + 1) >> 1;
                    if ((mid - i + 1) * (prefix_sums[mid + 1] - prefix_sums[i]) >= k)
                        r = mid - 1;
                    else
                        l = mid;
                }
                if (l > i)
                    ans += l - i + 1;
                else
                    ans += num >= k ? 0 : 1;
            }
            return ans;
        }
    };
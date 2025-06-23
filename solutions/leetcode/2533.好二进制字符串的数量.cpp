class Solution {
public:
    int goodBinaryStrings(int minLength, int maxLength, int oneGroup, int zeroGroup) {
        vector<int> f(maxLength + 1, 0);
        f[0] = 1;
        const int MOD = 1e9 + 7;
        long long ans = 0;
        for (int i = 1; i <= maxLength; i++) {
            if (i >= oneGroup)
                f[i] += f[i - oneGroup];
            if (i >= zeroGroup)
                f[i] += f[i - zeroGroup];
            if (i >= minLength) {
                ans += f[i] % MOD;
                ans %= MOD;
            }
            f[i] %= MOD;
        }
        return ans;
    }
};
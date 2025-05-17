#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

pii partition(vector<int>& nums, int l, int r, int pivot) {
    // 荷兰国旗三分法
    int lo = l, curr = l, hi = r;
    while (curr <= hi) {
        if (nums[curr] < pivot)
            swap(nums[curr++], nums[lo++]);
        else if (nums[curr] > pivot)
            swap(nums[curr], nums[hi--]);
        else
            curr++;
    }
    return {lo, hi};
}

void q_sort(vector<int>& nums, int l, int r) {
    if (l >= r)
        return ;
    int mid = (l + r) >> 1;
    pii p = partition(nums, l, r, nums[mid]);
    int lo = p.first, hi = p.second;
    
    q_sort(nums, l, lo - 1);
    q_sort(nums, hi + 1, r);
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
        cin >> nums[i];
        
    q_sort(nums, 0, n - 1);
    
    for (const auto& num : nums)
        cout << num << ' ';
    return 0;
}
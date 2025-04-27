class Solution {
    public:
        
        bool is_palindrome(const string& s) {
            int n = s.size();
            for (int i = 0; i < n / 2; i++)
                if (s[i] != s[n - i - 1])
                    return false;
            return true;
        }
    
        void dfs(string s, int p, vector<string>& curr, vector<vector<string>>& ans) {
            int n = s.size();
            if (p >= n) {
                ans.push_back(curr);
                return ;
            }
            for (int l = 1; p + l <= n; l++) {      
                string ss = s.substr(p, l);
                if (is_palindrome(ss)) {
                    curr.push_back(ss);
                    dfs(s, p + ss.size(), curr, ans);
                    curr.pop_back();
                }
            }
        }
    
        vector<vector<string>> partition(string s) {
            vector<vector<string>> ans;
            vector<string> curr;
            dfs(s, 0, curr, ans);
            return ans;
        }
    };
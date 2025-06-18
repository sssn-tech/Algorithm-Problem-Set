/*
 * @lc app=leetcode.cn id=2359 lang=cpp
 *
 * [2359] 找到离给定两个节点最近的节点
 */

// @lc code=start
/*
分别从两个节点出发走到底, 得到有序数组path1和path2
找到num属于path1, 2, 令num的两个下标中更大的那个更小
*/
class Solution {
public:
    vector<int> dfs(vector<int>& edges, int start) {
        int n = edges.size();
        vector<bool> vis = vector<bool>(n, false);
        vector<int> res;
        while (start != -1 && !vis[start]) {
            res.push_back(start);
            vis[start] = true;
            start = edges[start];
        }
        return res;
    }
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        vector<int> path1 = dfs(edges, node1);
        vector<int> path2 = dfs(edges, node2);

        map<int, int> num2p;
        for (int i = 0; i < path2.size(); i++)
            num2p[path2[i]] = i; 

        const int INF = 1 << 30;
        int min_step = INF, ans = -1;
        for (int i = 0; i < path1.size(); i++) {
            int node = path1[i];
            auto it = num2p.find(node);
            if (it != num2p.end() && min_step >= max(i, num2p[node])) {
                if (min_step == max(i, num2p[node]))
                    ans = min(ans, node);
                else 
                    ans = node;
                min_step = max(i, num2p[node]);
            }
        }

        return ans;
    }
};
// @lc code=end


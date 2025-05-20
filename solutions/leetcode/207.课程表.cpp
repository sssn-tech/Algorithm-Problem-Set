/*
 * @lc app=leetcode.cn id=207 lang=cpp
 *
 * [207] 课程表
 */

// @lc code=start
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> ind(numCourses);
        for (auto &e : prerequisites) {
            int x = e[0], y = e[1];
            g[x].push_back(y);
            ind[y]++;
        }
        queue<int> q;
        for (int i = 0; i < numCourses; i++)
            if (!ind[i])
                q.push(i);
        int finish = 0;
        while (!q.empty()) {
            int x = q.front();
            finish++;
            q.pop();
            for (auto &y : g[x]) {
                ind[y]--;
                if (!ind[y])
                    q.push(y);
            }
        }
        return finish == numCourses;
    }
};
// @lc code=end


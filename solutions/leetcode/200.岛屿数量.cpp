/*
 * @lc app=leetcode.cn id=200 lang=cpp
 *
 * [200] 岛屿数量
 */

// @lc code=start
class Solution {
public:
    void floodFill(vector<vector<char>>& grid, int x, int y) {
        typedef pair<int, int> pii;
        queue<pii> q;
        q.push({x, y});
        int n = grid.size(), m = grid[0].size();
        int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
        while (!q.empty()) {
            pii front = q.front();
            q.pop();
            int x = front.first, y = front.second;
            grid[x][y] = '0';
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == '1') {
                    grid[nx][ny] = '0'; // mark
                    q.push({nx, ny});
                }
                    
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    ans++;
                    floodFill(grid, i, j);
                }
            }
        }
        return ans;
    }
};
// @lc code=end


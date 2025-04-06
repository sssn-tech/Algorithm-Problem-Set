# include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

const int N = 5e4 + 10;

int fa[N], wt[N]; //wt[i]是i节点和祖宗的关系, 0是同类, 1是吃祖先, 2是被祖先吃

pii find(int u) {
    // 返回u的祖先与到祖先的距离
    if (fa[u] == u) 
        return make_pair(fa[u], wt[fa[u]]);
    pii p = find(fa[u]);
    fa[u] = p.first;
    wt[u] = (p.second + wt[u]) % 3;
    return make_pair(fa[u], wt[u]);
}

void unite(int u, int v, int relation) {
    // 保证u, v不在一个集合, 已知relation, 合并集合
    pii pu = find(u), pv = find(v);
    int fu = pu.first, du = pu.second, fv = pv.first, dv = pv.second;
    if (fu != fv) {
        fa[fu] = fv;
        wt[fu] = (relation + dv - du + 3) % 3;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++)
        fa[i] = i;

    int ans = 0;
    while (m--) {
        int statement, u, v;
        cin >> statement >> u >> v;
        if (u <= 0 || v <= 0 || u > n || v > n) {
            ans++;
            continue;
        }
        statement--;
        pii pu = find(u), pv = find(v);
        int fu = pu.first, du = pu.second, fv = pv.first, dv = pv.second;
        if (fu != fv) {
            unite(u, v, statement);
        } else {
            int relation = (du - dv + 3) % 3;
            if (relation != statement)
                ans++;
        }
    }
    cout << ans << endl;

    return 0;
}
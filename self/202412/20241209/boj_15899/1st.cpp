#include <iostream>
#include <vector>
#include <algorithm>
#define MOD 1000000007
using namespace std;

const int MAXN = 200001;

int N, M, C;
vector<int> arr(MAXN), A(MAXN), E(MAXN), T(MAXN);
vector<vector<int>> tree(4 * MAXN), G(MAXN);
int cnt = 0;

void dfs(int n, int parent) {
    A[n] = ++cnt;
    T[cnt] = n;
    for (int x : G[n]) {
        if (x != parent && A[x] == 0) {
            dfs(x, n);
        }
    }
    E[n] = cnt;
}

vector<int> merge(const vector<int>& X, const vector<int>& Y) {
    vector<int> res;
    int i = 0, j = 0, x = X.size(), y = Y.size();

    while (i < x && j < y) {
        if (X[i] >= Y[j]) {
            res.push_back(Y[j++]);
        } else {
            res.push_back(X[i++]);
        }
    }
    while (i < x) res.push_back(X[i++]);
    while (j < y) res.push_back(Y[j++]);

    return res;
}

vector<int> buildTree(int s, int e, int idx) {
    if (s == e) {
        tree[idx] = {arr[T[s]]};
        return tree[idx];
    }

    int mid = (s + e) / 2;
    tree[idx] = merge(buildTree(s, mid, idx * 2), buildTree(mid + 1, e, idx * 2 + 1));
    return tree[idx];
}

int countLessEqual(const vector<int>& X, int c) {
    int s = 0, e = X.size() - 1;

    while (s <= e) {
        int mid = (s + e) / 2;

        if (X[mid] > c) {
            e = mid - 1;
        } else {
            s = mid + 1;
        }
    }
    return e + 1;
}

int query(int s, int e, int idx, int l, int r, int c) {
    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return countLessEqual(tree[idx], c) % MOD;
    }

    int mid = (s + e) / 2;
    return (query(s, mid, idx * 2, l, r, c) + query(mid + 1, e, idx * 2 + 1, l, r, c)) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> C;
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    dfs(1, -1);
    buildTree(1, N, 1);

    long long ans = 0;
    for (int i = 0; i < M; i++) {
        int v, c;
        cin >> v >> c;
        ans = (ans + query(1, N, 1, A[v], E[v], c)) % MOD;
    }

    cout << ans << '\n';
    return 0;
}

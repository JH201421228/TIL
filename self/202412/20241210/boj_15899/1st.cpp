#include <iostream>
#include <vector>
using namespace std;


int N, M, C;
int T[200001];
int A[200001];
int E[200001];
vector<int> G[200001];
int arr[200001];
int cnt = 0;
long long MOD = 1000000007;
vector<int> tree[800001];

void dfs(int n) {
    A[n] = ++cnt;
    T[cnt] = n;

    for (auto& x : G[n]) {
        if (A[x] == 0) {
            dfs(x);
        }
    }

    E[n] = cnt;
}

vector<int> merge(const vector<int>& X, const vector<int>& Y) {
    vector<int> res;
    int i = 0, j = 0, x = X.size(), y = Y.size();

    while (i < x && j < y) {
        if (X[i] >= Y[j]) {
            res.emplace_back(Y[j++]);
        }
        else {
            res.emplace_back(X[i++]);
        }
    }

    while (i < x) res.emplace_back(X[i++]);
    while (j < y) res.emplace_back(Y[j++]);

    return res;
}

vector<int> I(int s, int e, int idx) {
    if (s == e) {
        tree[idx] = {arr[T[s]]};
        return tree[idx];
    }

    int mid = (s+e) >> 1;

    tree[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1));
    return tree[idx];
}

int count(const vector<int>& X, int c) {
    int s = 0, e = X.size()-1;

    while (s <= e) {
        int mid = (s+e) >> 1;

        if (X[mid] > c) {
            e = mid-1;
        }
        else {
            s = mid+1;
        }
    }

    return s;
}

int S(int s, int e, int idx, int l, int r, int c) {
    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return count(tree[idx], c);
    }

    int mid = (s+e) >> 1;

    return (S(s, mid, idx<<1, l, r, c) + S(mid+1, e, idx<<1|1, l, r, c));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> C;

    for (int i = 1; i < N+1; ++i) {
        cin >> arr[i];
    }

    for (int i = 0; i < N-1; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
        G[v].emplace_back(u);
    }

    dfs(1);

    I(1, N, 1);

    long long ans = 0;

    for (int i = 0; i < M; ++i) {
        int v, c; cin >> v >> c;
        ans += S(1, N, 1, A[v], E[v], c);
        ans %= MOD;
    }

    cout << ans << '\n';

    return 0;
}
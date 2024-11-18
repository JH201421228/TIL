#include<iostream>
#include<vector>
using namespace std;

int N, M;
vector<vector<int>> G;
int F[500001];
int cnt = 0;
int A[500001];
int E[500001];
int T[500001];
long long tree[2000001];
long long lazy[2000001];

void dfs(int n) {
    A[n] = ++cnt;
    T[cnt] = n;
    for (auto& x : G[n]) {
        dfs(x);
    }
    E[n] = cnt;
}

void I(int s, int e, int idx) {
    if (s == e) {
        tree[idx] = F[T[s]];
        return;
    }

    int mid = (s+e) >> 1;

    I(s, mid, idx*2);
    I(mid+1, e, idx*2+1);
}

void lazy_U(int s, int e, int idx) {
    if (lazy[idx]) {
        if (s == e) {
            tree[idx] += lazy[idx];
        }
        else {
            lazy[idx*2] += lazy[idx];
            lazy[idx*2+1] += lazy[idx];
        }
        lazy[idx] = 0;
    }
}

void U(int s, int e, int idx, int l, int r, int v) {
    lazy_U(s, e, idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        lazy[idx] += v;
        lazy_U(s, e, idx);
        return;
    }

    int mid = (s+e) >> 1;

    U(s, mid, idx*2, l, r, v);
    U(mid+1, e, idx*2+1, l, r, v);
}

long long S(int s, int e, int idx, int i) {
    lazy_U(s, e, idx);

    if (s > i || e < i) {
        return 0;
    }

    if (s == e) {
        return tree[idx];
    }

    int mid = (s+e) >> 1;

    return S(s, mid, idx*2, i) + S(mid+1, e, idx*2+1, i);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    G.resize(N+1);

    cin >> F[1];
    for (int i = 2; i < N+1; ++i) {
        cin >> F[i];
        int a; cin >> a;
        G[a].emplace_back(i);
    }

    dfs(1);

    I(1, N, 1);

    for (int i = 0; i < M; ++i) {
        char c; cin >> c;

        if (c == 'p') {
            int a, b; cin >> a >> b;
            U(1, N, 1, A[a], E[a], b);
            U(1, N, 1, A[a], A[a], -b);
        }
        else {
            int a; cin >> a;
            cout << S(1, N, 1, A[a]) << "\n";
        }
    }

    return 0;
}
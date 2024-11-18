#include <iostream>
#include <vector>
using namespace std;

int N, M, z;
int A[100001];
int E[100001];
vector<int> G[100001];
int cnt = 0;
int tree[400001];
int lazy[400001];

void dfs(int n) {
    A[n] = ++cnt;

    for (auto& x : G[n]) {
        dfs(x);
    }

    E[n] = cnt;
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
    tree[idx] = tree[idx*2] + tree[idx*2+1];
}

int S(int s, int e, int idx, int i) {
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

    cin >> N >> M >> z;

    for (int i = 2; i < N+1; ++i) {
        int a; cin >> a;
        G[a].emplace_back(i);
    }

    dfs(1);

    for (int i = 0; i < M; ++i) {
        int a; cin >> a;

        if (a == 1) {
            int b, c; cin >> b >> c;
            U(1, N, 1, A[b], E[b], c);
        }
        else {
            int b; cin >> b;
            cout << S(1, N, 1, A[b]) << "\n";
        }
    }

    return 0;
}
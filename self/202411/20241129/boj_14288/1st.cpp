#include <iostream>
#include <vector>
using namespace std;

int N, M, z;
vector<int> G[100001];
int A[100001];
int E[100001];
int cnt = 0;
int tree1[400001];
int tree2[400001];
int lazy1[400001];
int lazy2[400001];
bool is_down_direction = true;

void dfs(int n) {
    A[n] = ++cnt;
    for (auto& x : G[n]) {
        dfs(x);
    }
    E[n] = cnt;
}

void lazy_U(int s, int e, int idx, int tree[], int lazy[]) {
    if (lazy[idx] != 0) {
        tree[idx] += (e-s+1) * lazy[idx];
        if (s != e) {
            lazy[idx*2] += lazy[idx];
            lazy[idx*2+1] += lazy[idx];
        }
        lazy[idx] = 0;
    }
}

void U(int s, int e, int idx, int l, int r, int v, int tree[], int lazy[]) {
    lazy_U(s, e, idx, tree, lazy);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        lazy[idx] += v;
        lazy_U(s, e, idx, tree, lazy);
        return;
    }

    int mid = (s+e) >> 1;
    U(s, mid, idx*2, l, r, v, tree, lazy);
    U(mid+1, e, idx*2+1, l, r, v, tree, lazy);
    tree[idx] = tree[idx*2] + tree[idx*2+1];
}

int S(int s, int e, int idx, int l, int r, int tree[], int lazy[]) {
    lazy_U(s, e, idx, tree, lazy);

    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[idx];
    }

    int mid = (s+e) >> 1;

    return S(s, mid, idx*2, l, r, tree, lazy) + S(mid+1, e, idx*2+1, l, r, tree, lazy);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> z;

    for (int i = 1; i < N; ++i) {
        int a; cin >> a;
        G[a].emplace_back(i+1);
    }

    dfs(1);

    for (int i = 0; i < M; ++i) {
        int a; cin >> a;

        if (a == 1) {
            int b, c; cin >> b >> c;

            if (is_down_direction) {
                U(1, N, 1, A[b], E[b], c, tree1, lazy1);
            }
            else {
                U(1, N, 1, A[b], A[b], c, tree2, lazy2);
            }
        }
        else if (a == 2) {
            int b; cin >> b;
            
            cout << S(1, N, 1, A[b], A[b], tree1, lazy1) + S(1, N, 1, A[b], E[b], tree2, lazy2) << '\n';
        }
        else {
            is_down_direction = !is_down_direction;
        }
    }

    return 0;
}
#include <iostream>
#include <vector>
#include <utility>
using namespace std;


vector<long long> arr;
vector<long long> tree;
vector<pair<long long, long long>> lazy;

long long MOD = 1000000007;

long long I(int s, int e, int tree_idx) {
    if (s == e) {
        tree[tree_idx] = arr[s];
        return arr[s];
    }

    int mid = (s + e) / 2;

    tree[tree_idx] = (I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)) % MOD;

    return tree[tree_idx];
}

void lazy_U(int s, int e, int tree_idx) {
    if (lazy[tree_idx].first != 1 || lazy[tree_idx].second != 0) {
        tree[tree_idx] = (tree[tree_idx] * lazy[tree_idx].first + (e-s+1) * lazy[tree_idx].second) % MOD;
        if (s != e) {
            lazy[tree_idx*2].first = (lazy[tree_idx*2].first * lazy[tree_idx].first) % MOD;
            lazy[tree_idx*2+1].first = (lazy[tree_idx*2+1].first * lazy[tree_idx].first) % MOD;
            lazy[tree_idx*2].second = (lazy[tree_idx*2].second * lazy[tree_idx].first + lazy[tree_idx].second) % MOD;
            lazy[tree_idx*2+1].second = (lazy[tree_idx*2+1].second * lazy[tree_idx].first + lazy[tree_idx].second) % MOD;
        }
        lazy[tree_idx].first = 1;
        lazy[tree_idx].second = 0;
    }
}

long long S(int s, int e, int tree_idx, int l, int r) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[tree_idx];
    }

    int mid = (s + e) / 2;

    return (S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r)) % MOD;
}

void U(int s, int e, int tree_idx, int l, int r, long long v1, long long v2) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        lazy[tree_idx].first = (lazy[tree_idx].first * v1) % MOD;
        lazy[tree_idx].second = (lazy[tree_idx].second * v1 + v2) % MOD;
        lazy_U(s, e, tree_idx);
        return;
    }

    int mid = (s + e) / 2;

    U(s, mid, tree_idx*2, l, r, v1, v2);
    U(mid+1, e, tree_idx*2+1, l, r, v1, v2);

    tree[tree_idx] = (tree[tree_idx*2] + tree[tree_idx*2+1]) % MOD;
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    arr.resize(N+1);
    tree.resize(4*N+1);
    lazy.resize(4*N+1, {1, 0});

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
    }

    I(1, N, 1);

    int M;
    cin >> M;

    for (int i = 0; i < M; ++i) {
        int a;
        cin >> a;

        if (a == 1) {
            int b, c;
            long long d;
            cin >> b >> c >> d;

            U(1, N, 1, b, c, 1, d);
        }
        else if (a == 2) {
            int b, c;
            long long d;
            cin >> b >> c >> d;

            U(1, N, 1, b, c, d, 0);
        }
        else if (a == 3) {
            int b, c;
            long long d;
            cin >> b >> c >> d;

            U(1, N, 1, b, c, 0, d);
        }
        else {
            int b, c;
            cin >> b >> c;

            cout << S(1, N, 1, b, c) <<'\n';
        }
    }

    return 0;
}
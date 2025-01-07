#include <iostream>
#include <vector>
using namespace std;

int M, V, arr[100001], T[400001], lazy[400001];
string S;

int I(int s, int e, int idx) {
    if (s == e) {
        T[idx] = arr[s];
        return T[idx];
    }

    int mid = (s+e) >> 1;

    T[idx] = min(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1));
    return T[idx];
}

void lazy_U(int s, int e, int idx) {
    if (lazy[idx]) {
        T[idx] += lazy[idx];
        if (s != e) {
            lazy[idx<<1] = lazy[idx];
            lazy[idx<<1|1] = lazy[idx];
        }
        lazy[idx] = 0;
    }
}

int U(int s, int e, int idx, int l, int r, int v) {
    lazy_U(s, e, idx);

    if (s > r || e < l) {
        return T[idx];
    }

    if (s >= l && e <= r) {
        lazy[idx] += v;
        lazy_U(s, e, idx);
        return T[idx];
    }

    int mid = (s+e) >> 1;

    U(s, mid, idx<<1, l, r, v);
    U(mid+1, e, idx<<1|1, l, r, v);

    return T[idx];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> S >> M;

    for (int i = 0; i < S.size(); ++i) {
        if (S[i] == '(') {
            arr[i+1] = arr[i] + 1;
        }
        else {
            arr[i+1] = arr[i] - 1;
        }
    }

    V = arr[S.size()-1];

    I(1, S.size(), 1);

    for (int i = 0; i < M; ++i) {
        int q; cin >> q;
    }

    return 0;
}
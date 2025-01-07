#include <iostream>
#include <vector>
using namespace std;

int N, M, V, ans, arr[100001], T[400001], lazy[400001];
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
            lazy[idx<<1] += lazy[idx];
            lazy[idx<<1|1] += lazy[idx];
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

    T[idx] = min(U(s, mid, idx<<1, l, r, v), U(mid+1, e, idx<<1|1, l, r, v));

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

    N = S.size();
    V = arr[N];

    I(1, N, 1);

    for (int i = 0; i < M; ++i) {
        int q, k; cin >> q;
        
        if (S[q-1] == '(') {
            S[q-1] = ')';
            V -= 2;
            k = U(1, N, 1, q, N, -2);
        }
        else {
            S[q-1] = '(';
            V += 2;
            k = U(1, N, 1, q, N, 2);
        }

        if (!V && k >= 0) {
            ans += 1;
        }
    }

    cout << ans << '\n';

    return 0;
}
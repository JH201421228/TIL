#include <iostream>
using namespace std;

int N, T[2000001 * 4 + 1];

int U(int s, int e, int idx, int v) {
    if (s == e && s == v) {
        T[idx]++;
        return T[idx];
    }

    if (s > v || e < v) {
        return T[idx];
    }

    int mid = (s+e) >> 1;

    T[idx] = U(s, mid, idx<<1, v) + U(mid+1, e, idx<<1|1, v);

    return T[idx];
}

int D(int s, int e, int idx, int v) {
    if (s == e) {
        T[idx]--;
        return s;
    }

    int mid = (s+e) >> 1;
    int res;

    if (T[idx<<1] >= v) {
        res = D(s, mid, idx<<1, v);
    }
    else {
        res = D(mid+1, e, idx<<1|1, v - T[idx<<1]);
    }

    T[idx]--;

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    
    for (int i = 0; i < N; ++i) {
        int t, x; cin >> t >> x;

        if (t == 1) {
            U(1, 2000000, 1, x);
        }
        else {
            cout << D(1, 2000000, 1, x) << '\n';
        }
    }

    return 0;
}
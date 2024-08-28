#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


vector<long long> arr;
vector<long long> lazy;

void U_lazy(int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        if (s == e) {
            arr[s] += lazy[tree_idx];
        }
        else {
            lazy[tree_idx*2] += lazy[tree_idx];
            lazy[tree_idx*2+1] += lazy[tree_idx];
        }
        lazy[tree_idx] = 0;
    }
}

long long S(int s, int e, int tree_idx, int arr_idx) {
    U_lazy(s, e, tree_idx);

    if (s == e) {
        if (s == arr_idx) {
            return arr[arr_idx];
        }
        else {
            return 0;
        }
    }

    if (s > arr_idx || e < arr_idx) {
        return 0;
    }

    int mid = (s+e) / 2;

    return S(s, mid, tree_idx*2, arr_idx) + S(mid+1, e, tree_idx*2+1, arr_idx);
}

void U(int s, int e, int tree_idx, int l, int r, long long val) {
    U_lazy(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        if (s == e) {
            arr[s] += val;  // 이 부분 누락되어 있었으니, 정신 멀쩡할 때 다시 확인하기
        }
        else {
            lazy[tree_idx*2] += val;
            lazy[tree_idx*2+1] += val;
        }
        return;
    }

    int mid = (s+e) / 2;

    U(s, mid, tree_idx*2, l, r, val);
    U(mid+1, e, tree_idx*2+1, l, r, val);
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    arr.resize(N+1);
    lazy.resize(4*N+1);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
    }

    int M;
    cin >> M;

    for (int i = 0; i < M; ++i) {
        int a;
        cin >> a;

        if (a == 1) {
            int b, c;
            long long d;
            cin >> b >> c >> d;

            U(1, N, 1, b, c, d);
        }
        else {
            int b;
            cin >> b;

            cout << S(1, N, 1, b) << "\n";
        }
    }

    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, T[500001];
vector<pair<int, int>> arr;

void U(int idx, int N) {
    while (idx < N+1) {
        ++T[idx];
        idx += (idx & -idx);
    }
}

int S(int idx) {
    int res = 0;
    while (idx > 0) {
        res += T[idx];
        idx -= (idx & -idx);
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; ++i) {
        int t; cin >> t;
        arr.emplace_back(t, i);
    }

    sort(arr.begin(), arr.end());
    for (int i = 0; i < N; ++i) {
        arr[i].first = i+1;
        swap(arr[i].first, arr[i].second);
    }

    sort(arr.begin(), arr.end());

    for (int i = 0; i < N; ++i) {
        cout << i+1 - S(arr[i].second) << '\n';
        U(arr[i].second, N);
    }

    return 0;
}
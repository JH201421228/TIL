#include <iostream>
#include <vector>
using namespace std;

int N, T[1000001], arr[500001];
long long ans = 0;


void count(int s, int e) {
    int mid = (s+e) >> 1;
    int i = s, j = mid+1, x = mid+1, y = e+1;
    int cnt = x-i;
    vector<int> temp;

    while (i < x && j < y) {
        if (arr[i] > arr[j]) {
            temp.emplace_back(arr[j++]);
            ans += cnt;
        }
        else {
            temp.emplace_back(arr[i++]);
            --cnt;
        }
    }

    while (i < x) temp.emplace_back(arr[i++]);
    while (j < y) temp.emplace_back(arr[j++]);

    for (int k = s; k < e+1; ++k) {
        arr[k] = temp[k-s];
    }

    return;
}

void merge(int s, int e) {
    if (s < e) {
        int mid = (s+e) >> 1;
        merge(s, mid);
        merge(mid+1, e);
        count(s, e);
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; ++i) {
        int t; cin >> t;
        T[t] = i;
    }

    for (int i = 0; i < N; ++i) {
        int t; cin >> t;
        arr[i] = T[t];
    }

    merge(0, N-1);

    cout << ans << '\n';

    return 0;
}
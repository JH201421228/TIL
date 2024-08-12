#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


vector<long long> arr;
vector<long long> temp;
long long ans = 0;

void merge (int s, int e) {
    int mid = (s+e) / 2;
    int i = s;
    int j = mid+1;
    int k = s;
    int cnt = 0;

    while (i <= mid && j <= e) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
            ans += (long long) cnt;
        }
        else {
            temp[k++] = arr[j++];
            cnt++;
        }
    }

    if (i > mid) {
        while (j <= e) {
            temp[k++] = arr[j++];
        }
    }
    else {
        while (i <= mid) {
            temp[k++] = arr[i++];
            ans += (long long) cnt;
        }
    }

    for (int idx = s; idx <= e; ++idx) {
        arr[idx] = temp[idx];
    }

    return;
}

void mergesort (int s, int e) {
    if (s < e) {
        int mid = (s+e) / 2;

        mergesort(s, mid);
        mergesort(mid+1, e);
        merge(s, e);
        return;
    }
    return;
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    arr.resize(N);
    temp.resize(N);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    mergesort(0, N-1);
    cout << ans << '\n';

    return 0;
}
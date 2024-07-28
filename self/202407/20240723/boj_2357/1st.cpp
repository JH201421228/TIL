#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


vector<long long> nums, tree1, tree2;
long long MAX = 1000000000;

long long I1(int s, int e, int idx) {
    if (s >= e) {
        tree1[idx] = nums[s];
        return tree1[idx];
    }

    int mid = (s+e) / 2;
    tree1[idx] = min(I1(s, mid, idx*2), I1(mid+1, e, idx*2+1));
    return tree1[idx];
}


long long I2(int s, int e, int idx) {
    if (s >= e) {
        tree2[idx] = nums[s];
        return tree2[idx];
    }

    int mid = (s+e) / 2;
    tree2[idx] = max(I2(s, mid, idx*2), I2(mid+1, e, idx*2+1));
    return tree2[idx];
}

long long S1(int s, int e, int l, int r, int idx) {
    if (s > r || e < l) {
        return MAX;
    }

    if (s >= l && e <= r) {
        return tree1[idx];
    }

    int mid = (s+e) / 2;
    long long v = min(S1(s, mid, l, r, idx*2), S1(mid+1, e, l, r, idx*2+1));
    return v;
}


long long S2(int s, int e, int l, int r, int idx) {
    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree2[idx];
    }

    int mid = (s+e) / 2;
    long long v = max(S2(s, mid, l, r, idx*2), S2(mid+1, e, l, r, idx*2+1));
    return v;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    cin >> N >> M;

    nums.resize(N+1);
    tree1.resize(4*N);
    tree2.resize(4*N);

    for (int i = 0; i < N; ++i) {
        cin >> nums[i+1];
    }

    I1(1, N, 1);
    I2(1, N, 1);

    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        cout << S1(1, N, a, b, 1) << ' ' << S2(1, N, a, b, 1) << '\n';
    }

    return 0;
}
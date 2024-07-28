#include <iostream>
#include <vector>
using namespace std;


vector<long long> nums, tree;

long long I(int s, int e, int i) {
    if (s == e) {
        tree[i] = nums[s-1];
        return tree[i];
    }

    int mid = (s+e) / 2;
    tree[i] = I(s, mid, i*2) + I(mid+1, e, i*2+1);
    return tree[i];
}

long long S(int s, int e, int l, int r, int idx) {
    if (e < l || s > r) {
        return 0;
    }

    if (l <= s && r >= e) {
        return tree[idx];
    }

    int mid = (s+e) / 2;
    long long val;
    val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1);
    return val;
}

void U(int s, int e, int idx, int cidx, long long val) {
    if (cidx > e || cidx < s) {
        return;
    }

    tree[idx] += val;

    if (s == e) {
        return;
    }

    int mid = (s+e) / 2;
    U(s, mid, idx*2, cidx, val);
    U(mid+1, e, idx*2+1, cidx, val);
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M, K;
    cin >> N >> M >> K;

    nums.resize(N);
    tree.resize(4*N);

    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    I(1, N, 1);

    for (int i = 0; i < M+K; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        if (a == 1) {
            long long v = c - nums[b-1];
            nums[b-1] = c;
            U(1, N, 1, b, v);
        }
        else {
            cout << S(1, N, b, c, 1) << '\n';
        }
    }

    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


vector<long long> nums;
vector<long long> tree;

long long I(int s, int e, int idx) {
    if (s == e) {
        tree[idx] = nums[s];
        return tree[idx];
    }

    int mid = (s+e) / 2;
    tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1);
    return tree[idx];
}


long long S(int s, int e, int l, int r, int idx) {
    if(s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[idx];
    }

    int mid = (s+e) / 2;
    long long val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1);
    return val;
}


void U(int s, int e, int nums_idx, int tree_idx, long long v) {
    if (nums_idx > e || nums_idx < s) {
        return;
    }

    tree[tree_idx] += v;

    if (s == e) {
        return;
    }

    int mid = (s+e) / 2;
    U(s, mid, nums_idx, tree_idx*2, v);
    U(mid+1, e, nums_idx, tree_idx*2+1, v);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, Q;
    cin >> N >> Q;

    nums.resize(N+1);
    tree.resize(4*N);
    nums[0] = 0;

    for (int i = 0; i < N; ++i) {
        cin >> nums[i+1];
    }

    I(1, N, 1);

    for (int i = 0; i < Q; ++i) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;
        cout << S(1, N, min(x, y), max(x, y), 1) << '\n';
        U(1, N, a, 1, b-nums[a]);
        nums[a] = b;
    }

    return 0;
}
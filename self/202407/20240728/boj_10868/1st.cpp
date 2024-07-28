#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


vector<long long> nums;
vector<long long> st;
long long MAXV = 1000000000;


int I(int s, int e, int idx) {
    if (s == e) {
        st[idx] = nums[s];
        return st[idx];
    }

    int mid = (s+e) / 2;
    st[idx] = min(I(s, mid, idx*2), I(mid+1, e, idx*2+1));
    return st[idx];
}


int S(int s, int e, int l, int r, int idx) {
    if (e < l || s > r) {
        return MAXV;
    }

    if (s >= l && e <= r) {
        return st[idx];
    }

    int mid = (s+e) / 2;
    long long val = min(S(s, mid, l, r, idx*2), S(mid+1, e, l, r, idx*2+1));
    return val;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    cin >> N >> M;

    nums.resize(N+1);
    nums[0] = 0;
    st.resize(4*N, MAXV);

    for (int i = 1; i <= N; ++i) {
        cin >> nums[i];
    }

    I(1, N, 1);

    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        cout << S(1, N, a, b, 1) << '\n';
    }

    return 0;
}
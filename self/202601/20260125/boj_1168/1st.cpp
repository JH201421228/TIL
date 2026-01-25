#include <iostream>
using namespace std;


int N, K;
int tree[400'005];


int I(int s, int e, int tree_idx) {
    if (s == e) {
        tree[tree_idx] = 1;
        return 1;
    }

    int mid = (s+e)>>1;

    tree[tree_idx] = I(s, mid, tree_idx<<1) + I(mid+1, e, tree_idx<<1|1);

    return tree[tree_idx];
}


int U(int s, int e, int tree_idx, int target) {
    tree[tree_idx] -= 1;

    if (s == e) return s;

    int mid = (s+e)>>1;

    if (target <= tree[tree_idx<<1]) return U(s, mid, tree_idx<<1, target);
    else return U(mid+1, e, tree_idx<<1|1, target-tree[tree_idx<<1]);
}


void solve() {
    cin >> N >> K;

    I(1, N, 1);

    int cur = K;
    cout << "<";
    for (int t = 0; t < N; ++t) {
        cout << U(1, N, 1, cur);

        if (t == N-1) break;
        cur = (cur+K-2) % (N-t-1) + 1;
        cout << ", ";
    }
    cout << ">" << "\n";

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
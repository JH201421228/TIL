#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <unordered_map>
#include <array>
using namespace std;


int N;
int yss[200'001 * 2];
int counts[200'001 * 8 + 1];
int tree[200'001 * 8 + 1];

vector<array<int, 4>> xs;
set<int> ys;
unordered_map<int, int> y_to_cnt;

void U(int s, int e, int l, int r, int tree_idx, int val) {
    if (s > r || e < l) return;

    if (s >= l && e <= r) counts[tree_idx] += val;

    else {
        int mid = (s+e)>>1;
        U(s, mid, l, r, tree_idx<<1, val);
        U(mid+1, e, l, r, tree_idx<<1|1, val);
    }

    if (counts[tree_idx]) tree[tree_idx] = yss[e+1] - yss[s];
    else {
        if (s == e) tree[tree_idx] = 0;
        else tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1];
    }

    return;
}


void solve() {
    cin >> N;
    
    for (int i = 0; i < N; ++i) {
        int x1, x2, y1, y2; cin >> x1 >> x2 >> y1 >> y2;
        
        xs.push_back({x1, y1, y2, 1});
        xs.push_back({x2, y1, y2, -1});
        ys.insert(y1);
        ys.insert(y2);
    }
    
    sort(xs.begin(), xs.end());
    
    int cnt = 0;
    
    for (auto& y : ys) {
        ++cnt;
        y_to_cnt[y] = cnt;
        yss[cnt] = y;
    }
    
    long long ans = 0;
    
    int prev, y1, y2;
    prev = xs[0][0]; y1 = xs[0][1]; y2 = xs[0][2];
    
    U(1, cnt-1, y_to_cnt[y1], y_to_cnt[y2]-1, 1, 1);
    
    for (int idx = 1; idx < xs.size(); ++idx) {
        int x, y1, y2, flag; x = xs[idx][0]; y1 = xs[idx][1]; y2 = xs[idx][2]; flag = xs[idx][3];
        
        ans += (long long) (x - prev) * tree[1];
        prev = x;
        U(1, cnt-1, y_to_cnt[y1], y_to_cnt[y2]-1, 1, flag);
    }
    
    cout << ans << '\n';
    
    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
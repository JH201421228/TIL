#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll MOD = 1'000'000'007;

int N, M;
ll tree[800'001];
vector<pair<int, int>> cordinates;
vector<int> xs;
unordered_map<int, int> x_dict;


ll S(int s, int e, int l, int r, int tree_idx) {
    if (s >= l && e <= r) return tree[tree_idx];
    
    if (l > e || r < s) return 0;

    int mid = (s+e)>>1;

    return S(s, mid, l, r, tree_idx<<1) + S(mid+1, e, l, r, tree_idx<<1|1);
}


void U(int s, int e, int idx, int tree_idx) {
    if (s == e && s == idx) {
        ++tree[tree_idx];
        return;
    }

    if (s > idx || e < idx) return;

    int mid = (s+e)>>1;

    U(s, mid, idx, tree_idx<<1);
    U(mid+1, e, idx, tree_idx<<1|1);

    tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1];

    return;
}


void solve() {
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int x, y; cin >> x >> y;
        cordinates.emplace_back(x, y);
        xs.emplace_back(x);
    }

    sort(xs.begin(), xs.end());

    int cur = 1;
    for (auto& x : xs) {
        if (x_dict.find(x) == x_dict.end()) {
            x_dict[x] = cur++;
        }
    }

    sort(cordinates.begin(), cordinates.end(), 
        [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

    M = x_dict.size();

    ll ans = 0;

    while (!cordinates.empty()) {
        int cur_x = cordinates.back().first;
        int cur_y = cordinates.back().second;
        cordinates.pop_back();
        
        vector<int> candidates;
        candidates.emplace_back(cur_x);
        
        while (!cordinates.empty() && cordinates.back().second == cur_y) {
            int cur_x = cordinates.back().first;
            int cur_y = cordinates.back().second;
            cordinates.pop_back();
            candidates.emplace_back(cur_x);
        }

        for (auto& x : candidates) {
            ans += S(1, M, 1, x_dict[x]-1, 1) * S(1, M, x_dict[x]+1, M, 1);
            ans %= MOD;
        }

        for (auto& x : candidates) U(1, M, x_dict[x], 1);
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
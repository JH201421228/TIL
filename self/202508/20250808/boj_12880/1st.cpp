#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int N, cnt, interval = 1e9;
int V[50];
int G[50][50];
vector<int> weights;


void dfs(int n, int l, int r, int flag) {
    cnt += 1;
    V[n] = 1;

    for (int x = 0; x < N; ++x) {
        if (flag) {
            if (!V[x] && l <= G[n][x] && G[n][x] <= r) dfs(x, l, r, flag);
        }
        else {
            if (!V[x] && l <= G[x][n] && G[x][n] <= r) dfs(x, l, r, flag);
        }
    }
}


bool checker(int l, int r) {
    fill(V, V+50, 0);
    cnt = 0;
    dfs(0, l, r, 0);
    if (cnt != N) return false;
    
    fill(V, V+50, 0);
    cnt = 0;
    dfs(0, l, r, 1);
    if (cnt != N) return false;

    return cnt == N;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    set<int> weights_set;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> G[i][j];
            weights_set.insert(G[i][j]);
        }
    }

    for (int w : weights_set) weights.emplace_back(w);
    sort(weights.begin(), weights.end());

    int s = 0;
    for (int e = 0; e < weights.size(); ++e) {
        for (; s <= e; ++s) {
            if (checker(weights[s], weights[e])) {
                interval = min(interval, weights[e] - weights[s]);
            }
            else break;
        }
    }

    cout << interval << '\n';

    return 0;
}
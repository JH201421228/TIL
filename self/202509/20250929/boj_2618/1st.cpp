#include <iostream>
#include <string.h>
using namespace std;

int N, W;
int dp[1'003][1'003];
int dp_trace[1'003][1'003];
pair<int, int> tasks[1'003];


int dist(int i, int j) {
    return abs(tasks[i].first - tasks[j].first) + abs(tasks[i].second - tasks[j].second);
}


int cal(int n, int m) {
    int x = max(n, m) + 1;
    if (x == W+2) return 0;
    if (dp[n][m] != -1) return dp[n][m];

    int first = cal(n, x) + dist(m, x);
    int second = cal(x, m) + dist(n, x);

    if (first > second) {
        dp[n][m] = second;
        dp_trace[n][m] = 1;
    }
    else {
        dp[n][m] = first;
        dp_trace[n][m] = 2;
    }

    return dp[n][m];
}


void solve(int N, int W) {
    tasks[0] = {1, 1};
    tasks[1] = {N, N};

    for (int i = 0; i < W; ++i) {
        int a, b; cin >> a >> b;
        tasks[i+2] = {a, b};
    }

    memset(dp, -1, sizeof(dp));
    memset(dp_trace, -1, sizeof(dp_trace));

    cout << cal(0, 1) << '\n';

    int n = 0, m = 1;
    for (int i = 2; i < W+2; ++i) {
        cout << dp_trace[n][m] << '\n';
        if (dp_trace[n][m] == 1) {
            n = i;
        }
        else {
            m = i;
        }
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> W;

    solve(N, W);

    return 0;
}
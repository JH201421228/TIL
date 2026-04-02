#include<iostream>
#include<stack>
#include<algorithm>
#include<string>
#include<climits>
using namespace std;


int N;
int cur[10'000];
int tar[10'000];
int dp[10'001][10];
int trace[10'001][10];
stack<int> ans;

void solve() {
    cin >> N;
    fill(&dp[0][0], &dp[0][0] + (N+1) * 10, INT_MAX);
    fill(&trace[0][0], &trace[0][0] + (N+1) * 10, 0);

    for (int idx = 0; idx < 10; ++idx) dp[0][idx] = idx;
    
    string tmp1, tmp2; cin >> tmp1 >> tmp2;
    for (int i = 0; i < N; ++i) cur[i] = tmp1[i] - '0';
    for (int i = 0; i < N; ++i) tar[i] = tmp2[i] - '0';

    for (int i = 1; i < N+1; ++i) {
        for (int j = 0; j < 10; ++j) {
            for (int k = 0; k < 10; ++k) {
                int l = (j - k + 10) % 10;
                int cur_n = (cur[i-1] + j) % 10;
                int diff = (cur_n - tar[i-1] + 10) % 10;

                if (dp[i-1][k] + diff + l < dp[i][j]) {
                    dp[i][j] = dp[i-1][k] + diff + l;
                    trace[i][j] = k;
                } 
            }
        }
    }

    int min_val = dp[N][0];
    int cur_idx = 0;

    for (int i = 1; i < 10; ++i) {
        if (dp[N][i] < min_val) {
            min_val = dp[N][i];
            cur_idx = i;
        }
    }
    cout << min_val << '\n';

    ans.push(cur_idx);
    for (int idx = N; idx > 1; --idx) {
        cur_idx = trace[idx][cur_idx];
        ans.push(cur_idx);
    }

    int acc = 0;
    int idx = 0;
    while (!ans.empty()) {
        int a = ans.top(); ans.pop();
        int left = (a - acc + 10) % 10;
        int right = ((cur[idx] + a) % 10 - tar[idx] + 10) % 10;

        if (left > 0) cout << idx+1 << ' ' << left << '\n';
        else cout << idx+1 << ' ' << -right << '\n';

        acc = a;
        ++idx;
    }
    
    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    int T, W, v, prev = 0, cnt = 0;

    cin >> T >> W;

    vector<int> vals;

    for (int i = 0; i < T; i++) {
        cin >> v;
        
        if (i == 0 && v == 1) {
            vals.emplace_back(0);
        }

        if (prev != 0 && prev != v) {
            vals.emplace_back(cnt);
            cnt = 0;
        }

        ++cnt;
        prev = v;
    }
    vals.emplace_back(cnt);

    int L = vals.size() + 1;
    vector<vector<int>> dp(W+1, vector<int>(L, 0));

    for (int i = 1; i < L; i++) {
        if (i%2) {
            dp[0][i] = dp[0][i-1];
        }
        else {
            dp[0][i] = dp[0][i-1] + vals[i-1];
        }
    }

    int ans = dp[0][L-1];

    for (int i = 1; i < W+1; i++) {
        for (int j = 1; j < L; j++) {
            if (i%2) {
                if (j%2) {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + vals[j-1];
                }
                else {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]);
                }
            }
            else {
                if (j%2) {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]);
                }
                else {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + vals[j-1];
                }
            }
        }
        ans = max(dp[i][L-1], ans);
    }

    cout << ans << endl;

    return 0;
}
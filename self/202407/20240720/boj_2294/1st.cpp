#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, K;
    cin >> N >> K;
    vector<int> dp(K+1, 0);

    int c;
    for (int i = 0; i < N; ++i) {
        cin >> c;

        if (c <= K) {
            dp[c] = 1;

            for (int j = c+1; j < K+1; ++j) {
                if (dp[j-c]) {
                    if (dp[j]) {
                        dp[j] = min(dp[j], dp[j-c]+1);
                    }
                    else {
                        dp[j] = dp[j-c] + 1;
                    }
                }
            }
        }
    }

    if (dp[K]) {
        cout << dp[K];
    }

    else {
        cout << -1;
    }

    return 0;
}
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M, ans = 0;
    cin >> N >> M;
    int dp[N][M] = {0};
    char c;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> c;
            dp[i][j] = c - '0';
        }
    }

    for (int i = 0; i < N; ++i) {
        if (dp[i][0]) {
            ans = 1;
            break;
        }
    }

    for (int i = 0; i < M; ++i) {
        if (dp[0][i]) {
            ans = 1;
            break;
        }
    }

    for (int i = 1; i < N; ++i) {
        for (int j = 1; j < M; ++j) {
            if (dp[i][j]) {
                dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                ans = max(ans, dp[i][j]);
            }
        }
    }

    cout << ans*ans << endl;

    return 0;
}
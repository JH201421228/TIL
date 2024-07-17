#include <iostream>
#include <vector>
using namespace std;


int main() {
    int T, N, M;

    cin >> T;

    while (T--) {
        cin >> N;

        int coins[N] = {0};

        for (int i = 0; i < N; ++i) {
            cin >> coins[i];
        }

        cin >> M;

        int dp[M+1] = {0};
        dp[0] = 1;

        for (int c: coins) {
            for (int i = c; i < M+1; ++i) {
                dp[i] = dp[i] + dp[i-c];
            }
        }

        cout << dp[M] << endl;
    }

    return 0;
}
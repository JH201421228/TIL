#include <iostream>
#include <vector>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M;

    cin >> N;

    int nums[N];

    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    vector<vector<int>> dp(N, vector<int>(N, 0));

    int n, di = -1, dj = 1;

    for (int i = 0; i < N; ++i) {
        dp[i][i] = 1;
        if (i+1 < N && nums[i] == nums[i+1]) {
            dp[i][i+1] = 1;
        }

        n = 1;
        while (i+n*di >= 0 && i+n*dj < N) {
            if (dp[i+(n-1)*di][i+(n-1)*dj] == 0) {
                break;
            }
            else if (nums[i+n*di] == nums[i+n*dj]) {
                dp[i+n*di][i+n*dj] = 1;
            }

            ++n;
        }

        n = 1;
        while (i+n*di >= 0 && i+n*dj+1 < N) {
            if (dp[i+(n-1)*di][i+(n-1)*dj+1] == 0) {
                break;
            }
            else if (nums[i+n*di] == nums[i+n*dj+1]) {
                dp[i+n*di][i+n*dj+1] = 1;
            }

            ++n;
        }
    }

    cin >> M;

    int S, E;

    for (int i = 0; i < M; ++i) {
        cin >> S >> E;

        cout << dp[S-1][E-1] << '\n';
    }

    return 0;
}
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    int M;
    cin >> M;

    vector<vector<int>> dp(N, vector<int>(N, 0));

    // 길이 1과 길이 2인 팰린드롬 초기화
    for (int i = 0; i < N; ++i) {
        dp[i][i] = 1;
        if (i + 1 < N && nums[i] == nums[i + 1]) {
            dp[i][i + 1] = 1;
        }
    }

    // 길이 3 이상인 팰린드롬 확인
    for (int length = 3; length <= N; ++length) {
        for (int i = 0; i <= N - length; ++i) {
            int j = i + length - 1;
            if (nums[i] == nums[j] && dp[i + 1][j - 1] == 1) {
                dp[i][j] = 1;
            }
        }
    }

    for (int i = 0; i < M; ++i) {
        int S, E;
        cin >> S >> E;
        cout << dp[S - 1][E - 1] << endl;
    }

    return 0;
}

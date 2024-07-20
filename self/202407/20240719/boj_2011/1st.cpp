#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string S;
    cin >> S;

    int s = S.size();

    vector<int> dp(s, 0);
    dp[0] = 1;

    if (S[0] == '0') {
        cout << 0 << '\n';
        return 0;
    }

    if (s >= 2) {
        if (S[1] == '0') {
            if (S[0] == '1' || S[0] == '2') {
                dp[1] = dp[0];
            }
            else {
                cout << 0 << '\n';
                return 0;
            }
        }
        else {
            dp[1] = 1;
            if ((S[0] - '0') * 10 + (S[1] - '0') <= 26) {
                dp[1] = 2;
            }
        }
    }

    for (int i = 2; i < s; ++i) {
        if (S[i] == '0') {
            if (S[i-1] == '1' || S[i-1] == '2') {
                dp[i] = dp[i-2];
            }
            else {
                cout << 0 << '\n';
                return 0;
            }
        }
        else {
            dp[i] = dp[i-1];
            if (S[i-1] == '0') {
                continue;
            }
            else if ((S[i-1] - '0') * 10 + (S[i] - '0') <= 26) {
                dp[i] += dp[i-2];
                dp[i] %= 1000000;
            }
        }
    }

    cout << dp[s-1] % 1000000;

    return 0;
}
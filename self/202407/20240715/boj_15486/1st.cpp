#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[1500051];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;

    int ans = 0;

    for (int i = 0; i < N; i++) {
        int c, d;
        cin >> d >> c;

        dp[i+d] = max(dp[i+d], ans+c);

        ans = max(ans, dp[i+1]);
    }

    cout << ans << endl;
}
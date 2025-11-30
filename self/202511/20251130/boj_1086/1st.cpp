#include <iostream>
using namespace std;


int N, K;
int seq[15];
int pow_seq[15];
int next_seq[15][100];
long long dp[1<<15][100];
string string_seq[15];


long long gcd(long long a, long long b) {
    while (b) {
        long long r = a%b;
        a = b;
        b = r;
    }

    return a;
}


void solve() {
    cin >> N;
    for (int idx = 0; idx < N; ++idx) cin >> string_seq[idx];
    cin >> K;

    dp[0][0] = 1;

    for (int i = 0; i < N; ++i) {
        int cur = 0;
        for (char c : string_seq[i]) {
            cur = (cur * 10 + (c - '0')) % K;
        }
        seq[i] = cur;

        int pow = 1;
        int len = string_seq[i].size();

        while (len--) pow = (pow * 10) % K;

        pow_seq[i] = pow;
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < K; ++j) {
            next_seq[i][j] = (j * pow_seq[i] + seq[i]) % K;
        }
    }

    for (int cur = 0; cur < (1<<N); ++cur) {
        for (int i = 0; i < N; ++i) {
            if (cur & (1<<i)) continue;

            for (int j = 0; j < K; ++j) {
                dp[cur | (1<<i)][next_seq[i][j]] += dp[cur][j];
            }
        }
    }

    long long a = dp[(1<<N)-1][0];
    long long b = 0;
    for (int idx = 0; idx < K; ++idx) b += dp[(1<<N)-1][idx];

    long long c = gcd(b, a);

    cout << a/c << '/' << b/c << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
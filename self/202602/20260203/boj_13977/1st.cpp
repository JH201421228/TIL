#include <iostream>
#include <cmath>
using namespace std;


const long long MOD = 1'000'000'007;
long long mods[4'000'001];
int T, N, K;


long long recur(long long cur, long long n) {
    if (!n) return 1;

    long long tmp = recur(cur, n/2);

    if (n%2) {
        --n;
        return (((tmp * tmp) % MOD) * cur) % MOD;
    }
    else return (tmp * tmp) % MOD;
}


void solve() {
    cin >> N >> K;

    cout << ((mods[N] * recur(mods[K], MOD-2)) % MOD) * recur(mods[N-K], MOD-2) % MOD << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    mods[0] = 1; mods[1] = 1;

    for (int i = 2; i < 4'000'001; ++i) mods[i] = (mods[i-1] * i) % MOD;

    cin >> T;

    while (T--) solve();

    return 0;
}
#include <iostream>
#include <tuple>
using namespace std;


int MAX = 1e9;
int T, K, C;


tuple<long long, long long, long long> egcd(long long a, long long b) {
    long long x0 = 1;
    long long x1 = 0;
    long long y0 = 0;
    long long y1 = 1;

    long long na, nb, nx0, nx1, ny0, ny1;

    while (b) {
        long long q = a / b;
        na = b; nb = a % b; a = na; b = nb;
        nx0 = x1; nx1 = x0 - q*x1; x0 = nx0; x1 = nx1;
        ny0 = y1; ny1 = y0 - q*y1; y0 = ny0; y1 = ny1;
    }

    return {a, x0, y0};
}


void solve() {
    cin >> K >> C;

    if (C == 1) {
        if (K+1 <= MAX) cout << K+1 << '\n';
        else cout << "IMPOSSIBLE" << '\n';
        return;
    }

    if (K == 1) {
        cout << 1 << '\n';
        return;
    }

    auto[g, x ,y] = egcd((long long) C, (long long) K);

    if (g != 1) {
        cout << "IMPOSSIBLE" << '\n';
        return;
    }

    long long ans = (x % K + K) % K;

    if (ans == 0) ans += K;

    if (ans > MAX) {
        cout << "IMPOSSIBLE" << '\n';
        return;
    }

    cout << ans << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    
    while (T--) solve();

    return 0;
}
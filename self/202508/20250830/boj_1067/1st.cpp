#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>
using namespace std;

using cd = complex<double>;
const double PI = acos(-1.0);

int N;
cd u[60000 * 8], v[60000 * 8], res[60000 * 16];

void fft(cd* v, int N, bool inv) {
    for (int i = 1, j = 0; i < N; ++i) {
        int bit = N >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;

        if (i < j) swap(v[i], v[j]);
    }

    int k = 1;
    while (k < N) {
        double ang = (PI/k) * (inv? 1.0 : -1.0);
        cd w(cos(ang), sin(ang));
        for (int i = 0; i < N; i += (k<<1)) {
            cd wp(1.0, 0.0);
            for (int j = 0; j < k; ++j) {
                cd x = v[i+j];
                cd y = v[i+j+k] * wp;

                v[i+j] = x + y;
                v[i+j+k] = x - y;

                wp *= w;
            }
        }

        k <<= 1;
    }

    if (inv) {
        for (int idx = 0; idx < N; ++idx) v[idx] /= N;
    }

    return;
}

void fft_wrapper(cd* u, cd* v, int N) {
    int n = 1;
    while (n < 2*N) n <<= 1;
    n <<= 1;

    fft(v, n, false);
    fft(u, n, false);

    for (int idx = 0; idx < n; ++idx) res[idx] = u[idx] * v[idx];

    fft(res, n, true);

    int ans = 0;

    for (int idx = n-1; idx >= 0; --idx) ans = max(ans, (int) round(res[idx].real()));

    cout << ans << '\n';

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int idx = 0; idx < N; ++idx) {
        cin >> u[idx];
        u[idx + N] = u[idx];
    }
    for (int idx = 0; idx < N; ++idx) cin >> v[N-1-idx];

    fft_wrapper(u, v, N);

    // for (int idx = 0; idx < 2*N; ++idx) cout << u[idx] << '\n';

    return 0;
}
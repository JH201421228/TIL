#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>
using namespace std;

using cd = complex<double>;
const double PI = acos(-1.0);

int N = 1 << 21;
int n = 1000000;
cd prime[1<<21], semi[1<<21];

void sieve() {
    fill(prime, prime+n, cd(1.0, 0.0));
    prime[0].real(0.0);
    prime[1].real(0.0);

    for (int i = 2; i < (int) sqrt(n) + 1; ++i) {
        if (prime[i].real() == 1.0) {
            for (int j = i*i; j < n+1; j += i) {
                prime[j].real(0.0);
            }
        }
    }

    prime[2] = 0;

    return;
}


void fft(cd* u, bool inv) {
    for (int i = 1, j = 0; i < N; ++i) {
        int bit = N >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        
        if (i < j) swap(u[i], u[j]);
    }

    int k = 1;
    while (k < N) {
        double ang = (PI/k) * (inv? 1.0 : -1.0);
        cd w(cos(ang), sin(ang));
        for (int i = 0; i < N; i += (k<<1)) {
            cd wp(1.0, 0.0);
            for (int j = 0; j < k; ++j) {
                cd x = u[i+j];
                cd y = u[i+j+k] * wp;

                u[i+j] = x + y;
                u[i+j+k] = x - y;

                wp *= w;
            }
        }

        k <<= 1;
    }

    if (inv) {
        for (int idx = 0; idx < N; ++idx) u[idx] /= N;
    }

    return;
}


void fft_wrapper(cd* u, cd* v) {
    fft(u, false);
    fft(v, false);

    for (int idx = 0; idx < N; ++idx) u[idx] *= v[idx];

    fft(u, true);

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    sieve();
    for (int i = 0; i < n+1; ++i) {
        if (prime[i].real() == 1.0 && 2*i < n+1) semi[2*i] = cd(1.0, 0.0);
    }
    semi[4] = cd(1.0, 0.0);

    fft_wrapper(prime, semi);

    int t; cin >> t;
    for (int i = 0; i < t; ++i) {
        int q; cin >> q;
        cout << (int) round(prime[q].real()) << '\n';
    }

    return 0;
}
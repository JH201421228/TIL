#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>
using namespace std;

using cd = complex<double>;
const double PI = acos(-1.0);

int n = 1'000'000;
int N = 1 << 20;

cd isPrime[1 << 21];
cd oddPrime[1 << 20];


void fft(cd* v, bool inv) {
    int j = 0;
    for (int i = 1; i < N; ++i) {
        int b = N >> 1;
        while (j & b) {
            j ^= b;
            b >>= 1;
        }
        j ^= b;

        if (i < j) swap(v[i], v[j]);
    }

    int k = 1;
    while (k < N) {
        double a = (PI/k) * (inv? 1.0 : -1.0);
        cd w(cos(a), sin(a));

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


void fft_wrapper(cd* u) {
    fft(u, false);

    for (int i = 0; i < N; ++i) u[i] *= u[i];

    fft(u, true);

    return;
}


void sieve() {
    fill(isPrime, isPrime+n, cd(1.0, 0.0));
    isPrime[0].real(0.0);
    isPrime[1].real(0.0);

    for (int i = 2; i < sqrt(n)+1; ++i) {
        if (isPrime[i].real() == 1.0) {
            for (int j = i*i; i < n+1) {

            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);



    return 0;
}
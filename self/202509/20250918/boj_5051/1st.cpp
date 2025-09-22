#include <iostream>
#include <algorithm>
#include <complex>
using namespace std;

using cd = complex<double>;
const double PI = acos(-1);

int N = 1<<20;
cd u[1<<20];
int v[1<<19];

void fft(cd* v, bool inv) {
    for (int i = 1, j = 0; i < N; ++i) {
        int b = N >> 1;
        while (j&b) {
            j ^= b;
            b >>= 1;
        }
        j ^= b;
    
        if (i < j) {
            swap(v[i], v[j]);
        }
    }

    int k = 1;
    while (k < N) {
        double a = (PI/k) * (inv? 1 : -1);
        cd w(cos(a), sin(a));

        for (int i = 0; i < N; i += (k<<1)) {
            cd wp(1, 0);
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
        for (int i = 0; i < N; ++i) {
            v[i] /= N;
        }
    }

    return;
}


void fft_wrapper(cd* u, int* v, int n) {
    fft(u, false);

    for (int i = 0; i < N; ++i) {
        u[i] *= u[i];
    }

    fft(u, true);

    long long ans = 0;

    for (int i = 0; i < N; ++i) {
        int tmp = round(u[i].real());
        if (tmp > 0 && v[i%n] > 0) {
            if (i % 2) {
                ans += (tmp/2) * v[i%n];
            }
            else {
                ans += (((tmp-v[i/2])/2) + v[i/2]) * v[i%n];
            }
        }
    }

    cout << ans << '\n';

    return;
}


void solve(int N) {
    for (int i = 1; i < N; ++i) {
        u[(int) ((1ULL*i*i)%N)] += cd(1, 0);
        v[(int) ((1ULL*i*i)%N)] += 1;
    }

    fft_wrapper(u, v, N);

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n; cin >> n;
    solve(n);

    return 0;
}
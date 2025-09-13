#include <iostream>
#include <algorithm>
#include <complex>
using namespace std;

using cd = complex<double>;
const double PI = acos(-1.0);

int N = 1<<20;
cd u[1<<20], v[1<<20];


void fft(cd* v, bool inv) {
    for (int i = 1, j = 0; i < N; ++i) {
        int b = N>>1;
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
        double a = (PI/k) * (inv? 1.0 : -1.0);
        cd w(cos(a), sin(a));

        for (int i = 0; i < N; i += (k<<1)) {
            cd wp(1, 0);
            for (int j = 0; j < k; ++j) {
                cd x = v[i+j];
                cd y = v[i+j+k] * wp;

                v[i+j] = x+y;
                v[i+j+k] = x-y;

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


void fft_wrapper(cd* u, cd* v) {
    fft(u, false);
    fft(v, false);

    for (int i = 0; i < N; ++i) {
        u[i] *= v[i];
    }

    fft(u, true);

    int ans = 0;

    for (int i = 0; i < N; ++i) {
        ans = max(ans, (int) round(u[i].real()));
    }

    cout << ans << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string u_temp; cin >> u_temp;
    string v_temp; cin >> v_temp;

    int length = u_temp.length();

    for (int i = 0; i < length; ++i) {
        u[i].real(u_temp[i] - 48);
        u[i+length].real(u_temp[i] - 48);
        v[length-1-i].real(v_temp[i] - 48);
    }

    fft_wrapper(u, v);

    return 0;
}
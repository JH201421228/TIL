#include <iostream>
#include <complex>
#include <vector>
#include <algorithm>

using namespace std;

using cd = complex<double>;
const double PI = acos(-1.0);


int N, M;
int shot[200001], distances[200001];
cd v[800001];

void fft(cd* v, int n, bool invert) {
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(v[i], v[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2.0*PI / len * (invert ? -1.0 : 1.0);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1.0, 0.0);
            int half = len >> 1;

            for (int j = 0; j < half; ++j) {
                cd u = v[i+j];
                cd t = v[i+j+half]*w;
                v[i+j] = u+t;
                v[i+j+half] = u-t;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (int i = 0; i < n; ++i) v[i] /= n;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 0; i < N; ++i) cin >> shot[i];
    cin >> M;
    for (int i = 0; i < M; ++i) cin >> distances[i];

    int maxS = 0;
    for (int x : shot) if (x > maxS) maxS = x;

    int base = maxS+1;
    int n = 1;
    while (n < base<<1) n <<= 1;

    v[0] = 1.0;
    for (int x : shot) v[x] = 1.0;

    fft(v, n, false);
    for (int i = 0; i < n; ++i) v[i] *= v[i];
    fft(v, n, true);

    long long ans = 0;
    for (int i = 0; i < M; ++i) {
        int d = distances[i];
        if (d >= 0 && d < n) {
            long long cnt = llround(v[d].real());
            if (cnt > 0) ++ans;
        }
    }
    
    cout << ans << '\n';

    return 0;
}
#include <iostream>
#include <array>
using namespace std;


long long N;
long long MOD = 1'000'000'007;

using Matrix = array<array<long long, 2>, 2>;


Matrix cal(Matrix& mat1, Matrix& mat2) {
    Matrix res {{{0, 0}, {0, 0}}};

    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            for (int k = 0; k < 2; ++k) {
                res[i][j] += (mat1[i][k] * mat2[k][j]) % MOD;
                res[i][j] %= MOD;
            }
        }
    }

    return res;
}


Matrix recur(long long n, Matrix mat) {
    Matrix res = {{{1, 0}, {0, 1}}};
    while (n) {
        if (n%2) res = cal(res, mat);
        mat = cal(mat, mat);
        n /= 2;
    }

    return res;
}


void solve() {
    cin >> N;

    if (N%2) {
        cout << 0 << '\n';
        return;
    }

    Matrix res = {{{4, -1}, {1, 0}}};
    res = recur(N/2, res);
    cout << (res[0][0] + res[0][1] + MOD) % MOD << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
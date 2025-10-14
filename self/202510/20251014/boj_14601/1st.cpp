#include <iostream>
#include <array>
using namespace std;


int K, ti, tj, cnt = 1;
int ans[1<<7][1<<7];
int delta[4][2] = {{0, 0}, {1, 0}, {0, 1}, {1, 1}};


array<array<int, 2>, 4> set_num(int i, int j, int ti, int tj, int l) {
    array<array<int, 2>, 4> res;
    
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 2; ++j) {
            res[i][j] = -1;
        }
    }

    if (ti >= i && ti < i+l && tj >= j && tj < j+l) {
        ;
    }
    else {
        ans[i+l-1][j+l-1] = cnt;
        res[0][0] = i+l-1;
        res[0][1] = j+l-1;
    }

    if (ti >= i+l && ti < i+l*2 && tj >= j && tj < j+l) {
        ;
    }
    else {
        ans[i+l][j+l-1] = cnt;
        res[1][0] = i+l;
        res[1][1] = j+l-1;
    }

    if (ti >= i && ti < i+l && tj >= j+l && tj < j+l*2) {
        ;
    }
    else {
        ans[i+l-1][j+l] = cnt;
        res[2][0] = i+l-1;
        res[2][1] = j+l-1;
    }

    if (ti >= i+l && ti < i+l*2 && tj >= j+l && tj < j+l*2) {
        ;
    }
    else {
        ans[i+l][j+l] = cnt;
        res[3][0] = i+l-1;
        res[3][1] = j+l-1;
    }

    ++cnt;

    return res;
}


void dq(int i, int j, int ti, int tj, int l) {
    if (l == 1) {
        for (int di = 0; di < 2; ++di) {
            for (int dj = 0; dj < 2; ++dj) {
                if (!ans[i+di][j+dj]) {
                    ans[i+di][j+dj] = cnt;
                }
            }
        }
        ++cnt;
        return;
    }

    array<array<int, 2>, 4> temp = set_num(i, j, ti, tj, l);

    for (int idx = 0; idx < 4; ++idx) {
        int di = delta[idx][0] * l;
        int dj = delta[idx][1] * l;

        if (temp[idx][0] != -1 && temp[idx][1] != -1) {
            dq(i+di, j+dj, temp[idx][0], temp[idx][1], l/2);
        }
        else {
            dq(i+di, j+dj, ti, tj, l/2);
        }
    }

    return;
}


void solve() {
    cin >> K >> ti >> tj;
    int tmp_i = ti, tmp_j = tj;

    ti = (1<<K)-tmp_j;
    tj = tmp_i-1;

    ans[ti][tj] = -1;

    dq(0, 0, ti, tj, (1<<(K-1)));

    for (int i = 0; i < (1<<K); ++i) {
        for (int j = 0; j < (1<<K); ++j) {
            cout << ans[i][j] << ' ';
        }
        cout << '\n';
    }

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
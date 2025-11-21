#include <iostream>
#include <vector>
#include <queue>
using namespace std;


double lines[3'001][4];
int N;
int V[3'001];
vector<int> G[3'001];
queue<int> q;


bool is_same_dot(double d1[], double d2[], double d3[], double d4[]) {
    if ((d1[0] == d3[0] && d1[1] == d3[1]) ||
        (d1[0] == d4[0] && d1[1] == d4[1]) ||
        (d2[0] == d3[0] && d2[1] == d3[1]) ||
        (d2[0] == d4[0] && d2[1] == d4[1])) {
        return true;
    }

    return false;
}

bool is_online(double d1[], double d2[], double d3[]) {
    if (d3[0] >= min(d1[0], d2[0]) &&
        d3[0] <= max(d1[0], d2[0]) &&
        d3[1] >= min(d1[1], d2[1]) &&
        d3[1] <= max(d1[1], d2[1]) &&
        ((d1[1] - d3[1]) * (d2[0] - d3[0])) ==
        ((d1[0] - d3[0]) * (d2[1] - d3[1]))) {
        return true;
    }

    return false;
}


bool ccw(double d1[], double d2[], double d3[], double d4[]) {
    double expr1 = (d3[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d3[1] - d2[1]);
    double expr2 = (d4[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d4[1] - d2[1]);
    double expr3 = (d1[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d1[1] - d4[1]);
    double expr4 = (d2[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d2[1] - d4[1]);
    
    if (expr1 * expr2 < 0 && expr3 * expr4 < 0) {
        return true;
    }

    return false;
}


bool cross_check(double d1[], double d2[], double d3[], double d4[]) {
    if (is_same_dot(d1, d2, d3, d4)) return true;

    if (is_online(d1, d2, d3)) return true;

    if (is_online(d1, d2, d4)) return true;

    if (is_online(d3, d4, d1)) return true;

    if (is_online(d3, d4, d2)) return true;

    if (ccw(d1, d2, d3, d4)) return true;

    return false;
}


int travel(int n) {
    int res = 0;

    V[n] = 1;
    q.push(n);

    while (!q.empty()) {
        int n = q.front();
        q.pop();

        ++res;

        for (auto& x : G[n]) {
            if (!V[x]) {
                V[x] = 1;
                q.push(x);
            }
        }
    }

    return res;
}


void solve() {
    cin >> N;

    for (int idx = 0; idx < N; ++idx) {
        cin >> lines[idx][0] >> lines[idx][1] >> lines[idx][2] >> lines[idx][3];
    }

    for (int i = 0; i < N; ++i) {
        for (int j = i+1; j <N; ++j) {
            if (cross_check(lines[i], lines[i]+2, lines[j], lines[j]+2)) {
                G[i+1].emplace_back(j+1);
                G[j+1].emplace_back(i+1);
            }
        }
    }

    int res = 0, cnt = 0;

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) {
            ++cnt;
            res = max(res, travel(n));
        }
    }

    cout << cnt << '\n' << res << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
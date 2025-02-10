#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>
using namespace std;

int N, T[75001], C;
vector<pair<int, int>> islands;
vector<int> xs, ys;
map<int, int> xd, yd;

int S(int idx) {
    int res = 0;
    while (idx > 0) {
        res += T[idx];
        idx -= (idx & -idx);
    }
    return res;
}

void U(int idx) {
    while (idx < N+1) {
        T[idx] += 1;
        idx += (idx & -idx);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> C;

    for (int z = 0; z < C; ++z) {
        cin >> N;

        islands.clear();
        xs.clear();
        ys.clear();
        xd.clear();
        yd.clear();
        fill(T, T + N + 1, 0);

        for (int i = 0; i < N; ++i) {
            int x, y;
            cin >> x >> y;
            islands.emplace_back(x, -y);
            xs.emplace_back(x);
            ys.emplace_back(-y);
        }

        sort(xs.begin(), xs.end());
        sort(ys.begin(), ys.end());

        int prex = 1, prey = 1;
        for (int i = 0; i < N; ++i) {
            if (!xd.count(xs[i])) xd[xs[i]] = prex++;
            if (!yd.count(ys[i])) yd[ys[i]] = prey++;
        }

        for (int i = 0; i < N; ++i)
            islands[i] = {xd[islands[i].first], yd[islands[i].second]};

        sort(islands.begin(), islands.end());

        long long ans = 0;
        for (auto& coord : islands) {
            ans += S(coord.second);
            U(coord.second);
        }

        cout << ans << '\n';
    }

    return 0;
}

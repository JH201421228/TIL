#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class FenwickTree {
public:
    vector<int> T;
    int N;

    FenwickTree(int n) : N(n) {
        T.assign(N + 1, 0);
    }

    void update(int idx) {
        while (idx <= N) {
            T[idx] += 1;
            idx += (idx & -idx);
        }
    }

    int sum(int idx) {
        int res = 0;
        while (idx > 0) {
            res += T[idx];
            idx -= (idx & -idx);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<pair<int, int>> islands;
        vector<int> xs, ys;
        map<int, int> xd, yd;

        for (int i = 0; i < N; i++) {
            int x, y;
            cin >> x >> y;
            islands.emplace_back(x, -y);
            xs.push_back(x);
            ys.push_back(-y);
        }

        sort(xs.begin(), xs.end());
        sort(ys.begin(), ys.end());

        int prex = 1, prey = 1;
        for (int i = 0; i < N; i++) {
            if (xd.find(xs[i]) == xd.end()) xd[xs[i]] = prex++;
            if (yd.find(ys[i]) == yd.end()) yd[ys[i]] = prey++;
        }

        for (int i = 0; i < N; i++) {
            int x = islands[i].first, y = islands[i].second;
            islands[i] = {xd[x], yd[y]};
        }

        sort(islands.begin(), islands.end());
        FenwickTree ft(N);

        long long ans = 0;
        for (auto &[x, y] : islands) {
            ans += ft.sum(y);
            ft.update(y);
        }

        cout << ans << "\n";
    }

    return 0;
}
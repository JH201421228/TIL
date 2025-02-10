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

    return;
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
        memset(T, 0, sizeof(T));

        for (int i = 0; i < N; ++i) {
            int x, y; cin >> x >> y;
            islands.emplace_back(x, -y);
            xs.emplace_back(x);
            ys.emplace_back(-y);
        }
    
        sort(xs.begin(), xs.end());
        sort(ys.begin(), ys.end());
    
        int prex = 1, prey = 1;
        for (int i = 0; i < N; ++i) {
            if (xd.find(xs[i]) == xd.end()) xd[xs[i]] = prex++;
            if (yd.find(ys[i]) == yd.end()) yd[ys[i]] = prey++;
        }
    
        for (int i = 0; i < N; ++i) islands[i] = {xd[islands[i].first], yd[islands[i].second]};
    
        sort(islands.begin(), islands.end());
    
        long long ans = 0;
        for (auto& cordinates : islands) {
            ans += S(cordinates.second);
            U(cordinates.second);
        }
    
        cout << ans << '\n';
    }

    return 0;
}
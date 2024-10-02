#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<pair<long long, int>> X;
vector<pair<long long, int>> Y;
vector<pair<long long, int>> Z;
vector<int> P;
vector<pair<long long, pair<int, int>>> M;

int find(int idx) {
    if (P[idx] == idx) {
        return idx;
    }

    P[idx] = find(P[idx]);

    return P[idx];
}

void uni(int a, int b) {
    a = find(a);
    b = find(b);

    if (a > b) {
        P[a] = b;
    }
    else {
        P[b] = a;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N; cin >> N;

    P.resize(N);
    for (int i = 0; i < N; ++i) {
        P[i] = i;
    }

    for (int i = 0; i < N; ++i) {
        long long x, y, z; cin >> x >> y >> z;

        X.emplace_back(x, i);
        Y.emplace_back(y, i);
        Z.emplace_back(z, i);
    }

    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    sort(Z.begin(), Z.end());

    for (int i = 0; i < N-1; ++i) {
        M.emplace_back(X[i+1].first-X[i].first, make_pair(X[i].second, X[i+1].second));
        M.emplace_back(Y[i+1].first-Y[i].first, make_pair(Y[i].second, Y[i+1].second));
        M.emplace_back(Z[i+1].first-Z[i].first, make_pair(Z[i].second, Z[i+1].second));
    }

    sort(M.begin(), M.end());

    int cnt = 0;
    long long ans = 0;
    int idx = 0;

    while (cnt < N-1) {
        int a = M[idx].second.first;
        int b = M[idx].second.second;

        if (find(a) != find(b)) {
            ans += M[idx].first;
            ++cnt;
            uni(a, b);
        }

        ++idx;
    }

    cout << ans << "\n";

    return 0;
}
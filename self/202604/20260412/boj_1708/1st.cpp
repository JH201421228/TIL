#include <bits/stdc++.h>

using namespace std;


int N;
vector<pair<int, int>> dots;


void solve() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        pair<int, int> temp;
        cin >> temp.first >> temp.second;
        dots.emplace_back(temp);
    }

    sort(dots.begin(), dots.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });

    pair<int, int> origin = dots[0];

    vector<pair<int, int>> rest(dots.begin()+1, dots.end());

    sort(rest.begin(), rest.end(), [&](const pair<int, int> &a, const pair<int, int> &b) {
        double angleA = atan2(a.second - origin.second, a.first - origin.first);
        double angleB = atan2(b.second - origin.second, b.first - origin.first);

        if (angleA == angleB) {
            long long distA = 1LL * (a.second - origin.second) * (a.second - origin.second)
                            + 1LL * (a.first - origin.first) * (a.first - origin.first);
            long long distB = 1LL * (b.second - origin.second) * (b.second - origin.second)
                            + 1LL * (b.first - origin.first) * (b.first - origin.first);
            return distA < distB;
        }
        return angleA < angleB;
    });

    vector<pair<int, int>> q;
    q.push_back(origin);

    for (auto& dot : rest) {
        if (q.size() < 2) q.push_back(dot);
        else {
            while (q.size() >= 2) {
                int dx1 = q[q.size() - 1].first - q[q.size() - 2].first;
                int dy1 = q[q.size() - 1].second - q[q.size() - 2].second;
                int dx2 = dot.first - q[q.size() - 1].first;
                int dy2 = dot.second - q[q.size() - 1].second;

                if (1LL * dx1 * dy2 - 1LL * dy1 * dx2 > 0) break;
                q.pop_back();
            }
            q.push_back(dot);
        }
    }

    cout << q.size() << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
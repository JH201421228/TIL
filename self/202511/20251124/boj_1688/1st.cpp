#include <iostream>
using namespace std;


int N;
pair<long long, long long> dots[10'001];


long long ccw(pair<long long, long long> p1, pair<long long, long long> p2, pair<long long, long long> p3) {
    return (p3.first - p1.first) * (p2.second - p3.second) - (p3.second - p1.second) * (p2.first - p3.first);
}


int is_cross_line(pair<long long, long long> p) {
    int res = 0;

    for (int idx = 0; idx < N; ++idx) {
        pair<long long, long long> p1 = dots[idx];
        pair<long long, long long> p2 = dots[(idx+1) % N];

        if (p1.second < p2.second) swap(p1, p2);

        if (ccw(p1, p2, p) == 0) {
            if (p.first >= min(p1.first, p2.first) &&
                p.first <= max(p1.first, p2.first) &&
                p.second >= min(p1.second, p2.second) &&
                p.second <= max(p1.second, p2.second)) {
                return 1;
            }
        }

        if (p.first > max(p1.first, p2.first)) continue;

        if (p.second >= max(p1.second, p2.second)) continue;

        if (p.second < min(p1.second, p2.second)) continue;

        if (ccw(p1, p2, p) > 0) ++res;

    }

    return res % 2;
}


void solve() {
    cin >> N;

    for (int idx = 0; idx < N; ++idx) {
        cin >> dots[idx].first >> dots[idx].second;
    }
    
    for (int idx = 0; idx < 3; ++idx) {
        pair<long long, long long> temp;
        cin >> temp.first >> temp.second;

        if (is_cross_line(temp)) {
            cout << 1 << '\n';
        }
        else {
            cout << 0 << '\n';
        }
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
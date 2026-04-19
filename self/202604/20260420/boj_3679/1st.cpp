#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

struct Point {
    long long x, y;
    int idx;
};

long long ccw(const Point& d1, const Point& d2, const Point& d3) {
    return (d2.x - d1.x) * (d3.y - d1.y) - (d2.y - d1.y) * (d3.x - d1.x);
}

void solve() {
    int N;
    cin >> N;

    vector<Point> dots;
    dots.reserve(N);

    for (int i = 0; i < N; ++i) {
        long long x, y;
        cin >> x >> y;
        dots.push_back({x, y, i});
    }

    // y 오름차순, 같으면 x 오름차순
    sort(dots.begin(), dots.end(), [](const Point& a, const Point& b) {
        if (a.y == b.y) return a.x < b.x;
        return a.y < b.y;
    });

    Point origin = dots[0];

    vector<Point> rest(dots.begin() + 1, dots.end());

    // origin 기준 각도 정렬, 같으면 거리순 정렬
    sort(rest.begin(), rest.end(), [&](const Point& a, const Point& b) {
        double angleA = atan2((double)(a.y - origin.y), (double)(a.x - origin.x));
        double angleB = atan2((double)(b.y - origin.y), (double)(b.x - origin.x));

        if (angleA == angleB) {
            long long distA = (a.x - origin.x) * (a.x - origin.x)
                            + (a.y - origin.y) * (a.y - origin.y);
            long long distB = (b.x - origin.x) * (b.x - origin.x)
                            + (b.y - origin.y) * (b.y - origin.y);
            return distA < distB;
        }

        return angleA < angleB;
    });

    int idx = (int)rest.size() - 1;
    while (idx > 0 && ccw(origin, rest[idx], rest[idx - 1]) == 0) {
        --idx;
    }

    reverse(rest.begin() + idx, rest.end());

    cout << origin.idx;
    for (const auto& p : rest) {
        cout << ' ' << p.idx;
    }
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; cin >> T;
    while (T--) solve();
    return 0;
}
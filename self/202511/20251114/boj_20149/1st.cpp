#include <iostream>
#include <vector>
using namespace std;

using ld = long double;

ld lines[2][4];
vector<pair<ld, ld>> ans;


bool in_ans(pair<ld, ld> p) {
    for (auto& q : ans) {
        if (q == p) return true;
    }

    return false;
}


bool same_dot(pair<ld, ld> d1, pair<ld, ld> d2) {
    if (d1.first == d2.first && d1.second == d2.second) return true;

    return false;
}


void is_same_dot() {
    pair<ld, ld> d1 = {lines[0][0], lines[0][1]};
    pair<ld, ld> d2 = {lines[0][2], lines[0][3]};
    pair<ld, ld> d3 = {lines[1][0], lines[1][1]};
    pair<ld, ld> d4 = {lines[1][2], lines[1][3]};

    if (same_dot(d1, d3) && !in_ans(d1)) ans.emplace_back(d1);
    if (same_dot(d1, d4) && !in_ans(d1)) ans.emplace_back(d1);
    if (same_dot(d2, d3) && !in_ans(d2)) ans.emplace_back(d2);
    if (same_dot(d2, d4) && !in_ans(d2)) ans.emplace_back(d2);

    return;
}


bool online(pair<ld, ld> d1, pair<ld, ld> d2, pair<ld, ld> d3) {
    if (d3.first >= min(d1.first, d2.first) &&
        d3.first <= max(d1.first, d2.first) && 
        d3.second >= min(d1.second, d2.second) &&
        d3.second <= max(d1.second, d2.second)) {
        
        if ((d1.second - d3.second) * (d2.first - d3.first) == 
            (d1.first - d3.first) * (d2.second - d3.second)) {
            return true;
        }
    }

    return false;
}


void is_online() {
    pair<ld, ld> d1 = {lines[0][0], lines[0][1]};
    pair<ld, ld> d2 = {lines[0][2], lines[0][3]};
    pair<ld, ld> d3 = {lines[1][0], lines[1][1]};
    pair<ld, ld> d4 = {lines[1][2], lines[1][3]};

    if (online(d1, d2, d3) && !in_ans(d3)) ans.emplace_back(d3);
    if (online(d1, d2, d4) && !in_ans(d4)) ans.emplace_back(d4);
    if (online(d3, d4, d1) && !in_ans(d1)) ans.emplace_back(d1);
    if (online(d3, d4, d2) && !in_ans(d2)) ans.emplace_back(d2);

    return;
}


void ccw() {
    pair<ld, ld> d1 = {lines[0][0], lines[0][1]};
    pair<ld, ld> d2 = {lines[0][2], lines[0][3]};
    pair<ld, ld> d3 = {lines[1][0], lines[1][1]};
    pair<ld, ld> d4 = {lines[1][2], lines[1][3]};

    ld expr1 = ((d3.first - d2.first) * (d2.second - d1.second) 
                - (d2.first - d1.first) * (d3.second - d2.second));
    ld expr2 = ((d4.first - d2.first) * (d2.second - d1.second) 
                - (d2.first - d1.first) * (d4.second - d2.second));
    ld expr3 = ((d1.first - d3.first) * (d3.second - d4.second) 
                - (d3.first - d4.first) * (d1.second - d3.second));
    ld expr4 = ((d2.first - d3.first) * (d3.second - d4.second) 
                - (d3.first - d4.first) * (d2.second - d3.second));

    if (expr1 * expr2 < 0 && expr3 * expr4 < 0) {
        cout << 1 << '\n';

        ld x, y;

        if (d1.first == d2.first) {
            x = d1.first;
            y = ((d4.second - d3.second) * (x - d3.first))
                 / (d4.first - d3.first) + d3.second;
        }
        else if (d3.first == d4.first) {
            x = d3.first;
            y = ((d2.second - d1.second) * (x - d1.first))
                 / (d2.first - d1.first) + d1.second;
        }
        else {
            ld alpha1 = (d2.second - d1.second) / (d2.first - d1.first);
            ld alpha2 = (d4.second - d3.second) / (d4.first - d3.first);

            x = (alpha1 * d1.first - alpha2 * d3.first - d1.second + d3.second)
                 / (alpha1 - alpha2);
            y = alpha1 * (x - d1.first) + d1.second;
        }

        cout << x << ' ' << y << '\n';

        return;
    }

    cout << 0 << '\n';

    return;
}


void cross_check() {
    is_same_dot();
    is_online();

    if (ans.size() > 1) {
        cout << 1 << '\n';
        return;
    }
    else if (ans.size() == 1) {
        cout << 1 << '\n';
        cout << ans[0].first << ' ' << ans[0].second << '\n';
        return;
    }

    ccw();

    return;
}


void solve() {
    cross_check();

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 4; ++j) cin >> lines[i][j];
    }

    solve();

    return 0;
}
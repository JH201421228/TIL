#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int N;
vector<pair<int, int>> A, B;
long long ans = 0, rest = 0;


void solve() {
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int a, b; cin >> a >> b;

        if (a < b) A.emplace_back(a, b);
        else B.emplace_back(-b, -a);
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    for (auto& p : A) {
        if (rest < p.first) {
            ans += (p.first-rest);
            rest = p.first;
        }

        rest += (p.second - p.first);
    }

    for (auto& p : B) {
        long long a = -p.second, b = -p.first;

        if (rest < a) {
            ans += (a-rest);
            rest = a;
        }

        rest += (b-a);
    }

    cout << ans << '\n';

    return;
}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
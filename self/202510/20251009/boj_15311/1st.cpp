#include <iostream>
using namespace std;


void solve() {
    string ans = "1999\n";

    for (int i = 0; i < 999; ++i) ans += "1 ";
    for (int i = 0; i < 1000; ++i) ans += "1000  ";

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
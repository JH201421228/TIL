#include <iostream>
#include <stack>
using namespace std;


int N;
string temp[1'000];
stack<string> S1, S2;


void solve() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> temp[i];
    }

    for (int idx = 0; idx < N; ++idx) {
        string t = temp[idx];

        if (S1.empty()) S1.push(t);
        else {
            if (S1.top() + t >= t + S1.top()) {
                if (S2.empty()) S2.push(t);
                else {
                    if (t + S2.top() < S2.top() + t) {
                        while (!S2.empty() && t + S2.top() < S2.top() + t) {
                            S1.push(S2.top());
                            S2.pop();
                        }
                    }
                    S2.push(t);
                }
            }
            else {
                while (!S1.empty() && S1.top() + t < t + S1.top()) {
                    S2.push(S1.top());
                    S1.pop();
                }
                S1.push(t);
            }
        }
    }

    string ans = "";

    while (!S1.empty()) {
        S2.push(S1.top());
        S1.pop();
    }

    while (!S2.empty()) {
        ans += S2.top();
        S2.pop();
    }

    if (ans[0] == '0') {
        cout << 0 << '\n';
        return;
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
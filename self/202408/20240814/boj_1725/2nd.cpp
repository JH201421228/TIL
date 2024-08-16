#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;


vector<long long> H;
stack<long long> S;

long long area(int n) {
    long long ans = 0;

    for (int idx = 1; idx < n+2; ++idx) {
        while (!S.empty() && H[S.top()] > H[idx]) {
            int i = S.top();
            S.pop();

            ans = max(ans, (long long) H[i]*(idx-S.top()-1));
        }

        S.push(idx);
    }

    return ans;
}


int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    H.resize(N+2);
    S.push(0);

    for (int idx = 1; idx < N+1; ++idx) {
        cin >> H[idx];
    }

    cout << area(N) << '\n';

    return 0;
}
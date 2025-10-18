#include <iostream>
#include <stack>
using namespace std;


int N, cur, cur_cnt;
long long ans = 0;
int arr[500'000];
stack<pair<int, int>> S;


void solve() {
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> arr[i];

    for (int idx = 0; idx < N; ++idx) {
        if (!S.empty()) {
            ++ans;
            cur = arr[idx];
            cur_cnt = 1;

            while (!S.empty() && S.top().first <= cur) {
                pair<int, int> temp = S.top(); S.pop();

                if (!S.empty()) {
                    ans += temp.second;
                }
                else {
                    ans += temp.second-1;
                }

                if (temp.first == cur) {
                    cur_cnt += temp.second;
                    break;
                }
            }

            S.push({cur, cur_cnt});
        }
        else {
            S.push({arr[idx], 1});
        }
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
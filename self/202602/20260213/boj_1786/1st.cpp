#include <iostream>
#include <vector>
using namespace std;


string T, P;


void solve() {
    getline(cin, T);
    getline(cin, P);

    int p_len = P.size();
    int preprocess[p_len] = {0};
    

    int stack_n = 0;

    for (int idx = 1; idx < p_len; ++idx) {
        while (stack_n && P[stack_n] != P[idx]) {
            stack_n = preprocess[stack_n-1];
        }

        if (P[stack_n] == P[idx]) {
            ++stack_n;
            preprocess[idx] = stack_n;
        }
    }

    int cnt = 0;
    vector<int> ans_list;
    int cur = 0;

    for (int idx = 0; idx < T.size(); ++idx) {
        while (cur && T[idx] != P[cur]) {
            cur = preprocess[cur-1];
        }

        if (T[idx] == P[cur]) {
            if (cur == p_len-1) {
                ++cnt;
                ans_list.emplace_back(idx-p_len+2);
                cur = preprocess[cur];
            }
            else ++cur;
        }
    }

    cout << cnt << '\n';
    for (int idx = 0; idx < ans_list.size(); ++idx) cout << ans_list[idx] << ' ';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
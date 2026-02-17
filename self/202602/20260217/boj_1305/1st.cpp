#include <iostream>
#include <string.h>
using namespace std;


int L;
string S;


void solve() {
    cin >> L >> S;

    int preprocess[L];
    memset(preprocess, 0, sizeof(int)*L);
    int stack_n = 0;

    for (int idx = 1; idx < L; ++idx) {
        while (stack_n && S[stack_n] != S[idx]) {
            stack_n = preprocess[stack_n-1];
        }

        if (S[stack_n] == S[idx]) {
            ++stack_n;
            preprocess[idx] = stack_n;
        }
    }

    cout << L - preprocess[L-1]  << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
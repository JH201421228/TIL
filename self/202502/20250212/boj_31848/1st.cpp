#include <iostream>
#include <vector>
using namespace std;


int N, Q, H[100000], cnt = 1;
vector<int> res, order;

void sieve(int l) {
    res.emplace_back(H[0]);
    order.emplace_back(0);
    int cur = H[0];

    for (int idx = 0; idx < l; ++idx) {
        if (H[idx] > cur) {
            cur = H[idx];
            res.emplace_back(H[idx]);
            order.emplace_back(idx);
            ++cnt;
        }
    }

    return;
}

int binary_search(int n) {
    int s = 0, e = cnt-1;

    while (s <= e) {
        int mid = (s+e) >> 1;

        if (res[mid] < n) {
            ++s;
        }
        else {
            --e;
        }
    }

    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> H[i];
        H[i] += i;
    }

    cin >> Q;

    sieve(N);

    for (int i = 0; i < Q; ++i) {
        int tmp; cin >> tmp;
        cout << order[binary_search(tmp)] + 1 << ' ';
    }

    return 0;
}
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <array>
using namespace std;

int T;
int N;
int idx = 0;
long long cur_s, cur_c, cur_t;

long long K;
long long cur_d;
long long nxt_d;
long long gap;
long long ans;

vector<array<long long, 3>> arr;

priority_queue<array<long long ,3>> pq;


long long solve() {
    cin >> N >> K;

    arr.clear();
    for (int i = 0; i < N; ++i) {
        long long c, t, s; cin >> c >> t >> s;
        arr.emplace_back(array<long long, 3>{c, t, s});
    }

    sort(arr.begin(), arr.end(), [](auto const& a, auto const& b) {
        return a[1] > b[1];
    });

    cur_d = K;
    idx = 0;
    while (!pq.empty()) pq.pop();

    cur_s = 0;
    cur_c = 0;
    cur_t = 0;

    ans = 0;

    while (cur_d > 0) {
        while (idx < N && arr[idx][1] >= cur_d) {
            long long c = arr[idx][0];
            long long t = arr[idx][1];
            long long s = arr[idx][2];
            
            ++idx;

            pq.push({s, c, t});
        }

        if (idx < N) nxt_d = arr[idx][1];
        else nxt_d = 0;

        gap = cur_d - nxt_d;


        while (gap > 0 && !pq.empty()) {
            array<long long, 3> temp = pq.top(); pq.pop();

            long long amount = min(gap, temp[1]);

            ans += amount * temp[0];
            gap -= amount;
            temp[1] -= amount;

            if (temp[1] > 0) pq.push(temp);
        }

        cur_d = nxt_d;
    }

    return ans;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i+1 << ": " << solve() << '\n';
    }

    return 0;
}
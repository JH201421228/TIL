#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long long ans = 0;

vector<long long> H;

long long area(int s, int e) {
    if (s == e) {
        return H[s];
    }

    int mid = (s+e) / 2;
    int l = mid - 1;
    int r = mid + 1;
    long long rec = H[mid];
    long long h = H[mid];

    while (s <= l || r <= e) {
        if (s > l) {
            h = min(h, H[r++]);
        }
        else if (r > e) {
            h = min(h, H[l--]);
        }
        else if (H[l] >= H[r]) {
            h = min(h, H[l--]);
        }
        else if (H[l] < H[r]) {
            h = min(h, H[r++]);
        }

        rec = max(rec, (long long) h*(r-l-1)); 
    }

    return max(rec, max(area(s, mid), area(mid+1, e)));
}


int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    H.resize(N);

    for (int idx = 0; idx < N; ++idx) {
        cin >> H[idx];
    }

    cout << area(0, N-1) << '\n';

    return 0;
}
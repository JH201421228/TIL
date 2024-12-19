#include <iostream>
#include <vector>
using namespace std;


int N, M;
long long arr[100001];
vector<long long> T[400001];
int last_ans = 0;

vector<long long> merge(const vector<long long>& X, const vector<long long>& Y) {
    vector<long long> res;
    int i = 0, j = 0, x = X.size(), y = Y.size();

    while (i < x && j < y) {
        if (X[i] > Y[j]) {
            res.emplace_back(Y[j++]);
        }
        else {
            res.emplace_back(X[i++]);
        }
    }

    while (i < x) res.emplace_back(X[i++]);
    while (j < y) res.emplace_back(Y[j++]);

    return res;
}

vector<long long> I(int s, int e, int idx) {
    if (s == e) {
        T[idx].emplace_back(arr[s]);
        return T[idx];
    }

    int mid = (s + e) >> 1;

    T[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1));
    return T[idx];
}

int count(vector<long long>& X, long long v) {
    int s = 0, e = X.size()-1;

    while (s <= e) {
        int mid = (s + e) >> 1;

        if (X[mid] > v) {
            e = mid-1;
        }
        else {
            s = mid+1;
        }
    }

    return X.size()-e-1;
}

int S(int s, int e, int idx, int l, int r, long long v) {
    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return count(T[idx], v);
    }

    int mid = (s + e) >> 1;

    return S(s, mid, idx<<1, l, r, v) + S(mid+1, e, idx<<1|1, l, r, v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
    }

    cin >> M;

    I(1, N, 1);

    for (int i = 0; i < M; ++i) {
        int a, b; long long c; cin >> a >> b >> c;
        a ^= last_ans;
        b ^= last_ans;
        c ^= last_ans;
        
        last_ans = S(1, N, 1, a, b, c);
        cout << last_ans << '\n';
    }

    return 0;
}
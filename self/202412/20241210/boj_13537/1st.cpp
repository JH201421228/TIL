#include <iostream>
#include <vector>
using namespace std;

int N, M;
long long arr[100001];
vector<long long> tree[400001];

vector<long long> merge(const vector<long long>& X, const vector<long long>& Y) {
    vector<long long> res;
    int i = 0, j = 0, x = X.size(), y = Y.size();

    while (i < x && j < y) {
        if (X[i] >= Y[j]) {
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
        tree[idx] = {arr[s]};
        return tree[idx];
    }

    int mid = (s+e) >> 1;

    tree[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1));
    return tree[idx];
}

int count(vector<long long>& X, long long k) {
    int s = 0; int e = X.size()-1;

    while (s <= e) {
        int mid = (s+e) >> 1;

        if (X[mid] <= k) {
            s = mid+1;
        }
        else {
            e = mid-1;
        }
    }

    return X.size()-s;
}

int S(int s, int e, int idx, int l, int r, long long k) {
    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return count(tree[idx], k);
    }

    int mid = (s+e) >> 1;

    return S(s, mid, idx<<1, l, r, k) + S(mid+1, e, idx<<1|1, l, r, k);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 1; i < N+1; ++i) {
        cin >> arr[i];
    }

    I(1, N, 1);

    cin >> M;

    for (int i = 0; i < M; ++i) {
        int a, b; long long c; cin >> a >> b >> c;
        cout << S(1, N, 1, a, b, c) << '\n';
    }

    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long> arr;
vector<long long> tree;
vector<long long> lazy;

long long I(int s, int e, int tree_idx)
{
    if (s == e)
    {
        tree[tree_idx] = arr[s];
        return arr[s];
    }

    int mid = (s + e) / 2;
    tree[tree_idx] = I(s, mid, tree_idx * 2) + I(mid + 1, e, tree_idx * 2 + 1);
    return tree[tree_idx];
}

void UU(int s, int e, int tree_idx)
{
    if (lazy[tree_idx]) {
        tree[tree_idx] += (e-s+1)*lazy[tree_idx];
        if (s != e) {
            lazy[tree_idx*2] += lazy[tree_idx];
            lazy[tree_idx*2+1] += lazy[tree_idx];
        }
        lazy[tree_idx] = 0;
    }
}

long long S(int s, int e, int tree_idx, int l, int r)
{
    UU(s, e, tree_idx);

    if (e < l || s > r)
    {
        return 0;
    }

    if (s >= l && e <= r)
    {
        return tree[tree_idx];
    }

    int mid = (s + e) / 2;
    return S(s, mid, tree_idx * 2, l, r) + S(mid + 1, e, tree_idx * 2 + 1, l, r);
}

void U(int s, int e, int tree_idx, int l, int r, long long c)
{
    UU(s, e, tree_idx);

    if (e < l || s > r)
    {
        return;
    }

    if (s >= l && e <= r)
    {
        tree[tree_idx] += (e - s + 1) * c;
        if (s != e)
        {
            lazy[tree_idx * 2] += c;
            lazy[tree_idx * 2 + 1] += c;
        }
        return;
    }

    int mid = (s+e) / 2;
    U(s, mid, tree_idx*2, l, r, c);
    U(mid+1, e, tree_idx*2+1, l, r, c);
    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M, K;
    cin >> N >> M >> K;

    arr.resize(N+1);
    tree.resize(4*N+1);
    lazy.resize(4*N+1);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
    }

    I(1, N, 1);

    for (int i = 0; i < M+K; ++i) {
        int a;
        cin >> a;
        if (a == 1) {
            int b, c;
            long long d;
            cin >> b >> c >> d;
            U(1, N, 1, b, c, d);
        }
        else {
            int b, c;
            cin >> b >> c;
            cout << S(1, N, 1, b, c) << '\n';
        }
    }

    return 0;
}
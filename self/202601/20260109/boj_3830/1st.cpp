#include <iostream>
#include <unordered_set>
using namespace std;

int N, M;
int arr[100'001];
long long state[100'001];
unordered_set<int> sets[100'001];


int find(int idx) {
    int root = idx;

    while (root != arr[root]) root = arr[root];

    while (idx != root) {
        int p = arr[idx];
        arr[idx] = root;
        idx = p;
    }

    return root;
}


void union_find(int a, int b, int w) {
    int pa = find(a);
    int pb = find(b);

    long long fix = state[a] - state[b];

    if (sets[pa].size() < sets[pb].size()) {
        swap(sets[pa], sets[pb]);
        w *= -1;
        fix *= -1;
    }

    arr[pb] = pa;

    for (auto& v : sets[pb]) {
        sets[pa].insert(v);
        state[v] += w+fix;
    }

    sets[pb].clear();

    return;
}


void solve(int N, int M) {
    for (int i = 0; i < N+1; ++i) {
        arr[i] = i;
        state[i] = 0;
        sets[i].clear();
        sets[i].insert(i);
    }

    for (int i = 0; i < M; ++i) {
        string sign; cin >> sign;
        int a, b; cin >> a >> b;

        int pa = find(a);
        int pb = find(b);

        if (sign == "!") {
            int w; cin >> w;

            if (pa != pb) union_find(a, b, w);
        }
        else {
            if (pa != pb) cout << "UNKNOWN" << '\n';
            else cout << state[b] - state[a] << '\n';
        }
    }

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (1) {
        cin >> N >> M;
        if (!N && !M) break;

        solve(N, M);
    }

    return 0;
}
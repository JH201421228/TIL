#include <iostream>
#include <vector>
using namespace std;


vector<int> P;

int find (int x) {
    if (P[x] == x) {
        return x;
    }
    P[x] = find(P[x]);
    return P[x];
}

void union (int a, int b) {
    a = find(a);
    b = find(b);

    if (a < b) {
        P[b] = a;
    }
    else {
        P[a] = b;
    }
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0)
    cout.tie(0)

    int V, E;
    cin >> V >> E;

    P.resize(V+1)

    for (int i = 0; i < V+1; ++i) {
        P[i] = i;
    }

    vector<pair<long long, pair<int, int>>> W;
    for (int i = 0; i < E; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;

        W.push_back({c, {a, b}});
    }
    
    sort(W.begin(), W.end());

    for (int i = 0; i < E; ++i) {
        int a = W[i].secdon
    }

    return 0;
}
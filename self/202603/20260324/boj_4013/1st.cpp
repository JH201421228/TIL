#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;


int N, M, S, P, o = 0, group_n = 1;
int V[500'001];
int F[500'001];
vector<int> G[500'001];
stack<int> Stack;
queue<int> Queue;

int cash[500'001];
int restaurant[500'001];

int group_cash[500'001];
int group_restaurant[500'001];
int group_visit[500'001];
int indegree[500'001];
int dp[500'001];

vector<int> group_graph[500'001];
stack<int> group_stack;

int scc(int n) {
    ++o;
    int p = o;
    V[n] = o;
    Stack.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) p = min(p, scc(x));
        else if (!F[x]) p = min(p, V[x]);
    }

    if (p == V[n]) {
        while (!Stack.empty()) {
            int c = Stack.top(); Stack.pop();
            F[c] = group_n;
            if (c == n) break;
        }
        ++group_n;
    }

    return p;
}


void solve() {
    cin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
    }

    for (int idx = 0; idx < N; ++idx) cin >> cash[idx+1];

    cin >> S >> P;

    for (int i = 0; i < P; ++i) {
        int idx; cin >> idx;
        restaurant[idx] = 1;
    }

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    for (int n = 1; n < N+1; ++n) {
        int group = F[n];
        group_cash[group] += cash[n];
        if (restaurant[n]) group_restaurant[group] = 1;

        for (auto& x : G[n]) {
            if (group != F[x]) group_graph[group].emplace_back(F[x]);
        }
    }

    S = F[S];
    group_visit[S] = 1;
    group_stack.push(S);

    while (!group_stack.empty()) {
        int n = group_stack.top(); group_stack.pop();
        for (auto& x : group_graph[n]) {
            if (!group_visit[x]) {
                group_visit[x] = 1;
                group_stack.push(x);
            }
        }
    }

    for (int n = 1; n < group_n; ++n) {
        if (!group_visit[n]) continue;
        
        for (auto& x : group_graph[n]) {
            if (group_visit[x]) ++indegree[x];
        }
    }

    dp[S] = group_cash[S];

    Queue.push(S);

    while (!Queue.empty()) {
        int n = Queue.front(); Queue.pop();

        for (auto& x : group_graph[n]) {
            dp[x] = max(dp[x], dp[n] + group_cash[x]);

            --indegree[x];

            if (!indegree[x]) Queue.push(x);
        }
    }

    int ans = 0;

    for (int idx = 1; idx < group_n; ++idx) {
        if (group_restaurant[idx]) ans = max(ans, dp[idx]);
    }

    cout << ans << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
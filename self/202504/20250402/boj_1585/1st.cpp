#include <iostream>
#include <vector>
#include <queue>
using namespace std;


int N, T, FF, time_in[50], time_out[50], src = 101, sink = 102, D[103][103], DD[103][103], F[103][103], C[103][103], pre[103], dist[103], checker[103], ans;
vector<int> G[103];
bool isPossible;


int fee(int t, int s, int f) {
    if (t > s) {
        if ((t-s)*(t-s) > f) {
            return f;
        }
        else {
            return (t-s)*(t-s);
        }
    }
    else {
        return 0;
    }
}


void solve() {
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> time_in[i];
    for (int i = 0; i < N; ++i) cin >> time_out[i];
    cin >> T >> FF;

    for (int i = 0; i < N; ++i) {
        int u = i+1;
        G[src].emplace_back(u); G[u].emplace_back(src); C[src][u] = 1;

        G[u+N].emplace_back(sink); G[sink].emplace_back(u+N); C[u+N][sink] = 1;

        for (int j = 0; j < N; ++j) {
            int v = N+j+1;

            if (time_out[j] - time_in[i] > 0) {
                int f = fee(T, time_out[j] - time_in[i], FF);
                G[u].emplace_back(v); G[v].emplace_back(u); C[u][v] = 1; D[u][v] = f; D[v][u] = -f;
            }
        }
    }

    isPossible = true; ans = 0;
    for (int i = 0; i < N; ++i) {
        fill(pre, pre+103, -1); fill(dist, dist+103, 1e9); fill(checker, checker+103, 0);
        queue<int> q; q.push(src); checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop();
            checker[n] = 0;

            for (int x : G[n]) {
                if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                    dist[x] = dist[n] + D[n][x]; pre[x] = n;

                    if (!checker[x]) {
                        checker[x] = 1;
                        q.push(x);
                    }
                }
            }
        }

        if (pre[sink] == -1) {
            isPossible = !isPossible;
            break;
        }

        for (int n = sink; n != src; n = pre[n]) {
            ++F[pre[n]][n]; --F[n][pre[n]]; ans += D[pre[n]][n];
        }
    }

    if (isPossible) {
        cout << ans << ' '; ans = 0;
    }
    else {
        cout << -1 << '\n'; exit(0);
    }

    for (int i = 0; i < 103; ++i) {
        for (int j = 0; j < 103; ++j) {
            F[i][j] = 0;
        }
    }

    for (int i = 0; i < N; ++i) {
        fill(pre, pre+103, -1); fill(dist, dist+103, 1e9); fill(checker, checker+103, 0);
        queue<int> q; q.push(src); checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop(); checker[n] = 0;

            for (int x : G[n]) {
                if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[x][n]) {
                    dist[x] = dist[n] + D[x][n]; pre[x] = n;
                    
                    if (!checker[x]) {
                        checker[x] = 1; q.push(x);
                    }
                }
            }
        }

        for (int n = sink; n != src; n = pre[n]) {
            ++F[pre[n]][n]; --F[n][pre[n]]; ans += D[n][pre[n]];
        }
    }

    cout << -ans << '\n';
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
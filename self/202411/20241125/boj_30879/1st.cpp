#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> G[200001];
vector<pair<int, int>> temp;
vector<int> num;
int cnt = 0;
vector<int> S;
int V[200001];
int F[200001];
int O = 0;
int grn = 0;

int scc(int n) {
    int p = V[n] = ++O;
    S.emplace_back(n);

    for (auto& x : G[n]) {
        if (V[x] == 0) {
            p = min(p, scc(x));
        }
        else if (F[x] == 0) {
            p = min(p, V[x]);
        }
    }

    if (p == V[n]) {
        ++grn;
        while (true) {
            int o = S.back();
            S.pop_back();
            F[o] = grn;

            if (o == n) {
                break;
            }
        }
    }

    return p;
}

int main () {
    ios::sync_with_stdio(false);

    cin >> N;

    temp.emplace_back(make_pair(0, 0));
    num.emplace_back(0);
    for (int i = 0; i < N; ++i) {
        int a; cin >> a;

        if (a == 1) {
            int b, c; cin >> b >> c;
            temp.emplace_back(make_pair(b, c));
            ++cnt;
        }
        else {
            num.emplace_back(cnt);
        }
    }

    int s = 1, e = num.size()-1;
    while (s <= e) {
        int mid = (s+e) >> 1;
        int is_possible = true;
        
        O = 0;
        grn = 0;
        S.clear();
        for (int i = 0; i < 200001; ++i) {
            G[i].clear();
            V[i] = 0;
            F[i] = 0;
        }

        for (int i = 1; i < num[mid]+1; ++i) {
            int a = temp[i].first, b = temp[i].second;

            if (a < 0) {
                if (b < 0) {
                    G[-a].emplace_back(200001+b);
                    G[-b].emplace_back(200001+a);
                }
                else {
                    G[-a].emplace_back(b);
                    G[200001-b].emplace_back(200001+a);
                }
            }
            else {
                if (b < 0) {
                    G[200001-a].emplace_back(200001+b);
                    G[-b].emplace_back(a);
                }
                else {
                    G[200001-a].emplace_back(b);
                    G[200001-b].emplace_back(a);
                }
            }
        }

        for (int i = 1; i < 200001; ++i) {
            if (V[i] == 0) {
                scc(i);
            }
        }

        for (int i = 1; i < 100001; ++i) {
            if (F[i] == F[200001-i]) {
                e = mid-1;
                is_possible = false;
                break;
            }
        }
        if (is_possible) {
            s = mid+1;
        }
    }

    for (int i = 0; i < e; ++i) {
        cout << "YES DINNER" << '\n';
    }

    for (int i = 0; i < num.size()-e-1; ++i) {
        cout << "NO DINNER" << '\n';
    }

    return 0;
}
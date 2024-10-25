#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int R, C;
char M[50][50];
int MM[50][50];
char c;
bool check = false;
vector<string> name;
vector<pair<int, int>> cities;
string temp;
int cities_num;
int names_num;
int F[2501] = {};
int V[2501] = {};
int delta[8][2] = {{1, 1}, {1, 0}, {0, 1}, {1, -1}, {-1, 1}, {-1, 0}, {0, -1}, {-1, -1}};
vector<vector<int>> G;

bool B(int n) {
    for (auto& x : G[n]) {
        if (V[x]) {
            continue;
        }
        V[x] = 1;

        if (!F[x] || B(F[x])) {
            F[x] = n;
            return true;
        }
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> R >> C;

    name.emplace_back("");
    cities.emplace_back(make_pair(0, 0));

    for (int i = 0; i < R; ++i) {

        if (check) {
            check = false;
            name.emplace_back(temp);
            temp = "";
        }

        for (int j = 0; j < C; ++j) {
            cin >> c;
            M[i][j] = c;

            if (c == '.') {
                if (check) {
                    check = false;
                    name.emplace_back(temp);
                    temp = "";
                }
            }

            else if (c == 'x') {
                if (check) {
                    check = false;
                    name.emplace_back(temp);
                    temp = "";
                }
                cities.emplace_back(make_pair(i, j));
            }

            else {
                if (!check) {
                    check = true;
                    ++names_num;
                }
                temp += c;
                MM[i][j] = names_num;
            }
        }
    }

    if(temp.compare("")) {
        name.emplace_back(temp);
    }

    cities_num = cities.size()-1;

    G.resize(cities_num+1);

    for (int i = 1; i < cities_num+1; ++i) {
        for (int j = 0; j < 8; ++j) {
            int x = cities[i].first + delta[j][0];
            int y = cities[i].second + delta[j][1];

            if (x >= 0 && x < R && y >= 0 && y < C && MM[x][y] != 0 && MM[x][y] != 0 && (find(G[i].begin(), G[i].end(), MM[x][y]) == G[i].end())) {
                G[i].emplace_back(MM[x][y]);
            }
        }
    }

    for (int i = 1; i < cities_num+1; ++i) {
        for (int j = 1; j < names_num+1; ++j) {
            V[j] = 0;
        }

        B(i);
    }

    for (int i = 1; i < names_num+1; ++i) {
        cout << cities[F[i]].first + 1 << ' ' << cities[F[i]].second + 1 << ' ' << name[i] << '\n';
    }

    return 0;
}
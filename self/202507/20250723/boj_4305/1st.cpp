#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int N, O;
int V[27], F[27], U[27];
stack<int> S;
vector<int> G[27];
vector<vector<char>> result;

int scc(int n)
{
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto &x : G[n])
    {
        if (!V[x])
        {
            p = min(p, scc(x));
        }
        else if (!F[x])
        {
            p = min(p, V[x]);
        }
    }

    if (p == V[n])
    {
        vector<char> temp;

        while (!S.empty())
        {
            int o = S.top();
            S.pop();
            F[o] = 1;
            temp.emplace_back((char)(o + 64));

            if (o == n)
            {
                sort(temp.begin(), temp.end());
                result.emplace_back(temp);
                break;
            }
        }
    }

    return p;
}

void solve(int N)
{
    O = 0;
    fill(V, V + 27, 0);
    fill(F, F + 27, 0);
    fill(U, U + 27, 0);
    for (int idx = 0; idx < 27; ++idx)
        G[idx].clear();
    result.clear();

    for (int i = 0; i < N; ++i)
    {
        int choices[6];
        for (int idx = 0; idx < 6; ++idx)
        {
            char c;
            cin >> c;
            choices[idx] = (int)c - 64;
        }

        for (int idx = 0; idx < 5; ++idx)
        {
            G[choices[idx]].emplace_back(choices[5]);
            U[choices[idx]] = 1;
        }
    }

    for (int n = 1; n < 27; ++n)
    {
        if (!V[n] && U[n])
        {
            scc(n);
        }
    }

    sort(result.begin(), result.end(), [](const vector<char> &a, const vector<char> &b)
         { return a[0] < b[0]; });

    for (auto &temp : result)
    {
        for (auto &n : temp)
        {
            cout << n << ' ';
        }
        cout << '\n';
    }
    cout << '\n';

    return;
}

void init()
{
    while (true)
    {
        cin >> N;
        if (!N)
            break;

        solve(N);
    }

    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    init();

    return 0;
}
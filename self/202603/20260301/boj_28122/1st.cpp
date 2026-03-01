#include <iostream>
#include <vector>
using namespace std;


struct Node
{
    int cnt = 0;
    int l = -1;
    int r = -1;
};

int N;
vector<Node> trie;


int cal(int idx, int depth, int need) {
    if (depth > 60) return depth - need + trie[idx].cnt;

    if (trie[idx].cnt <= need) return depth;

    if (trie[idx].l == -1) return cal(trie[idx].r, depth+1, need+1);
    else if (trie[idx].r == -1) return cal(trie[idx].l, depth+1, need+1);
    else return max(cal(trie[idx].l, depth+1, max(1, need+1-trie[trie[idx].r].cnt)), cal(trie[idx].r, depth+1, max(1, need+1-trie[trie[idx].l].cnt)));
}


void solve() {
    trie.emplace_back(Node());

    cin >> N;
    for (int i = 0; i < N; ++i) {
        long long cur; cin >> cur;
        int idx = 0;
        
        ++trie[idx].cnt;

        for (int j = 0; j < 61; ++j) {
            if (cur & (1LL<<j)) {
                if (trie[idx].r == -1) {
                    trie[idx].r = trie.size();
                    trie.emplace_back(Node());
                }
                idx = trie[idx].r;
                ++trie[idx].cnt;
            }
            else {
                if (trie[idx].l == -1) {
                    trie[idx].l = trie.size();
                    trie.emplace_back(Node());
                }
                idx = trie[idx].l;
                ++trie[idx].cnt;
            }
        }
    }

    cout << cal(0, 0, 0) << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}
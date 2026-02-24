#include <iostream>
#include <vector>
#include <cmath>
using namespace std;


struct Node {
    int child[26];
    bool isEnd;
    int childCount;

    Node() : isEnd(false), childCount(0) {
        fill(child, child+26, -1);
    }
};

int N;
vector<Node> trie;
vector<string> words;


bool solve() {
    if (!(cin >> N)) return false;

    trie.clear();
    words.clear();

    words.reserve(N);
    trie.emplace_back();

    for (int i = 0; i < N; ++i) {
        string s; cin >> s;
        words.emplace_back(s);

        int cur = 0;
        for (char ch : s) {
            int c = ch - 'a';

            if (trie[cur].child[c] == -1) {
                trie[cur].child[c] = trie.size();
                trie.emplace_back();
                ++trie[cur].childCount;
            }

            cur = trie[cur].child[c];
        }

        trie[cur].isEnd = true;
    }

    int ans = 0;
    for (const auto& word : words) {
        int cnt = 1;
        int cur = 0;

        int first = word[0] - 'a';
        cur = trie[cur].child[first];

        for (int i = 1; i < word.size(); ++i) {
            if (trie[cur].childCount > 1 || trie[cur].isEnd) ++cnt;

            int c = word[i] - 'a';
            cur = trie[cur].child[c];
        }

        ans += cnt;
    }

    cout << fixed << round((float) ans * 100 / N) / 100 << '\n';

    return true;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout.precision(2);

    while (solve());

    return 0;
}
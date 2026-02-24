#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;


int N;
unordered_map<string, vector<string>> trie;
vector<string> words;


bool solve() {
    trie.clear();
    words.clear();

    if(!(cin >> N)) return false;

    trie[""] = {};
    words.reserve(N);

    for (int i = 0; i < N; ++i) {
        string word;
        cin >> word;
        words.emplace_back(word);

        string prev_key = "";
        string cur_key = "";

        for (int idx = 1; idx < word.size()+1; ++idx) {
            cur_key = word.substr(0, idx);

            bool exists = false;
            for (const auto& child : trie[prev_key]) {
                if (child == cur_key) {
                    exists = true;
                    break;
                }
            }
    
            if (!exists) {
                trie[prev_key].emplace_back(cur_key);
                trie[cur_key] = {};
            }
    
            prev_key = cur_key;
        }

        trie[cur_key].emplace_back("");
    }

    int ans = 0;

    for (const auto& word : words) {
        int cnt = 1;

        for (int idx = 0; idx < word.size() - 1; ++idx) {
            string key = word.substr(0, idx+1);

            if (trie[key].size() > 1) ++cnt;
        }

        ans += cnt;
    }

    cout << fixed << (float) (round(ans * 100) / N) / 100 << '\n';

    return true;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cout.precision(2);

    while (1) {
        if (!solve()) break;
    }

    return 0;
}
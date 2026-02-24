const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];
let z = 0;

rl.on("line", l => input.push(l));

rl.on("close", () => {
    class Node {
        child = Array(26).fill(-1)
        isEnd = false;
        childCount = 0;

        constructor() {};
    }


    let N;
    const trie = [];
    const words = [];


    function solve() {
        N = Number(input[z++]);
        while (trie.length > 0) trie.pop();
        while (words.length > 0) words.pop();

        trie.push(new Node());

        for (let i = 0; i < N; ++i) {
            const word = input[z++];
            words.push(word);

            let cur = 0;
            for (const ch of word) {
                let c = ch.charCodeAt(0) - 97;

                if (trie[cur].child[c] === -1) {
                    trie[cur].child[c] = trie.length;
                    trie.push(new Node());
                    ++trie[cur].childCount;
                }

                cur = trie[cur].child[c];
            }

            trie[cur].isEnd = true;
        }

        let ans = 0;

        for (let word of words) {
            let cnt = 1;
            let cur = 0;

            let first = word[0].charCodeAt(0) - 97;
            cur = trie[cur].child[first];

            for (let i = 1; i < word.length; ++i) {
                if (trie[cur].childCount > 1 || trie[cur].isEnd) ++cnt;

                let c = word[i].charCodeAt(0) - 97;
                cur = trie[cur].child[c];
            }

            ans += cnt;
        }

        console.log((Math.round(ans * 100 / N) / 100).toFixed(2));

        return;
    }


    function main() {
        while (z < input.length) solve();

        return;
    }


    main();


    return;
});
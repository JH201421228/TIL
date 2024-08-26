const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];

rl.on('line', (line) => {
    input.push(line);
});

rl.on('close', () => {
    let arr;
    let tree;
    let lazy;

    const I = (s, e, tree_idx) => {
        if (s === e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        const mid = Math.floor((s + e) / 2);

        tree[tree_idx] = I(s, mid, tree_idx * 2) + I(mid + 1, e, tree_idx * 2 + 1);
        return tree[tree_idx];
    };

    const UU = (s, e, tree_idx) => {
        if (lazy[tree_idx] !== 0) {
            tree[tree_idx] += (e - s + 1) * lazy[tree_idx];

            if (s !== e) {
                lazy[tree_idx * 2] += lazy[tree_idx];
                lazy[tree_idx * 2 + 1] += lazy[tree_idx];
            }

            lazy[tree_idx] = 0;
        }
    };

    const S = (s, e, tree_idx, l, r) => {
        UU(s, e, tree_idx);

        if (l > e || r < s) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[tree_idx];
        }

        const mid = Math.floor((s + e) / 2);
        return S(s, mid, tree_idx * 2, l, r) + S(mid + 1, e, tree_idx * 2 + 1, l, r);
    };

    const U = (s, e, tree_idx, l, r, c) => {
        UU(s, e, tree_idx);

        if (l > e || r < s) {
            return;
        }

        if (s >= l && e <= r) {
            tree[tree_idx] += (e - s + 1) * c;
            if (s !== e) {
                lazy[tree_idx * 2] += c;
                lazy[tree_idx * 2 + 1] += c;
            }
            return;
        }

        const mid = Math.floor((s + e) / 2);
        U(s, mid, tree_idx * 2, l, r, c);
        U(mid + 1, e, tree_idx * 2 + 1, l, r, c);
        tree[tree_idx] = tree[tree_idx * 2] + tree[tree_idx * 2 + 1];
    };

    const [N, M, K] = input[0].split(' ').map(Number);

    arr = new Array(N + 1).fill(0);
    tree = new Array(4 * N + 1).fill(0);
    lazy = new Array(4 * N + 1).fill(0);

    for (let i = 0; i < N; ++i) {
        arr[i + 1] = Number(input[i + 1]);
    }

    I(1, N, 1);

    for (let i = 0; i < M + K; ++i) {
        const temp = input[N + 1 + i].split(' ').map(Number);
        const a = temp[0];

        if (a === 1) {
            const b = temp[1];
            const c = temp[2];
            const d = temp[3];

            U(1, N, 1, b, c, d);
        } else {
            const b = temp[1];
            const c = temp[2];

            console.log(S(1, N, 1, b, c));
        }
    }
});

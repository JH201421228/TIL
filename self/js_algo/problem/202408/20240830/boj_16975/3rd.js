const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];

rl.on('line', line => {
    input.push(line);
});

rl.on('close', () => {
    let arr, lazy;

    const lazy_U = (s, e, tree_idx) => {
        if (lazy[tree_idx] !== 0n) {
            if (s === e) {
                arr[s] += lazy[tree_idx];
            } else {
                lazy[tree_idx * 2] += lazy[tree_idx];
                lazy[tree_idx * 2 + 1] += lazy[tree_idx];
            }
            lazy[tree_idx] = 0n;
        }
    };

    const S = (s, e, tree_idx, arr_idx) => {
        lazy_U(s, e, tree_idx);

        if (s === e) {
            if (s === arr_idx) {
                return arr[arr_idx];
            } else {
                return 0n;
            }
        }

        if (arr_idx > e || arr_idx < s) {
            return 0n;
        }

        const mid = Math.floor((s + e) / 2);

        return S(s, mid, tree_idx * 2, arr_idx) + S(mid + 1, e, tree_idx * 2 + 1, arr_idx);
    };

    const U = (s, e, tree_idx, l, r, val) => {
        lazy_U(s, e, tree_idx);

        if (s > r || e < l) {
            return;
        }

        if (s >= l && e <= r) {
            if (s === e) {
                arr[s] += val;
                return;
            } else {
                lazy[tree_idx * 2] += val;
                lazy[tree_idx * 2 + 1] += val;
                return;
            }
        }

        const mid = Math.floor((s + e) / 2);

        U(s, mid, tree_idx * 2, l, r, val);
        U(mid + 1, e, tree_idx * 2 + 1, l, r, val);
    };

    const N = Number(input[0]);

    arr = Array(N + 1).fill(0n);
    lazy = Array(4 * N + 1).fill(0n);

    const temp = input[1].split(' ').map(BigInt);

    for (let i = 0; i < N; ++i) {
        arr[i + 1] = temp[i];
    }

    const M = Number(input[2]);

    for (let i = 0; i < M; ++i) {
        const temp = input[3 + i].split(' ').map(Number);

        if (temp[0] === 1) {
            U(1, N, 1, temp[1], temp[2], BigInt(temp[3]));
        } else {
            console.log(S(1, N, 1, temp[1]).toString());
        }
    }
});

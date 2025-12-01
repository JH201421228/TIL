const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    
    function gcd(a, b) {
        while (b > 0) {
            const r = a % b;
            a = b;
            b = r;
        }

        return a;
    }

    const N = Number(input[z++]);
    const string_seq = Array(N).fill("");
    for (let idx = 0; idx < N; ++idx) string_seq[idx] = input[z++];
    const K = Number(input[z++]);

    const seq = Array(N).fill(0);
    const pow_seq = Array(N).fill(N);
    const next_seq = Array.from({length: N}, () => Array(K).fill(0));
    const dp = Array.from({length: (1<<N)}, () => Array(K).fill(0));

    dp[0][0] = 1;

    for (let i = 0; i < N; ++i) {
        let cur = 0;
        const s = string_seq[i];

        for (let j = 0; j < s.length; ++j) {
            cur = (cur * 10 + (s[j] - '0')) % K;
        }

        seq[i] = cur;

        let pow = 1;
        const len = string_seq[i].length;

        for (let j = 0; j < len; ++j) {
            pow = (pow * 10) % K;
        }

        pow_seq[i] = pow;
    }

    for (let i = 0; i < N; ++i) {
        for (let j = 0; j < K; ++j) {
            next_seq[i][j] = (j * pow_seq[i] + seq[i]) % K;
        }
    }

    for (let cur = 0; cur < (1<<N); ++cur) {
        for (let i = 0; i < N; ++i) {
            if ((cur & (1<<i)) > 0) continue;

            for (let j = 0; j < K; ++j) {
                dp[cur | (1<<i)][next_seq[i][j]] += dp[cur][j];
            }
        }
    }

    let a = dp[(1<<N)-1][0];
    let b = 0;
    for (let idx = 0; idx < K; ++idx) b += dp[(1<<N)-1][idx];

    let c = gcd(b, a);

    console.log(`${a/c}/${b/c}`)
});
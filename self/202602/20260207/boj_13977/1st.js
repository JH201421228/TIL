const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const MOD = 1_000_000_007n;
    const mods = Array(4_000_001);
    let T, N, K;


    function binary_exponentiation(n) {
        let res = 1n;
        let p = MOD - 2n;

        while (p > 0n) {
            if (p%2n > 0n) res = (res * n) % MOD;
            p >>= 1n;
            n *= n;
            n %= MOD;
        }

        return res;
    }


    function solve() {
        [N, K] = input[z++].split(" ").map(Number);

        console.log((mods[N] * binary_exponentiation(mods[K] * mods[N-K] % MOD) % MOD).toString());

        return;
    }


    function main() {
        mods[0] = 1n;
        mods[1] = 1n;

        for (let i = 2; i < 4_000_001; ++i) mods[i] = mods[i-1] * BigInt(i) % MOD;

        T = Number(input[z++]);

        while (T-- > 0) solve();

        return;
    }


    main();

    return;
})
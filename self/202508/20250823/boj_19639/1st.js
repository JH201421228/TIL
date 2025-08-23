const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const D = Number(input[z++]);
    const L = Number(input[z++]);

    const G = Array.from({length: D+1}, () => []);
    const V = Array(D+1).fill(0);
    const F = Array(D+1).fill(0);

    const S = [];

    let O = 0;
    let ans = 0;

    function scc(n) {
        let p = ++O;
        V[n] = O;
        S.push(n);

        for (let x of G[n]) {
            if (V[x] === 0) p = Math.min(p, scc(x));
            else if (F[x] === 0) p = Math.min(p, V[x]);
        }

        if (V[n] === p) {
            let tmp = 0;

            while (S.length > 0) {
                let o = S.pop();
                ++tmp;

                F[o] = 1;

                if (o === n) break;
            }

            ans = Math.max(ans, tmp);
        }

        return p;
    }

    for (let i = 0; i < L; ++i) {
        const [u, v] = input[z++].split(' ').map(Number);
        G[u].push(v);
    }

    for (let n = 1; n < D+1; ++n) {
        if (V[n] === 0) scc(n);
    }

    console.log(ans);
})
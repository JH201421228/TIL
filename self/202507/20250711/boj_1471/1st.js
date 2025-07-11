const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => input.push(l));

rl.on("close", () => {
    const N = Number(input[z++]);
    const V = Array(N+1).fill(0);
    const G = Array(N+1).fill(0);
    const F = Array(N+1).fill(0);
    const S = [];
    const L = [];
    let O = 0;

    function get_next(n) {
        let res = n;
        while (n > 0) {
            res += n % 10;
            n = Math.floor(n / 10);
        }

        return res;
    };

    function scc(n) {
        let p = ++O;
        V[n] = p;
        S.push(n);

        let x = G[n];
        if (V[x] === 0) p = Math.min(p, scc(x));
        else if (F[x] === 0) p = Math.min(p, V[x]);

        if (p === V[n]) {
            const temp = [];

            while (S.length > 0) {
                let o = S.pop();
                temp.push(o);
                F[o] = -1;

                if (o === n) {
                    L.push(temp);
                    break;
                };
            }
        };

        return p;
    };

    function get_max_value(n) {
        let x = G[n];

        if (x === n) F[n] = 1;
        else if (F[x] !== 1) F[n] = F[x] + 1;
        else F[n] = get_max_value(x) + 1;

        return F[n];
    };

    function solve() {
        for (let n = 1; n < N+1; ++n) {
            let x = get_next(n);
            if (x < N+1) G[n] = x;
            else if (x % N == 0) G[n] = N;
            else G[n] = x % N;
        };

        for (let n = 1; n < N+1; ++n) if (V[n] === 0) scc(n);

        for (let temp of L) {
            let val = temp.length;

            for (let v of temp) F[v] = val;
        }

        for (let n = 1; n < N+1; ++n) {
            if (F[n] !== 1) continue;
            get_max_value(n);
        }

        console.log(Math.max(...F));
    };

    solve();
});
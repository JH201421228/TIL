const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = [];
let z = 0;

rl.on("line", l => input.push(l))

rl.on("close", () => {
    const [N, K] = input[z++].split(' ').map(Number);
    let O = 0;
    let C = 0;
    const V = Array(N+1).fill(0);
    const F = Array(N+1).fill(0);
    const U = Array(N+1).fill(0);
    let dp = Array(N+1).fill(0);
    const G = [0, ...input[z++].split(' ').map(Number)];
    const S = [];

    const cycle_parent = Array.from({length: N+1}, () => []);
    const cycle_child = Array.from({length: N+1}, () => []);

    function scc(n) {
        let p = ++O;
        V[n] = O;
        S.push(n);

        let x = G[n];
        if (V[x] === 0) p = Math.min(p, scc(x));
        else if (F[x] === 0) p = Math.min(p, V[x]);

        if (V[n] === p) {
            ++C;

            while (S.length > 0) {
                let o = S.pop();
                
                F[o] = C;
                U[C] += 1;

                if (o === n) break;
            }
        }

        return p;
    }

    function solve() {
        for (let n = 1; n < N+1; ++n) {
            if (V[n] === 0) scc(n);
        }

        for (let n = 1; n < N+1; ++n) {
            if (F[n] !== F[G[n]]) {
                cycle_parent[F[G[n]]].push(F[n]);
                cycle_child[F[n]].push(F[G[n]]);
            }
        }

        dp[0] = 1;

        for (let x = 1; x < C+1; ++x) {
            if (cycle_child[x].length === 0) {
                const temp = [];
                const q = [x];

                while (q.length > 0) {
                    let n = q.shift();
                    temp.push(n);
                    
                    for (let nxt of cycle_parent[n]) q.push(nxt);
                }

                const dp_temp = [...dp];

                for (let n = U[temp[0]]; n < U[temp[0]] + temp.length; ++n) {
                    for (let idx = 0; idx < K; ++idx) {
                        if (dp[idx] !== 0 && idx + n < K+1) dp_temp[idx+n] = 1;
                    }
                }

                dp = [...dp_temp];
            }
        }

        let ans = K;

        while (ans !== 0) {
            if (dp[ans] !== 0) break;

            --ans;
        }

        console.log(ans);

        return;
    }

    solve();

    return;
})
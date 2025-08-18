const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;

rl.on("line", l => input.push(l))

rl.on("close", () => {
    const [K, N] = input[z++].split(' ').map(Number);
    const G = Array.from({length: 2*K+2}, () => []);
    const V = Array(2*K+2).fill(0);
    const F = Array(2*K+2).fill(0);
    const S = [];

    let O = 0;
    let cnt = 0;

    const color = {'R': 0, 'B': 1}

    function minor_setting(a, b, c, d) {
        G[b].push(a);
        G[c].push(d);

        return;
    }

    function setting(a, b, c, d, e, f) {
        minor_setting(2*a+color[b], 2*c+1-color[d], 2*a+1-color[b], 2*c+color[d]);
        minor_setting(2*a+color[b], 2*e+1-color[f], 2*a+1-color[b], 2*e+color[f]);
        minor_setting(2*c+color[d], 2*e+1-color[f], 2*c+1-color[d], 2*e+color[f]);

        return;
    }

    function scc(n) {
        let p = ++O;
        V[n] = O;
        S.push(n);

        for (let x of G[n]) {
            if (V[x] === 0) p = Math.min(p, scc(x));
            else if (F[x] === 0) p = Math.min(p, V[x]);
        }

        if (p === V[n]) {
            ++cnt;

            while (S.length > 0) {
                const o = S.pop();
                F[o] = cnt;

                if (o === n) break;
            }
        }

        return p;
    }

    for (let i = 0; i < N; ++i) {
        const temp = input[z++].split(' ');
        setting(Number(temp[0]), temp[1], Number(temp[2]), temp[3], Number(temp[4]), temp[5]);
    }

    for (let n = 2; n < 2*K+2; ++n) {
        if (V[n] === 0) scc(n);
    }

    let ans = '';

    for (let n = 1; n < K+1; ++n) {
        if (F[2*n] === F[2*n+1]) {
            console.log(-1);
            return;
        }
        else if (F[2*n] < F[2*n+1]) ans += 'R';
        else ans += 'B';
    }

    console.log(ans);

    return;
})
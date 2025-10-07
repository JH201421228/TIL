const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const N = Number(input[z++]);
    const V = Array(N+1).fill(0);
    const nodes = Array(N+1).fill(0);
    const inner = Array(N+1).fill(0);
    const outer = Array(N+1).fill(0);
    const G = Array.from({length: N+1}, () => [])
    
    function set_inner(n) {
        nodes[n] = 1;

        for (let xd of G[n]) {
            const x = xd[0];
            const d = xd[1];
            if (nodes[x] === 0) {
                set_inner(x);
                nodes[n] += nodes[x];
                inner[n] += inner[x] + nodes[x] * d;
            }
        }
        return;
    }

    function set_outer(n) {
        V[n] = 1;

        for (let xd of G[n]) {
            const x = xd[0];
            const d = xd[1];
            if (V[x] === 0) {
                outer[x] = outer[n] + (N - nodes[n]) * d + inner[n] - (inner[x] + nodes[x] * d) + (nodes[n] - nodes[x]) * d;
                set_outer(x);
            }
        }

        return;
    }

    function solve() {
        for (let i = 0; i < N-1; ++i) {
            const [u, v, d] = input[z++].split(' ').map(Number);

            G[u].push([v, d]);
            G[v].push([u, d]);
        }

        set_inner(1);
        set_outer(1);

        for (let i = 1; i < N+1; ++i) {
            console.log(inner[i] + outer[i]);
        }

        return;
    }

    solve();
})
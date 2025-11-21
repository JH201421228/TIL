const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const N = Number(input[z++]);
    const lines = [];
    const V = Array(N+1).fill(0);
    const G = Array.from({length: N+1}, () => []);
    const q = []


    function is_same_dot(d1, d2, d3, d4) {
        if ((d1[0] === d3[0] && d1[1] === d3[1]) ||
            (d1[0] === d4[0] && d1[1] === d4[1]) ||
            (d2[0] === d3[0] && d2[1] === d3[1]) ||
            (d2[0] === d4[0] && d2[1] === d4[1])) {
                return true;
        }

        return false;
    }


    function is_online(d1, d2, d3) {
        if (d3[0] >= Math.min(d1[0], d2[0]) &&
            d3[0] <= Math.max(d1[0], d2[0]) &&
            d3[1] >= Math.min(d1[1], d2[1]) &&
            d3[1] <= Math.max(d1[1], d2[1]) &&
            ((d1[1] - d3[1]) * (d2[0] - d3[0])) ===
            ((d1[0] - d3[0]) * (d2[1] - d3[1]))) {
                return true;
        }

        return false;
    }


    function ccw(d1, d2, d3, d4) {
        const expr1 = (d3[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d3[1] - d2[1]);
        const expr2 = (d4[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d4[1] - d2[1]);
        const expr3 = (d1[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d1[1] - d4[1]);
        const expr4 = (d2[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d2[1] - d4[1]);

        if (expr1 * expr2 < 0 && expr3 * expr4 < 0) {
            return true;
        }

        return false;
    }


    function cross_check(d1, d2, d3, d4) {
        if (is_same_dot(d1, d2, d3, d4)) return true;

        if (is_online(d1, d2, d3)) return true;

        if (is_online(d1, d2, d4)) return true;

        if (is_online(d3, d4, d1)) return true;

        if (is_online(d3, d4, d2)) return true;

        if (ccw(d1, d2, d3, d4)) return true;

        return false;
    }


    function travel(m) {
        let res = 0;

        V[m] = 1;
        q.push(m);

        while (q.length !== 0) {
            let n = q.shift();

            ++res;

            for (let x of G[n]) {
                if (V[x] === 0) {
                    V[x] = 1;
                    q.push(x);
                }
            }
        }

        return res;
    }


    function solve() {
        for (let idx = 0; idx < N; ++idx) {
            lines.push(input[z++].split(' ').map(Number))
        }

        for (let i = 0; i < N; ++i) {
            const [x1, y1, x2, y2] = lines[i];

            for (let j = i+1; j < N; ++j) {
                const [x3, y3, x4, y4] = lines[j];

                if (cross_check([x1, y1,], [x2, y2], [x3, y3], [x4, y4])) {
                    G[i+1].push(j+1);
                    G[j+1].push(i+1);
                }
            }
        }
        
        let res = 0, cnt = 0;

        for (let n = 1; n < N+1; ++n) {
            if (V[n] === 0) {
                ++cnt;
                res = Math.max(res, travel(n));
            }
        }

        console.log(cnt);
        console.log(res);

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
});
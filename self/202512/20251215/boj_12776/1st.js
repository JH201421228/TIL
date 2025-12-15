const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const N = Number(input[z++]);
    const A = [];
    const B = [];
    let ans = 0;
    let rest = 0;

    function solve() {
        for (let i = 0; i < N; ++i) {
            const [a, b] = input[z++].split(' ').map(Number);

            if (a < b) A.push([a, b]);
            else B.push([-B, -a]);
        }

        A.sort((x, y) => {
            if (x[0] !== y[0]) return x[0] - y[0];
            return x[1] - y[1];
        })

        B.sort((x, y) => {
            if (x[0] !== y[0]) return x[0] - y[0];
            return x[1] - y[1];
        })

        for (let p of A) {
            const [a, b] = p;
            if (rest < a) {
                ans += (a - rest);
                rest = a;
            }

            rest += (b-a);
        }

        for (let p of B) {
            const a = -p[1];
            const b = -p[0];

            if (rest < a) {
                ans += (a - rest);
                rest = a;
            }

            rest += (b-a);
        }

        console.log(ans);

        return;
    }


    function main() {
        solve()

        return;
    }

    main();

    return;
})
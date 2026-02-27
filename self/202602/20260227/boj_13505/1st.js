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
    let mask = 0, cand = 0, attempt = 0;
    const nums = input[z++].split(" ").map(Number);
    const S = new Set();


    function solve() {
        for (let i = 29; i >= 0; --i) {
            mask |= 1<<i;
            attempt = 1<<i | cand;

            S.clear();

            for (let n of nums) {
                const tmp = n & mask;
                if (S.has(tmp ^ attempt)) {
                    cand = attempt;
                    break;
                }
                S.add(tmp);
            }
        }

        console.log(cand);

        return;
    }


    function main() {
        solve();

        return;
    }


    main()

    return;
})
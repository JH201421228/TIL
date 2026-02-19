const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const L = Number(input[z++]);
    const S = input[z++];
    const preprocess = Array(L).fill(0);
    let stack_n = 0;


    function solve() {
        for (let idx = 1; idx < L; ++idx) {
            while (stack_n > 0 && S[idx] !== S[stack_n]) {
                stack_n = preprocess[stack_n-1];
            }

            if (S[idx] === S[stack_n]) {
                ++stack_n;
                preprocess[idx] = stack_n;
            }
        }

        console.log(L-preprocess[L-1]);

        return;
    }


    function main() {
        solve();

        return;
    }


    main()

    return;
})
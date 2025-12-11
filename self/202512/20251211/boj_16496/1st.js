const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const N = Number(input[z++]);
    const temp = input[z++].split(' ');
    const S1 = [];
    const S2 = [];


    function solve() {
        for (let idx = 0; idx < N; ++idx) {
            const t = temp[idx];

            if (S1.length === 0) S1.push(t);
            else {
                if (S1[S1.length - 1] + t >= t + S1[S1.length - 1]) {
                    if (S2.length === 0) S2.push(t);
                    else {
                        if (t + S2[S2.length - 1] < S2[S2.length - 1] + t) {
                            while (S2.length > 0 && t + S2[S2.length - 1] < S2[S2.length - 1] + t) {
                                S1.push(S2.pop());
                            }
                        }
                        S2.push(t);
                    }
                }
                else {
                    while (S1.length > 0 && S1[S1.length - 1] + t < t + S1[S1.length - 1]) {
                        S2.push(S1.pop());
                    }
                    S1.push(t);
                }
            }
        }

        let ans = '';

        while (S1.length > 0) S2.push(S1.pop());

        while (S2.length > 0) ans += S2.pop();

        if (ans[0] === '0') console.log(0);
        else console.log(ans);

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

})
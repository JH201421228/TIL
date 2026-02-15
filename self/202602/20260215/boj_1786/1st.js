const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    
    function solve() {
        const T = input[z++];
        const P = input[z++];
        
        const p_len = P.length;
        const preprocess = Array(p_len).fill(0);

        let stack_n = 0;

        for (let idx = 1; idx < p_len; ++idx) {
            while (stack_n > 0 && P[idx] !== P[stack_n]) {
                stack_n = preprocess[stack_n-1];
            }

            if (P[idx] === P[stack_n]) {
                ++stack_n;
                preprocess[idx] = stack_n;
            }
        }

        const t_len = T.length;
        const ans_list = [];
        let cnt = 0;
        let p_idx = 0;

        for (let idx = 0; idx < t_len; ++idx) {
            while (p_idx > 0 && T[idx] !== P[p_idx]) {
                p_idx = preprocess[p_idx-1];
            }

            if (P[p_idx] === T[idx]) {
                if (p_idx === p_len-1) {
                    ++cnt;
                    ans_list.push(idx-p_len+2);
                    p_idx = preprocess[p_idx];
                }
                else {
                    ++p_idx;
                }
            }
        }

        console.log(cnt);
        console.log(...ans_list)

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
})
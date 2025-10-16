const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const K = Number(input[z++]);
    let cnt = 1;
    let [tti, ttj] = input[z++].split(' ').map(Number)
    let ti = (1<<K) - ttj;
    let tj = tti - 1;

    const delta = [[0, 0], [1, 0], [0, 1], [1, 1]];


    function set_num(i, j, ti, tj, l) {
        const res = Array.from({length: 4}, () => Array(2).fill(-1));

        if (ti >= i && ti < i+l && tj >= j && tj < j+l) {
            ;
        }
        else {
            ans[i+l-1][j+l-1] = cnt;
            res[0][0] = i+l-1;
            res[0][1] = j+l-1;
        }

        if (ti >= i+l && ti < i+l*2 && tj >= j && tj < j+l) {
            ;
        }
        else {
            ans[i+l][j+l-1] = cnt;
            res[1][0] = i+l;
            res[1][1] = j+l-1;
        }

        if (ti >= i && ti < i+l && tj >= j+l && tj < j+l*2) {
            ;
        }
        else {
            ans[i+l-1][j+l] = cnt;
            res[2][0] = i+l-1;
            res[2][1] = j+l;
        }

        if (ti >= i+l && ti < i+l*2 && tj >= j+l && tj < j+l*2) {
            ;
        }
        else {
            ans[i+l][j+l] = cnt;
            res[3][0] = i+l;
            res[3][1] = j+l;
        }

        ++cnt;

        return res;
    }
    
    
    function dq(i, j, ti, tj, l) {
        if (l === 1) {
            for (let di = 0; di < 2; ++di) {
                for (let dj = 0; dj < 2; ++dj) {
                    if (ans[i+di][j+dj] === 0) {
                        ans[i+di][j+dj] = cnt;
                    }
                }
            }
            ++cnt;
            return;
        }

        const temp = set_num(i, j, ti, tj, l);

        for (let idx = 0; idx < 4; ++idx) {
            let di = delta[idx][0] * l;
            let dj = delta[idx][1] * l;

            if (temp[idx][0] != -1 && temp[idx][1] != -1) {
                dq(i+di, j+dj, temp[idx][0], temp[idx][1], l/2);
            }
            else {
                dq(i+di, j+dj, ti, tj, l/2);
            }
        }

        return;
    }


    const ans = Array.from({length: 1<<K}, () => Array(1<<K).fill(0));
    ans[ti][tj] = -1;

    dq(0, 0, ti, tj, (1<<(K-1)));

    for (let i = 0; i < (1<<K); ++i) {
        console.log(...ans[i]);
    }
});
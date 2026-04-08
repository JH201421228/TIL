const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    
    const N = BigInt(input[z++]);
    const MOD = 1_000_000_007n;

    function cal(mat1, mat2) {
        const res = [[0n, 0n], [0n, 0n]];
        
        for (let i = 0; i < 2; ++i) {
            for (let j = 0; j < 2; ++j) {
                for (let k = 0; k < 2; ++k) {
                    res[i][j] += mat1[i][k] * mat2[k][j] % MOD;
                    res[i][j] %= MOD; 
                }
            }
        }
        
        return res;
    }
    
    function recur(n, mat) {
        let res = [[1n, 0n], [0n, 1n]];

        while (n > 0n) {
            if (n%2n > 0) res = cal(res, mat);
            mat = cal(mat, mat);
            n /= 2n;
        }

        return res;
    }


    function solve() {
        if (N%2n > 0) {
            console.log(0);
            return;
        }

        let res = [[4n, -1n], [1n, 0n]]
        res = recur(N/2n, res);
        console.log(((res[0][0] + res[0][1] + MOD)%MOD).toString())

        return;
    }

    function main() {
        solve();

        return;
    }

    main();

    return;
})
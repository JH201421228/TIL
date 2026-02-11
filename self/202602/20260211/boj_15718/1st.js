const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));


rl.on("close", () => {
    const MOD = 100_007;
    let N, M, T;
    const fac1 = Array(97);
    const fac2 = Array(1031);
    const inv1 = Array(97);
    const inv2 = Array(1031);


    function lucas(n, k, fac, inv, p) {
        let res = 1;
        let a, b;

        while (n > 0 || k > 0) {
            a = n % p; b = k % p;
            
            if (b > a) return 0;

            res = res * ((fac[a] * inv[b] % p) * inv[a-b] % p) % p;

            n = Math.floor(n/p); k = Math.floor(k/p);
        }

        return res;
    }


    function egcd(a, b) {
        let x0 = 1, x1 = 0, y0 = 0, y1 = 1, p = a;

        while (b > 0) {
            let q = Math.floor(a/b);
            let a_ = b, b_ = a % b;
            let x0_ = x1, x1_ = x0 - q * x1;
            let y0_ = y1, y1_ = y0 - q * y1;

            a = a_, b = b_, x0 = x0_, x1 = x1_, y0 = y0_, y1 = y1_;
        }


        if (y0 < 0) y0 += p;

        return y0;
    }


    function crt(a, b) {
        let res = 0;

        res = (res + (a * 1031 % MOD) * egcd(97, 1031) % MOD) % MOD;
        res = (res + (b * 97 % MOD) * egcd(1031, 97) % MOD) % MOD;

        return res;
    }
    

    function solve() {
        [N, M] = input[z++].split(" ").map(Number);

        if (N === 0 && M === 1) {
            console.log(1);
            return;
        }

        if (N === 0) {
            console.log(0);
            return;
        }

        if (M === 1) {
            console.log(0);
            return;
        }

        let a = lucas(N-1, M-2, fac1, inv1, 97);
        let b = lucas(N-1, M-2, fac2, inv2, 1031);

        console.log(crt(a, b));

        return;
    }


    function main() {
        T = Number(input[z++])

        fac1[0] = 1; fac1[1] = 1; fac2[0] = 1; fac2[1] = 1;

        for (let i = 1; i < 97; ++i) fac1[i] = fac1[i-1] * i % 97;
        for (let i = 1; i < 1031; ++i) fac2[i] = fac2[i-1] * i % 1031;

        inv1[96] = egcd(97, fac1[96]);
        inv2[1030] = egcd(1031, fac2[1030]);

        for (let i = 96; i > 0; --i) inv1[i-1] = inv1[i] * i % 97;
        for (let i = 1030; i > 0; --i) inv2[i-1] = inv2[i] * i % 1031;

        while (T-- > 0) solve();

        return;
    }


    main();

    return;
})
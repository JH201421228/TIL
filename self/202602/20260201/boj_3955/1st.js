const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const MAX = 1_000_000_000;
    let T, K, C;


    function egcd(a, b) {
        let x0 = 1, x1 = 0, y0 = 0, y1 = 1;
        let na, nb, nx0, nx1, ny0, ny1;

        while (b != 0) {
            let q = Math.floor(a/b);
            na = b; nb = a%b; a = na; b = nb;
            nx0 = x1; nx1 = x0 - q*x1; x0 = nx0; x1 = nx1;
            ny0 = y1; ny1 = y0 - q*y1; y0 = ny0; y1 = ny1;
        }

        return [a, x0, y0];
    }


    function solve() {
        [K, C] = input[z++].split(" ").map(Number);

        if (C === 1) {
            if (K+1 <= MAX) console.log(K+1);
            else console.log("IMPOSSIBLE");
            return;
        }

        if (K === 1) {
            console.log(1);
            return;
        }

        const [g, x, y] = egcd(C, K);

        if (g !== 1) {
            console.log("IMPOSSIBLE");
            return;
        }

        let ans = (x % K + K) % K;

        if (ans > MAX) {
            console.log("IMPOSSIBLE");
            return;
        }

        console.log(ans);

        return;
    }


    function main() {
        T = Number(input[z++]);
        
        while (T-- > 0) solve();

        return;
    }


    main();

    return;
})
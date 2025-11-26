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
    const dots = Array.from({length: N}, () => Array(2).fill(0));


    function ccw(p1, p2, p3) {
        return (p3[0] - p1[0]) * (p2[1] - p3[1]) - (p3[1] - p1[1]) * (p2[0] - p3[0]);
    }


    function is_cross_line(p) {
        let res = 0;

        for (let idx = 0; idx < N; ++idx) {
            let p1 = dots[idx];
            let p2 = dots[(idx+1) % N];

            if (p1[1] < p2[1]) {
                const temp = p1;
                p1 = p2;
                p2 = temp;
            }

            if (ccw(p1, p2, p) === 0) {
                if (p[0] >= Math.min(p1[0], p2[0]) &&
                    p[0] <= Math.max(p1[0], p2[0]) &&
                    p[1] >= Math.min(p1[1], p2[1]) &&
                    p[1] <= Math.max(p1[1], p2[1])) {
                        return 1;
                }
            }

            if (p[0] > Math.max(p1[0], p2[0])) continue;

            if (p[1] >= Math.max(p1[1], p2[1])) continue;

            if (p[1] < Math.min(p1[1], p2[1])) continue;

            if (ccw(p1, p2, p) > 0) ++res;
        }

        return res % 2;
    }


    function solve() {
        for (let idx = 0; idx < N; ++idx) {
            const temp = input[z++].split(' ').map(Number);

            if (is_cross_line(temp) === 1) {
                console.log(1);
            }
            else {
                console.log(0);
            }
        }

        return;
    }


    function main() {
        for (let idx = 0; idx < N; ++idx) {
            const temp = input[z++].split(' ').map(Number);
            dots[idx][0] = temp[0];
            dots[idx][1] = temp[1];
        }

        solve();

        return;
    }


    main();

});
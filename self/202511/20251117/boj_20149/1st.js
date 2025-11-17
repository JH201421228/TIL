const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const lines = [];
    const ans = [];

    function in_ans(p) {
        for (let q of ans) {
            if (q[0] === p[0] && q[1] === p[1]) return true;
        }

        return false;
    }

    function same_dot(d1, d2) {
        if (d1[0] === d2[0] && d1[1] === d2[1]) return true;

        return false;
    }

    function is_same_dot() {
        const d1 = [lines[0][0], lines[0][1]];
        const d2 = [lines[0][2], lines[0][3]];
        const d3 = [lines[1][0], lines[1][1]];
        const d4 = [lines[1][2], lines[1][3]];

        if (same_dot(d1, d3) && !in_ans(d1)) ans.push(d1);
        if (same_dot(d1, d4) && !in_ans(d1)) ans.push(d1);
        if (same_dot(d2, d3) && !in_ans(d2)) ans.push(d2);
        if (same_dot(d2, d4) && !in_ans(d2)) ans.push(d2);

        return;
    }

    function online(d1, d2, d3) {
        if (d3[0] >= Math.min(d1[0], d2[0]) &&
            d3[0] <= Math.max(d1[0], d2[0]) &&
            d3[1] >= Math.min(d1[1], d2[1]) &&
            d3[1] <= Math.max(d1[1], d2[1])) {
            if ((d1[1] - d3[1]) * (d2[0] - d3[0]) ===
                (d1[0] - d3[0]) * (d2[1] - d3[1])) {
                return true;
            }
        }

        return false;
    }

    function is_online() {
        const d1 = [lines[0][0], lines[0][1]];
        const d2 = [lines[0][2], lines[0][3]];
        const d3 = [lines[1][0], lines[1][1]];
        const d4 = [lines[1][2], lines[1][3]];

        if (online(d1, d2, d3) && !in_ans(d3)) ans.push(d3);
        if (online(d1, d2, d4) && !in_ans(d4)) ans.push(d4);
        if (online(d3, d4, d1) && !in_ans(d1)) ans.push(d1);
        if (online(d3, d4, d2) && !in_ans(d2)) ans.push(d2);

        return;
    }

    function ccw() {
        const d1 = [lines[0][0], lines[0][1]];
        const d2 = [lines[0][2], lines[0][3]];
        const d3 = [lines[1][0], lines[1][1]];
        const d4 = [lines[1][2], lines[1][3]];

        const expr1 = ((d3[0] - d2[0]) * (d2[1] - d1[1]) -
                        (d2[0] - d1[0]) * (d3[1] - d2[1]))
        const expr2 = ((d4[0] - d2[0]) * (d2[1] - d1[1]) -
                        (d2[0] - d1[0]) * (d4[1] - d2[1]))
        const expr3 = ((d1[0] - d3[0]) * (d3[1] - d4[1]) -
                        (d3[0] - d4[0]) * (d1[1] - d3[1]))
        const expr4 = ((d2[0] - d3[0]) * (d3[1] - d4[1]) -
                        (d3[0] - d4[0]) * (d2[1] - d3[1]))

        if (expr1 * expr2 < 0 && expr3 * expr4 < 0) {
            console.log(1);

            let x, y;

            if (d1[0] === d2[0]) {
                x = d1[0];
                y = ((d4[1] - d3[1]) * (x - d3[0]) /
                    (d4[0] - d3[0]) + d3[1]);
            }
            else if (d3[0] === d4[0]) {
                x = d3[0];
                y = ((d2[1] - d1[1]) * (x - d1[0]) /
                    (d2[0] - d1[0]) + d1[1]);
            }
            else {
                const alpha1 = (d2[1] - d1[1]) / (d2[0] - d1[0]);
                const alpha2 = (d4[1] - d3[1]) / (d4[0] - d3[0]);

                x = (alpha1 * d1[0] - alpha2 * d3[0] - d1[1] + d3[1])
                    / (alpha1 - alpha2);
                y = alpha1 * (x - d1[0]) + d1[1];
            }

            console.log(x, y);

            return;
        }

        console.log(0);

        return;
    }

    function cross_check() {
        is_same_dot();
        is_online();

        if (ans.length > 1) {
            console.log(1);
            return;
        }
        else if (ans.length === 1) {
            console.log(1);
            console.log(ans[0][0], ans[0][1]);
            return;
        }

        ccw();

        return;
    }

    function solve() {
        cross_check();

        return;
    }

    function main() {
        for (let i = 0; i < 2; ++i) lines.push(input[z++].split(" ").map(Number));

        solve();

        return;
    }

    main();
})
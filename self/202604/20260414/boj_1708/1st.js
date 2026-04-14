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
    const dots = [];

    function solve() {
        for (let i = 0; i < N; ++i) {
            dots.push(input[z++].split(" ").map(Number))
        }

        dots.sort((a, b) => {
            if (a[1] === b[1]) return a[0] - b[0];
            return a[1] - b[1];
        })

        const origin = dots[0];

        const rest = dots.slice(1);

        rest.sort((a, b) => {
            const angleA = Math.atan2(a[1] - origin[1], a[0] - origin[0]);
            const angleB = Math.atan2(b[1] - origin[1], b[0] - origin[0]);

            if (angleA === angleB) {
                const distA = (a[1] - origin[1]) * (a[1] - origin[1]) + (a[0] - origin[0]) * (a[0] - origin[0]);
                const distB = (b[1] - origin[1]) * (b[1] - origin[1]) + (b[0] - origin[0]) * (b[0] - origin[0]);

                return distA - distB;
            }

            return angleA - angleB;
        })

        const q = [origin];

        for (let dot of rest) {
            if (q.length < 2) q.push(dot);
            else {
                while (q.length >= 2) {
                    const p1 = q[q.length-2];
                    const p2 = q[q.length-1];

                    const dx1 = p2[0] - p1[0];
                    const dy1 = p2[1] - p1[1];
                    const dx2 = dot[0] - p1[0];
                    const dy2 = dot[1] - p1[1];

                    if (dx1 * dy2 - dx2 * dy1 > 0) break;
                    q.pop();
                }

                q.push(dot);
            }
        }
        console.log(q.length);

        return;
    }

    function main() {
        solve();

        return;
    }

    main();

    return;
});
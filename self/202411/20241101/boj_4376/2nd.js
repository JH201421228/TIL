const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];
rl.on('line', line => {
    input.push(line);
});

rl.on('close', () => {
    let idx = 0;

    while (idx < input.length) {
        const [N, M, S, speed] = input[idx++].split(" ").map(Number);
        const gopers = [[]];
        const holes = [[]];

        for (let i = 0; i < N; i++) {
            gopers.push(input[idx++].split(" ").map(Number));
        }

        for (let i = 0; i < M; i++) {
            holes.push(input[idx++].split(" ").map(Number));
        }

        const G = Array.from({ length: N + 1 }, () => []);
        for (let i = 1; i <= N; i++) {
            const [g_x, g_y] = gopers[i];

            for (let j = 1; j <= M; j++) {
                const [h_x, h_y] = holes[j];
                const distance = Math.sqrt((g_x - h_x) ** 2 + (g_y - h_y) ** 2);
                
                if (distance <= S * speed) {
                    G[i].push(j);
                }
            }
        }

        let ans = 0;
        const C = Array(M + 1).fill(0);

        const B = n => {
            for (let x of G[n]) {
                if (V[x]) continue;
                V[x] = 1;

                if (C[x] === 0 || B(C[x])) {
                    C[x] = n;
                    return true;
                }
            }
            return false;
        };

        for (let i = 1; i <= N; i++) {
            V = Array(M + 1).fill(0);
            if (B(i)) ans++;
        }

        console.log(N - ans);
    }
});

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l))


rl.on("close", () => {
    const [N, M] = input[z++].split(" ").map(Number);
    let o = 0;
    let group_n = 1;
    const V = Array(N+1).fill(0);
    const F = Array(N+1).fill(0);
    const cash = Array(N+1).fill(0);
    const restaurant = Array(N+1).fill(0);
    const stack = [];
    const queue = [];
    const G = Array.from({length: N+1}, () => []);

    function scc(n) {
        ++o;
        let p = o;
        V[n] = o;
        stack.push(n);

        for (let x of G[n]) {
            if (V[x] === 0) p = Math.min(p, scc(x));
            else if (F[x] === 0) p = Math.min(p, V[x]);
        }

        if (p === V[n]) {
            while (stack.length > 0) {
                let c = stack.pop();
                F[c] = group_n;
                if (c === n) break;
            }
            ++group_n;
        }

        return p;
    }
    

    function solve() {
        for (let i = 0; i < M; ++i) {
            const [u, v] = input[z++].split(" ").map(Number);
            G[u].push(v);
        }

        for (let idx = 0; idx < N; ++idx) cash[idx+1] = Number(input[z++]);

        let [S, P] = input[z++].split(" ").map(Number);

        const temp = input[z++].split(" ").map(Number);

        for (let i = 0; i < P; ++i) restaurant[temp[i]] = 1;

        for (let n = 1; n < N+1; ++n) {
            if (V[n] === 0) scc(n);
        }

        const group_cash = Array(group_n).fill(0);
        const group_restaurant = Array(group_n).fill(0);
        const group_visit = Array(group_n).fill(0);
        const indegree = Array(group_n).fill(0);
        const dp = Array(group_n).fill(0);
        const group_graph = Array.from({length: group_n}, () => []);
        const group_stack = [];

        for (let n = 1; n < N+1; ++n) {
            const group = F[n];
            group_cash[group] += cash[n];
            if (restaurant[n] !== 0) group_restaurant[group] = 1;

            for (let x of G[n]) {
                if (group !== F[x]) group_graph[group].push(F[x]);
            }
        }

        S = F[S];
        group_visit[S] = 1;
        group_stack.push(S);

        while (group_stack.length > 0) {
            const n = group_stack.pop();
            for (let x of group_graph[n]) {
                if (group_visit[x] === 0) {
                    group_visit[x] = 1;
                    group_stack.push(x);
                }
            }
        }

        for (let n = 1; n < group_n; ++n) {
            if (group_visit[n] === 0) continue;

            for (let x of group_graph[n]) {
                if (group_visit[x] !== 0) ++indegree[x];
            }
        }

        dp[S] = group_cash[S];
        queue.push(S);

        while (queue.length > 0) {
            const n = queue.shift();

            for (let x of group_graph[n]) {
                dp[x] = Math.max(dp[x], dp[n] + group_cash[x]);

                --indegree[x];

                if (indegree[x] === 0) queue.push(x);
            }
        }

        let ans = 0;

        for (let idx = 1; idx < group_n; ++idx) {
            if (group_restaurant[idx] != 0) ans = Math.max(ans, dp[idx]);
        }

        console.log(ans);

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
})
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = [];
let z = 0;

rl.on("line", l => input.push(l));

rl.on("close", () => {
    const arr = Array(100_001).fill(0);
    const state = Array(100_001).fill(0);
    const sets = Array.from({length: 100_001}, () => new Set());
    

    function find(idx) {
        let root = idx;

        while (root != arr[root]) root = arr[root];

        while (idx != root) {
            let p = arr[idx];
            arr[idx] = root;
            idx = p;
        }

        return root;
    }


    function union(a, b, w) {
        let pa = find(a);
        let pb = find(b);

        let fix = state[a] - state[b];

        if (sets[pa].size < sets[pb].size) {
            let temp = sets[pa];
            sets[pa] = sets[pb];
            sets[pb] = temp;
            w *= -1;
            fix *= -1;
        }

        arr[pb] = pa;

        for (let v of sets[pb]) {
            sets[pa].add(v);
            state[v] += w+fix;
        }

        sets[pb].clear();

        return;
    }

    
    function solve(N, M) {
        for (let idx = 0; idx < N+1; ++idx) {
            arr[idx] = idx;
            sets[idx].clear();
            sets[idx].add(idx)
            state[idx] = 0;
        }
        
        for (let i = 0; i < M; ++i) {
            const temp = input[z++].split(" ");
            const a = Number(temp[1]);
            const b = Number(temp[2]);
            
            const pa = find(a);
            const pb = find(b);
            
            if (temp[0] === "!") {
                const w = Number(temp[3]);

                if (pa !== pb) union(a, b, w);
            }
            else {
                if (pa !== pb) console.log("UNKNOWN");
                else console.log(state[b] - state[a]);
            }
        }

        return;
    }

    
    function main() {
        while (true) {
            const [N, M] = input[z++].split(" ").map(Number);

            if (N === 0 && M === 0) break;

            solve(N, M);
        }

        return;
    }


    main();

    return;
});
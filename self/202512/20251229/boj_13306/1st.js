const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {

    const [N, Q] = input[z++].split(' ').map(Number);
    const parent = Array(N+1).fill(0);
    const tree = Array(N+1).fill(0);
    const ans = [];
    const question = [];
    

    function find(idx) {
        let root = idx;

        while (root !== tree[root]) root = tree[root];

        while (idx !== root) {
            const parent = tree[idx];
            tree[idx] = root;
            idx = parent;
        }

        return root;
    }


    function union(idx) {
        const p = find(parent[idx]);

        tree[idx] = p;

        return;
    }


    function solve() {
        parent[1] = 1;
        for (let idx = 0; idx < N-1; ++idx) parent[idx+2] = Number(input[z++]);
        for (let idx = 0; idx < N+1; ++idx) tree[idx] = idx;

        for (let i = 0; i < N+Q-1; ++i) {
            const temp = input[z++].split(' ').map(Number);

            if (temp[0] === 1) {
                const a = temp[1];
                const b = temp[2];
                question.push([a, b]);
            }
            else {
                question.push([0, temp[1]])
            }
        }
        
        while (question.length > 0) {
            const cur_question = question.pop();

            if (cur_question[0] !== 0) {
                if (find(cur_question[0]) === find(cur_question[1])) ans.push("YES");
                else ans.push("NO");
            }
            else union(cur_question[1]);
        }

        for (let idx = ans.length; idx > 0; --idx) console.log(ans[idx-1]);

        return;
    }

    
    function main() {
        solve();

        return;
    }


    main();

    return;
})
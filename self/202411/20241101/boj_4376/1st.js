const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    while(z < input.length) {
        const [N, M, S, V] = input[z].split(" ").map(Number); ++z;
        const G = Array.from({length: N+1}, () => [])
        const gopers = [[]]
        const holse = [[]]
        const C = Array(M+1).fill(0)
        const U = Array(M+1).fill(0)
    
        const B = n => {
            for (let x of G[n]) {
                if (U[x] !== 0) {
                    continue
                }
                U[x] = 1
    
                if (C[x] === 0 || B(C[x])) {
                    C[x] = n
                    return true
                }
            }
    
            return false
        }
    
        for (let i = 1; i < N+1; ++i) {
            gopers.push(input[z].split(" ").map(Number)); ++z;
        }
    
        for (let i = 1; i < M+1; ++i) {
            holse.push(input[z].split(" ").map(Number)); ++z;
        }
    
        for (let i = 1; i < N+1; ++i) {
            const [x, y] = gopers[i]
            for (let j = 1; j < M+1; ++j) {
                const dx = x - holse[j][0]
                const dy = y - holse[j][1]
    
                if (Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2)) <= S*V) {
                    G[i].push(j)
                }
            }
        }
    
        for (let i = 1; i < N+1; ++i) {
            for (let j = 1; j < M+1; ++j) {
                U[j] = 0
            }
            B(i)
        }
    
        let ans = 0
        for (let i = 1; i < M+1; ++i) {
            if (C[i] !== 0) {
                ++ans
            }
        }
    
        console.log(N-ans)
    }
})
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    const N = Number(input[0])
    const H = Array(N+2).fill(0)
    const S = [0]

    for (let idx = 1; idx < N+1; ++idx) {
        H[idx] = Number(input[idx])
    }

    const area = N => {
        let ans = 0

        for (let idx = 1; idx < N+2; ++idx) {
            while (!(S.length === 0) && H[S[S.length-1]] > H[idx]) {
                const i = S.pop()
                ans = Math.max(ans, H[i]*(idx-S[S.length-1]-1))
            }
            S.push(idx)
        }

        return ans
    }

    console.log(area(N))
})
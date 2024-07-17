const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


let input = []

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    let idx = 0
    const T = parseInt(input[idx++])

    for (let i = 0; i < T; i++) {
        const N = parseInt(input[idx++])
        const coins = input[idx++].split(' ').map(Number)
        const M = parseInt(input[idx++])
        const dp = Array(M+1).fill(0)

        dp[0] = 1

        for (let c of coins) {
            for (let j = c; j < M+1; j++) {
                dp[j] = dp[j] + dp[j-c]
            }
        }

        console.log(dp[M])
    }
})
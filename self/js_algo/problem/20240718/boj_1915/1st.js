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
    let [N, M] = input[0].split(' ').map(Number)
    let dp = []

    for (let i = 0; i < N; ++i) {
        dp.push(input[i+1].split('').map(Number))
    }

    let ans = 0
    for (let i = 0; i < N; ++i) {
        if (dp[i][0] === 1) {
            ans = 1
            break
        }
    }

    for (let i = 0; i < M; ++i) {
        if (dp[0][i] === 1) {
            ans = 1
            break
        }
    }

    for (let i = 1; i < N; ++i) {
        for (let j = 1; j < M; ++j) {
            if (dp[i][j] === 1) {
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = Math.max(dp[i][j], ans)
            }
        }
    }

    console.log(ans**2)
})
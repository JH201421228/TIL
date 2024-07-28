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
    const [N, K] = input[0].split(' ').map(Number)
    const dp = Array(K+1).fill(0)
    let c

    for (let i = 0; i < N; ++i) {
        c = parseInt(input[i+1])

        if (c <= K) {
            dp[c] = 1

            for (let j = c+1; j < K+1; ++j) {
                if (dp[j-c] !== 0) {
                    if (dp[j] !== 0) {
                        dp[j] = Math.min(dp[j], dp[j-c]+1)
                    }
                    else {
                        dp[j] = dp[j-c]+1
                    }
                }
            }
        }
    }

    if (dp[K] !== 0) {
        console.log(dp[K])
    }
    else {
        console.log(-1)
    }
})
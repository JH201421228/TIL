const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


rl.on('line', line => {
    const S = line.split('').map(Number)
    const s = S.length
    
    const dp = Array(s).fill(0)
    dp[0] = 1

    if (S[0] === 0) {
        console.log(0)
        process.exit(0)
    }

    if (s >= 2) {
        if (S[1] === 0) {
            if (S[0] === 1 || S[0] === 2) {
                dp[1] = dp[0]
            }
            else {
                console.log(0)
                process.exit(0)
            }
        }
        else {
            dp[1] += 1
            if (S[0] * 10 + S[1] <= 26) {
                dp[1] += 1
            }
        }
    }

    for (let i = 2; i < s; ++i) {
        if (S[i] === 0) {
            if (S[i-1] === 1 || S[i-1] === 2) {
                dp[i] = dp[i-2]
            }
            else {
                console.log(0)
                process.exit(0)
            }
        }
        else {
            dp[i] = dp[i-1]
            if (S[i-1] === 0) {
                continue
            }
            else if (S[i-1] * 10 + S[i] <= 26) {
                dp[i] += dp[i-2]
                dp[i] %= 1000000
            }
        }
    }

    console.log(dp[s-1])
    rl.close()
})
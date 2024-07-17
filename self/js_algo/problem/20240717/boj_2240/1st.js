const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


rl.question('', line => {
    const [T, W] = line.split(' ').map(Number)
    let vals = []
    let prev = 0, cnt = 0, v = 0
    let inputNum = 0

    rl.on('line', line => {
        v = parseInt(line)

        if (inputNum === 0 && v === 1) {
            vals.push(0)
        }

        if (prev !== 0 && prev !== v) {
            vals.push(cnt)
            cnt = 0
        }

        ++cnt
        prev = v
        ++inputNum

        
        if (inputNum === T) {
            vals.push(cnt)

            const L = vals.length + 1
            const dp = Array.from({length: W+1}, () => Array(L).fill(0))

            for (let i = 1; i < L; i++) {
                if (i%2 === 1) {
                    dp[0][i] = dp[0][i-1]
                }
                else {
                    dp[0][i] = dp[0][i-1] + vals[i-1]
                }
            }

            let ans = dp[0][L-1]

            for (let i = 1; i < W+1; i++) {
                for (let j = 1; j < L; j++) {
                    if (i%2 === 1) {
                        if (j%2 === 1) {
                            dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]) + vals[j-1]
                        }
                        else {
                            dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1])
                        }
                    }
                    else {
                        if (j%2 === 1) {
                            dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1])
                        }
                        else {
                            dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]) + vals[j-1]
                        }
                    }
                }

                ans = Math.max(ans, dp[i][L-1])
            }

            console.log(ans)

            rl.close()
        }

    })

})
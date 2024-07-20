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
    const N = parseInt(input[0])
    const M = parseInt(input[2])
    const nums = input[1].split(' ').map(Number)

    const dp = Array.from({length: N}, () => Array(N).fill(0))
    const di = -1, dj = 1
    let n

    for (let i = 0 ; i < N; ++i) {
        dp[i][i] = 1
        if (i+1 < N && nums[i] === nums[i+1]) {
            dp[i][i+1] = 1
        }

        n = 1
        while (i+n*di >= 0 && i+n*dj < N) {
            if (dp[i+(n-1)*di][i+(n-1)*dj] === 0) {
                break
            }
            else if (nums[i+n*di] === nums[i+n*dj]) {
                dp[i+n*di][i+n*dj] = 1
            }

            ++n
        }

        n = 1
        while (i+n*di >= 0 && i+n*dj+1 < N) {
            if (dp[i+(n-1)*di][i+(n-1)*dj+1] === 0) {
                break
            }
            else if (nums[i+n*di] === nums[i+n*dj+1]) {
                dp[i+n*di][i+n*dj+1] = 1
            }

            ++n
        }
    }

    let S, E
    const output = []

    for (let i = 0; i < M; ++i) {
        [S, E] = input[i+3].split(' ').map(Number)
        output.push(dp[S-1][E-1])
    }

    console.log(output.join('\n'))
})
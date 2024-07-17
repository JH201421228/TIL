const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    ouput: process.stdout,
})

rl.question('', line => {
    const N = parseInt(line)
    let dp = Array(N+51).fill(0)
    let ans = 0
    let i = 0

    rl.on('line', line => {
        const [d, c] = line.split(' ').map(Number)
        dp[i+d] = Math.max(dp[i+d], ans+c)
        ans = Math.max(dp[i+1], ans)
        i++
        
        if (i === N) {
            console.log(ans)
            rl.close()
        }
    })
})
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
    const N = Number(input[0])
    const H = Array(N)
    const S = []

    for (let idx = 0; idx < N; ++idx) {
        H[idx] = Number(input[idx+1])
    }

    const area = (s, e) => {
        if (s === e) {
            return H[s]
        }

        const mid = Math.floor((s+e) / 2)
        let l = mid-1
        let r = mid+1
        let h = H[mid]
        let ans = H[mid]

        while (s <= l || r <= e) {
            if (s > l) {
                h = Math.min(h, H[r++])
            }
            else if (r > e) {
                h = Math.min(h, H[l--])
            }
            else if (H[l] >= H[r]) {
                h = Math.min(h, H[l--])
            }
            else if (H[l] < H[r]) {
                h = Math.min(h, H[r++])
            }

            ans = Math.max(ans, h*(r-l-1))
        }

        return Math.max(ans, Math.max(area(s, mid), area(mid+1, e)))
    }

    console.log(area(0, N-1))
})
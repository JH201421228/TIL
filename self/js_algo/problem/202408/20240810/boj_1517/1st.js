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
    const arr = input[1].split(' ').map(Number)
    const temp = Array(N).fill(0)
    let ans = 0

    const merge = (s, e) => {
        const mid = Math.floor((s + e) / 2)
        let i = s
        let j = mid+1
        let k = s
        let cnt = 0

        while (i <= mid && j <= e) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++]
                ans += cnt
            }
            else {
                temp[k++] = arr[j++]
                cnt += 1
            }
        }

        if (i <= mid) {
            while (i <= mid) {
                temp[k++] = arr[i++]
                ans += cnt
            }
        }
        else {
            while (j <= e) {
                temp[k++] = arr[j++]
            }
        }

        for (let idx = s; idx <= e; ++idx) {
            arr[idx] = temp[idx]
        }
    }

    const mergesort = (s, e) => {
        if (s < e) {
            const mid = Math.floor((s + e) / 2)
            mergesort(s, mid)
            mergesort(mid + 1, e)
            merge(s, e)
        }
    }

    mergesort(0, N-1)
    console.log(ans)
})
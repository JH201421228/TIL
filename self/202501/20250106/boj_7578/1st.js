const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let ans = 0

rl.on("line", l => {
    input.push(l)
})

rl.on("close", () => {
    function count(s, e) {
        const tmp = []
        const mid = (s+e) >> 1
        let i = s, j = mid+1, cnt = mid-s+1

        while (i < mid+1 && j < e+1) {
            if (arr[i] > arr[j]) {
                tmp.push(arr[j++])
                ans += cnt
            }
            else {
                tmp.push(arr[i++])
                --cnt
            }
        }

        while (i < mid+1) tmp.push(arr[i++])
        while (j < e+1) tmp.push(arr[j++])

        for (let k = s; k < e+1; ++k) {
            arr[k] = tmp[k-s]
        }
    }

    function merge(s, e) {
        if (s < e) {
            const mid = (s+e) >> 1
            merge(s, mid)
            merge(mid+1, e)
            count(s, e)
        }
    }

    const N = Number(input[0])

    const temp = input[1].split(' ').map(Number)
    const arr = input[2].split(' ').map(Number)
    const T = Array(1000001)

    for (let i = 0; i < N; ++i) {
        T[temp[i]] = i
    }

    for (let i = 0; i < N; ++i) {
        arr[i] = T[arr[i]]
    }

    merge(0, N-1)

    console.log(ans)
})
const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    const N = Number(input[0])
    const temp = [[0, 0]]
    let cnt = 0
    const nums = [0]
    const G = Array.from({length: 200001}, () => [])
    let O = 0
    let grn = 0
    let S = []
    const V = Array(200001).fill(0)
    const F = Array(200001).fill(0)

    const scc = n => {
        let p = V[n] = ++O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) {
                p = Math.min(p, scc(x))
            }
            else if (F[x] === 0) {
                p = Math.min(p, V[x])
            }
        }

        if (p == V[n]) {
            ++grn
            while (true) {
                const o = S.pop()
                F[o] = grn
                if (o == n) {
                    break
                }
            }
        }

        return p
    }

    for (let i = 0; i < N; ++i) {
        const tmp = input[i+1].split(' ').map(Number)

        if (tmp[0] === 1) {
            temp.push([tmp[1], tmp[2]])
            ++cnt
        }
        else {
            nums.push(cnt)
        }
    }

    let s = 0
    let e = nums.length-1

    while (s <= e) {
        const mid = (s+e) >> 1
        let is_break = false
        O = 0
        grn = 0
        S = []

        for (let i = 0; i < 200001; ++i) {
            G[i] = []
            V[i] = 0
            F[i] = 0
        }

        for (let i = 1; i <= nums[mid]; ++i) {
            const [a, b] = temp[i]
            
            if (a < 0) {
                if (b < 0) {
                    G[-a].push(200001+b)
                    G[-b].push(200001+a)
                }
                else {
                    G[-a].push(b)
                    G[200001-b].push(200001+a)
                }
            }
            else {
                if (b < 0) {
                    G[200001-a].push(200001+b)
                    G[-b].push(a)
                }
                else {
                    G[200001-a].push(b)
                    G[200001-b].push(a)
                }
            }
        }

        for (let i = 1; i < 200001; ++i) {
            if (V[i] === 0) {
                scc(i)
            }
        }

        for (let i = 1; i < 100001; ++i) {
            if (F[i] === F[200001-i]) {
                e = mid-1
                is_break = !is_break
                break
            }
        }
        if (!is_break) {
            s = mid+1
        }
    }

    for (let i = 0; i < e; ++i) {
        console.log("YES DINNER")
    }
    for (let i = 0; i < nums.length-e-1; ++i) {
        console.log("NO DINNER")
    }
})
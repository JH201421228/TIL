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
    let nums = [0]
    for (let i = 0; i < N; ++i) {
        nums.push(Number(input[i+1]))
    }

    let tree1 = Array(4*N).fill(0)
    let tree2 = Array(4*N).fill(0)

    const I1 = (s, e, idx) => {
        if (s >= e) {
            tree1[idx] = nums[s]
            return tree1[idx]
        }

        let mid = Math.floor((s+e)/2)
        tree1[idx] = Math.min(I1(s, mid, idx*2), I1(mid+1, e, idx*2+1))
        return tree1[idx]
    }
    
    const I2 = (s, e, idx) => {
        if (s >= e) {
            tree2[idx] = nums[s]
            return tree2[idx]
        }

        let mid = Math.floor((s+e)/2)
        tree2[idx] = Math.max(I2(s, mid, idx*2), I2(mid+1, e, idx*2+1))
        return tree2[idx]
    } 

    const S1 = (s, e, l, r, idx) => {
        if (s > r || e < l) {
            return Infinity
        }

        if (s >= l && e <= r) {
            return tree1[idx]
        }

        let mid = Math.floor((s+e)/2)
        return Math.min(S1(s, mid, l, r, idx*2), S1(mid+1, e, l, r, idx*2+1))
    }

    const S2 = (s, e, l, r, idx) => {
        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return tree2[idx]
        }

        let mid = Math.floor((s+e)/2)
        return Math.max(S2(s, mid, l, r, idx*2), S2(mid+1, e, l, r, idx*2+1))
    }
    
    I1(1, N, 1)
    I2(1, N, 1)

    for (let i = 0; i < M; ++i) {
        let [a, b] = input[N+1+i].split(' ').map(Number)
        console.log(S1(1, N, a, b, 1), S2(1, N, a, b, 1))
    }

    return
})
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const G = Array.from({length: 10001}, () => [])
const C = Array(10001).fill(0)
const V = Array(10001).fill(0)
const Ss = Array.from({length: 101}, () => Array(101).fill(0))
const Sg = Array.from({length: 101}, () => Array(101).fill(0))

const B = (n) => {
    for (let x of G[n]) {
        if (V[x] === 1) {
            continue
        }
        V[x] = 1

        if (C[x] === 0 || B(C[x])) {
            C[x] = n
            return true
        }
    }

    return false
}

rl.question('', line => {
    const [N, M] = line.split(' ').map(Number)

    let S = []
    let inputLines = 0

    rl.on('line', line => {
        S.push(line.trim())
        inputLines++
        
        if (inputLines === N) {
            let cnt_s = 0, cnt_g = 0
            for (let i = 0; i < N; i++) {
                for (let j = 0; j < M; j++) {
                    if (S[i][j] === 'S') {
                        Ss[i][j] = ++cnt_s
                    }
                    else if (S[i][j] === 'G') {
                        Sg[i][j] = ++cnt_g
                    }
                }
            }

            const delta = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            for (let i = 0; i < N; i++) {
                for (let j = 0; j < M; j++) {
                    if (S[i][j] === 'S') {
                        for (let d of delta) {
                            const ii = i+d[0], jj = j+d[1]
                            if (ii >= 0 && ii < N && jj >= 0 && jj < M) {
                                if (S[ii][jj] === 'G') {
                                    if ((i + 2 * d[0] >= 0 && i + 2 * d[0] < N && j + 2 * d[1] >= 0 && j + 2 * d[1] < M && S[i + 2 * d[0]][j + 2 * d[1]] === 'M') || (i - d[0] >= 0 && i - d[0] < N && j - d[1] >= 0 && j - d[1] < M && S[i - d[0]][j - d[1]] === 'M')) {
                                    G[Ss[i][j]].push(Sg[ii][jj])
                                    }
                                }
                            }
                        }
                    }
                }
            }

            let ans = 0
            for (let i = 1; i <= cnt_s; i++) {
                V.fill(0, 0, cnt_g+1)
                if (B(i)) {
                    ++ans
                }
            }

            console.log(ans)

            rl.close()
        }
    })
})
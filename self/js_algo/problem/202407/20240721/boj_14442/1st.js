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
    const [N, M, K] = input[0].split(' ').map(Number)

    if (N === 1 && M === 1) {
        console.log(1)
        return
    }

    const G = []
    for (let i = 0; i < N; ++i) {
        G.push(input[i + 1].split('').map(Number))
    }

    const V = Array.from({ length: N }, () =>
        Array.from({ length: M }, () =>
            Array(K + 1).fill(0)
        )
    )
    V[0][0][0] = 1

    const delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    const q = [{ i: 0, j: 0, k: 0 }]

    while (q.length) {
        const { i, j, k } = q.shift()

        for (const [di, dj] of delta) {
            const ii = i + di, jj = j + dj
            if (ii >= 0 && ii < N && jj >= 0 && jj < M) {
                if (G[ii][jj] === 0 && V[ii][jj][k] === 0) {
                    V[ii][jj][k] = V[i][j][k] + 1
                    q.push({ i: ii, j: jj, k: k })
                    if (ii === N - 1 && jj === M - 1) {
                        console.log(V[ii][jj][k])
                        return
                    }
                }
                else if (G[ii][jj] === 1 && k < K && V[ii][jj][k + 1] === 0) {
                    V[ii][jj][k + 1] = V[i][j][k] + 1
                    q.push({ i: ii, j: jj, k: k + 1 })
                    if (ii === N - 1 && jj === M - 1) {
                        console.log(V[ii][jj][k + 1])
                        return
                    }
                }
            }
        }
    }

    console.log(-1)

    return
})
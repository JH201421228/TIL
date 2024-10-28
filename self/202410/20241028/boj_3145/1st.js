const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    const [R, C] = input[0].split(" ").map(Number)

    const M = []
    const names = [""]
    const cities = [[0, 0]]
    const delta = [[1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, -1], [-1, 1]]
    let names_num = 0
    let cities_num = 0
    let check = false
    let temp = ""

    const B = n => {
        for (let x of G[n]) {
            if (V[x] !== 0) {
                continue
            }
            V[x] = 1

            if (F[x] === 0 || B(F[x])) {
                F[x] = n
                return true
            }
        }

        return false
    }

    for (let i = 0; i < R; ++i) {
        M.push(input[i+1].split(""))

        if (check) {
            check = false
            names.push(temp)
            temp = ""
        }

        for (let j = 0; j < C; ++j) {
            if (M[i][j] === '.') {
                if (check) {
                    check = false
                    names.push(temp)
                    temp = ""
                }
            }
            else if (M[i][j] === 'x') {
                if (check) {
                    check = false
                    names.push(temp)
                    temp = ""
                }
                ++cities_num
                cities.push([i, j])
            }
            else {
                if (!check) {
                    ++names_num
                    check = !check
                }
                temp += M[i][j]
                M[i][j] = names_num
            }
        }
    }

    const G = Array.from({length: cities_num+1}, () => [])
    const V = Array(names_num+1).fill(0)
    const F = Array(names_num+1).fill(0)

    if (temp !== "") {
        names.push(temp)
    }

    for (let i = 1; i < cities_num+1; ++i) {
        for (let d of delta) {
            const x = cities[i][0] + d[0]
            const y = cities[i][1] + d[1]

            if (x >= 0 && x < R && y >= 0 && y < C) {
                const n = M[x][y]
                if (n !== 'x' && n !== '.' && !G[i].includes(n)) {
                    G[i].push(n)
                }
            }
        }
    }

    for (let i = 1; i < cities_num+1; ++i) {
        for (let j = 1; j < names_num+1; ++j) {
            V[j] = 0
        }
        B(i)
    }

    for (let i = 1; i < names_num+1; ++i) {
        console.log(...cities[F[i]].map(val => val+1), names[i])
    }
})
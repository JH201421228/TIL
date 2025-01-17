const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on("line", l => {
    input.push(l)
})

rl.on("close", () => {
    function greedy () {

    }
    [1,2,3,4,5].reduce((a, b) => a + b);
    [1,2,3,4,5].reduce((a, b) => a + b);
    let ans = 0
    const idxs = [[0, 3], [1, 2], [0, 2], [1, 3], [0, 1], [2, 3]]
    const arr = input[1].split(' ')

    // arr.reduce((acc, cur) => )

    console.log(typeof arr[0])
    console.log(typeof +(arr[0]))
    console.log(typeof BigInt(Number(arr[0])))
    console.log(typeof BigInt(arr[0]))
    console.log(typeof 1n)
    console.log('b' + 'a' + +'a' + 'a')
})
const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

rl.on('line', (line) => {
    const numbers = line.split(' ').map(Number)

    console.log(numbers[0] + numbers[1])
    console.log(numbers[0] - numbers[1])
    console.log(numbers[0] * numbers[1])
    console.log(Math.floor(numbers[0] / numbers[1]))
    console.log(numbers[0] % numbers[1])

    rl.close()
})
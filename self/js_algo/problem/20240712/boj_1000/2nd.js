const { type } = require('os');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

rl.on('line', (line) => {
    const numbers = line.split(' ').map(Number);
    const sum = numbers.reduce((acc, cur) => acc + cur, 0);
    console.log(sum)
    rl.close()
})
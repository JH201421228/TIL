const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];
let z = 0;

rl.on("line", l => input.push(l))

rl.on("close", () => {
    let ans = "1999\n";

    for (let i = 0; i < 999; ++i) ans += "1 ";
    for (let i = 0; i < 1000; ++i) ans += "1000 ";

    console.log(ans);
})

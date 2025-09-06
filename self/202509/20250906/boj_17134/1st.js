const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


class Complex {
    constructor(r = 0, i = 0) {
        this.real = r;
        this.image = i;
    }

    addComplex(c) {
        return new Complex(this.real + c.real, this.image + c.image);
    }

    subComplex(c) {
        return new Complex(this.real - c.real, this.image - c.image);
    }

    mulComplex(c) {
        return new Complex(this.real * c.real - this.image * c.image, 
                            this.image * c.real + this.real * c.image)
    }
}


function fft(u, inv) {
    for (let i = 1, j = 0; i < N; ++i) {
        let bit = N >>> 1;
        while ((j & bit) > 0) {
            j ^= bit;
            bit >>>= 1;
        }
        j ^= bit;

        if (i < j) {
            const temp_i = u[i];
            const temp_j = u[j];
            u[i] = temp_j; u[j] = temp_i;
        }
    }

    let k = 1;
    while (k < N) {
        let ang = (Math.PI/k) * (inv? 1.0 : -1.0);
        let w = new Complex(Math.cos(ang), Math.sin(ang));
        for (let i = 0; i < N; i += (k<<1)) {
            let wp = new Complex(1.0, 0.0);
            for (let j = 0; j < k; ++j) {
                let x = u[i+j];
                let y = u[i+j+k].mulComplex(wp);

                u[i+j] = x.addComplex(y);
                u[i+j+k] = x.subComplex(y);

                wp = wp.mulComplex(w);
            }
        }

        k <<= 1;
    }

    if (inv) {
        for (let idx = 0; idx < N; ++idx) u[idx] = new Complex(u[idx].real/N, u[idx].image/N);
    }

    return;
}


function fft_wrapper(u, v) {
    fft(u, false);
    fft(v, false);

    for (let idx = 0; idx < N; ++idx) u[idx] = u[idx].mulComplex(v[idx]);

    fft(u, true);

    return;
}


const N = 1 << 21;
const n = 1000000;
const prime = Array(N);
const semi = Array(N);

for (let i = 0; i < N; ++i) {
    prime[i] = new Complex(0.0, 0.0);
    semi[i] = new Complex(0.0, 0.0);
}

for (let i = 0; i < n+1; ++i) prime[i].real = 1.0;


function sieve() {
    prime[0].real = 0.0;
    prime[1].real = 0.0;

    for (let i = 2; i < Math.sqrt(n) + 1; ++i) {
        if (prime[i].real == 1.0) {
            for (let j = i*i; j < n+1; j += i) {
                prime[j].real = 0.0;
            }
        }
    }

    prime[2].real = 0.0;

    for (let i = 0; i < n+1; ++i) {
        if (prime[i].real == 1.0 && 2*i < n+1) semi[2*i].real = 1.0;
    }

    semi[4].real = 1.0;

    return;
}


const input = [];
let z = 0;

rl.on("line", l => input.push(l))

rl.on("close", () => {
    sieve();

    fft_wrapper(prime, semi);

    const t = Number(input[z++]);
    for (let i = 0; i < t; ++i) {
        console.log(Math.round(prime[Number(input[z++])].real))
    }
})
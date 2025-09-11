const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

class Complex {
    constructor(r = 0, i = 0) {
        this.real = r; this.image = i;
    }

    addComplex(c) {
        return new Complex(this.real + c.real, this.image + c.image);
    }

    subComplex(c) {
        return new Complex(this.real - c.real, this.image - c.image);
    }

    mulComplex(c) {
        return new Complex(this.real * c.real - this.image * c.image, this.real * c.image + this.image * c.real);
    }
}

const PI = Math.PI;
const n = 1_000_000;
const N = 1 << 20;
let T;

const isPrime = Array(1<<21);
const oddPrime = Array(1<<20);

const input = [];
let z = 0;


function fft(v, inv) {
    for (let i = 1, j = 0; i < N; ++i) {
        let b = N >> 1;
        while ((j & b) > 0) {
            j ^= b;
            b >>>= 1;
        }
        j ^= b;

        if (i < j) {
            const tmp_i = v[i];
            const tmp_j = v[j];

            v[i] = tmp_j; v[j] = tmp_i;
        }
    }

    let k = 1;
    while (k < N) {
        let a = (PI/k) * (inv? 1.0 : -1.0);
        let w = new Complex(Math.cos(a), Math.sin(a));

        for (let i = 0; i < N; i += (k << 1)) {
            let wp = new Complex(1, 0);
            for (let j = 0; j < k; ++j) {
                let x = v[i+j];
                let y = v[i+j+k].mulComplex(wp);

                v[i+j] = x.addComplex(y);
                v[i+j+k] = x.subComplex(y);

                wp = wp.mulComplex(w);
            }
        }

        k <<= 1;
    }

    if (inv) {
        for (let idx = 0; idx < N; ++idx) v[idx] = new Complex(v[idx].real/N, v[idx].image/N);
    }

    return;
}


function fft_wrapper(u) {
    fft(u, false);

    for (let i = 0; i < N; ++i) u[i] = u[i].mulComplex(u[i]);

    fft(u, true);

    return;
}


function sieve() {
    for (let i = 0; i < n; ++i) isPrime[i] = new Complex(1, 0);
    for (let i = n; i < isPrime.length; ++i) isPrime[i] = new Complex(0, 0);
    for (let i = 0; i < oddPrime.length; ++i) oddPrime[i] = new Complex(0, 0);

    isPrime[0].real = 0;
    isPrime[1].real = 0;

    for (let i = 2; i < Math.sqrt(n)+1; ++i) {
        if (isPrime[i].real === 1) {
            for (let j = i*i; j < n+1; j += i) {
                isPrime[j].real = 0;
            }
        }
    }

    for (let idx = 0; idx < N; ++idx) {
        oddPrime[idx].real = isPrime[idx*2+1].real;
    }

    return;
}


rl.on("line", l => input.push(l))

rl.on("close", () => {
    sieve();

    fft_wrapper(oddPrime);

    T = Number(input[z++]);
    for (let i = 0; i < T; ++i) {
        const tmp = Number(input[z++]);

        if (tmp === 4) {
            console.log(1);
        }
        else {
            console.log(
                Math.round(oddPrime[(tmp-2)>>>1].real+1)>>>1
            )
        }
    }
})
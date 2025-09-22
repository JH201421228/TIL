const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


class Complex {
    constructor(r, i) {
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
        return new Complex(this.real * c.real - this.image * c.image, this.real * c.image + this.image * c.real);
    }
}


function fft(v, inv) {
    const N = v.length;

    for (let i = 1, j = 0; i < N; ++i) {
        let b = N >>> 1;
        while ((j&b) > 0) {
            j ^= b;
            b >>>= 1;
        }
        j ^= b;

        if (i < j) {
            let temp_i = v[i], temp_j = v[j];
            v[i] = temp_j; v[j] = temp_i;
        }
    }

    let k = 1;
    while (k < N) {
        let a = (Math.PI/k) * (inv? 1 : -1);
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
        for (let i = 0; i < N; ++i) v[i] = new Complex(v[i].real/N, v[i].image/N);
    }

    return;
}


function fft_wrapper(u, v, n) {
    let N = u.length;

    fft(u, false);

    for (let i = 0; i < N; ++i) {
        u[i] = u[i].mulComplex(u[i]);
    }

    fft(u, true);

    let ans = 0;

    for (let i = 0; i < N; ++i) {
        let tmp = Math.round(u[i].real);
        if (tmp > 0 && v[i%n] > 0) {
            if (i%2 > 0) {
                ans += (tmp/2) * v[i%2];
            }
            else {
                ans += ((tmp-v[i/2])/2 + v[i/2]) * v[i%n];
            }
        }
    }

    console.log(ans);

    return;
}


function solve(N) {
    let M = 1;
    while (M < N) M <<= 1;
    M <<= 1;

    const u = Array(M);
    for (let i = 0; i < M; ++i) u[i] = new Complex(0, 0);

    const v = Array(N).fill(0);

    for (let i = 1; i < N; ++i) {
        ++u[i*i%N].real;
        ++v[i*i%N];
    }

    fft_wrapper(u, v, N);

    return;
}


rl.on("line", l => input.push(l));

rl.on("close", () => {
    solve(Number(input[z++]))
})
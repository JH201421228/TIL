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
        return new Complex(
            this.real * c.real - this.image * c.image,
            this.real * c.image + this.image * c.real
        )
    }
}


function fft(v, n, inv) {
    for (let i = 1, j = 0; i < n; ++i) {
        let bit = n >>> 1;
        while ((j & bit) > 0) {
            j ^= bit;
            bit >>>= 1;
        }
        j ^= bit;

        if (i < j) {
            const v_temp = v[i];
            v[i] = v[j];
            v[j] = v_temp;
        }
    }

    let k = 1;
    while (k < n) {
        const ang = (Math.PI / k) * (inv? 1.0 : -1.0);
        let w = new Complex(Math.cos(ang), Math.sin(ang));
        for (let i = 0; i < n; i += (k << 1)) {
            let wp = new Complex(1.0, 0.0);
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
        for (let idx = 0; idx < n; ++idx) v[idx] = new Complex(v[idx].real / n, v[idx].image / n);
    }

    return;
}


function fft_wrapper(u, v, res, n) {
    fft(v, n, false);
    fft(u, n ,false);

    for (let idx = 0; idx < n; ++idx) res[idx] = u[idx].mulComplex(v[idx]);

    fft(res, n, true);

    let ans = 0;

    for (let idx = 0; idx < n; ++idx) ans = Math.max(ans, Number(Math.round(res[idx].real)));

    console.log(ans);

    return;
}


const input = [];
let z = 0;

rl.on("line", l => input.push(l))

rl.on("close", () => {
    const N = Number(input[z++]);
    
    let n = 1;
    while (n < 2*N) n <<= 1;

    const u = Array(n).fill(new Complex(0.0, 0.0));
    const v = Array(n).fill(new Complex(0.0, 0.0));
    const res = Array(n).fill(new Complex(0.0, 0.0));

    const temp_u = input[z++].split(' ').map(Number);
    for (let idx = 0; idx < N; ++idx) {
        u[idx] = new Complex(temp_u[idx], 0.0);
        u[idx+N] = u[idx];
    }

    const temp_v = input[z++].split(' ').map(Number);
    for (let idx = 0; idx < N; ++idx) v[N-1-idx] = new Complex(temp_v[idx], 0.0);

    fft_wrapper(u, v, res, n);

    return;
})
const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


class Complex {
    constructor (r, i) {
        this.real = r; this.image = i;
    }

    addComplex(c) {
        return new Complex(this.real+c.real, this.image+c.image);
    }

    subComplex(c) {
        return new Complex(this.real-c.real, this.image-c.image);
    }

    mulComplex(c) {
        return new Complex(this.real*c.real - this.image*c.image, this.real*c.image + this.image*c.real);
    }
}


const PI = Math.PI;
const input = [];
let z = 0;
let N = 0;


function fft(v, inv) {
    for (let i = 1, j = 0; i < N; ++i) {
        let b = N >>> 1;
        while ((j&b) > 0) {
            j ^= b;
            b >>>= 1;
        }
        j ^= b;

        if (i < j) {
            const temp_i = v[i];
            const temp_j = v[j];

            v[i] = temp_j;
            v[j] = temp_i;
        }
    }

    let k = 1;
    while (k < N) {
        let a = (PI/k) * (inv? 1 : -1);
        let w = new Complex(Math.cos(a), Math.sin(a));

        for (let i = 0; i < N; i += (k<<1)) {
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
        for (let i = 0; i < N; ++i) {
            v[i] = new Complex(v[i].real/N, v[i].image/N);
        }
    }

    return;
}


function fft_wrapper(u, v) {
    fft(u, false);
    fft(v, false);

    for (let i = 0; i < N; ++i) {
        u[i] = u[i].mulComplex(v[i]);
    }

    fft(u, true);

    let ans = 0;

    for (let i = 0; i < N; ++i) {
        ans = Math.max(ans, Number(Math.round(u[i].real)));
    }

    console.log(ans);

    return;
}


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const u_temp = input[z++];
    const v_temp = input[z++];

    N = 1;
    while (N < u_temp.length) {
        N <<= 1;
    }
    N <<= 1;

    const u = Array(N)
    const v = Array(N)

    for (let i = 0; i < N; ++i) {
        u[i] = new Complex(0, 0);
        v[i] = new Complex(0, 0);
    }

    const u_len = u_temp.length;

    for (let i = 0; i < u_len; ++i) {
        u[i].real = Number(u_temp[i]);
        u[i+u_len].real = Number(u_temp[i]);
        v[u_len-1-i].real = Number(v_temp[i]);
    }

    fft_wrapper(u, v);

    return;
})
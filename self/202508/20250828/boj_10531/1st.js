const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];
let z = 0;

function bitReversPermute(re, im) {
    const n = re.length;
    for (let i = 1, j = 0; i < n; ++i) {
        let bit = n>>>1;
        for (; j & bit; bit>>>=1) j ^= bit;
        j ^= bit;
        if (i < j) {
            const tr = re[i]; re[i] = re[j]; re[j] = tr;
            const ti = im[i]; im[i] = im[j]; im[j] = ti;
        }
    }

    return [re, im];
}

function fft(re, im, invert) {
    const n = re.length;
    [re, im] = bitReversPermute(re, im);

    for (let len = 2; len <= n; len <<= 1) {
        const ang = (2*Math.PI/len) * (invert ? -1.0 : 1.0);
        const wlenRe = Math.cos(ang);
        const wlenIm = Math.sin(ang);
        for (let i = 0; i < n; i += len) {
            let wRe = 1.0; let wIm = 0.0;
            const half = len >>> 1;

            for (let j = 0; j < half; ++j) {
                const uRe = re[i+j], uIm = im[i+j];
                const vRe = re[i+j+half], vIm = im[i+j+half];

                const tRe = vRe*wRe - vIm*wIm;
                const tIm = vIm*wRe + vRe*wIm;

                re[i+j] = uRe+tRe;
                im[i+j] = uIm+tIm;
                re[i+j+half] = uRe-tRe;
                im[i+j+half] = uIm-tIm;

                const nwRe = wRe*wlenRe - wIm*wlenIm;
                const nwIm = wRe*wlenIm + wIm*wlenRe;
                wRe = nwRe; wIm = nwIm;
            }
        }
    }

    if (invert) {
        for (let idx = 0; idx < n; ++idx) {
            re[idx] /= n;
            im[idx] /= n;
        }
    }

    return [re, im];
}


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const N = Number(input[z++]);
    const shot = Array(N);
    for (let idx = 0; idx < N; ++idx) shot[idx] = Number(input[z++]);

    const M = Number(input[z++]);
    const distance = Array(M);
    for (let idx = 0; idx < M; ++idx) distance[idx] = Number(input[z++]);

    let maxS = 0;
    for (let x of shot) if (x > maxS) maxS = x;

    let base = maxS+1;
    let n = 1;
    while (n < base<<1) n <<= 1;

    let re = new Float64Array(n);
    let im = new Float64Array(n);

    re[0] = 1.0;
    for (let idx = 0; idx < N; ++idx) {
        const x = shot[idx];
        if (x >= 0 && x < n) re[x] = 1.0;
    }

    [re, im] = fft(re, im, false);

    for (let i = 0; i < n; ++i) {
        const a = re[i], b = im[i];
        const nr = a*a-b*b;
        const ni = 2*a*b;
        re[i] = nr;
        im[i] = ni;
    }

    [re, im] = fft(re, im, true);

    let ans = 0;
    for (let i = 0; i < M; ++i) {
        const d = distance[i];
        if (d >= 0 && d < n) {
            const cnt = Math.round(re[d]);
            if (cnt > 0) ans += 1;
        }
    }

    console.log(ans)
})
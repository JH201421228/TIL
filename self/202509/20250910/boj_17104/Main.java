import java.io.*;
import java.util.*;


public class Main {

    static class Complex {
        public double real = 0;
        public double image = 0;

        Complex(double r, double i) {
            real = r; image = i;
        }

        public Complex addComplex(Complex c) {
            Complex res = new Complex(0, 0);
            res.real = real + c.real;
            res.image = image + c.image;

            return res;
        }

        public Complex subComplex(Complex c) {
            Complex res = new Complex(0, 0);
            res.real = real - c.real;
            res.image = image - c.image;

            return res;
        }

        public Complex mulComplex(Complex c) {
            Complex res = new Complex(0, 0);
            res.real = real * c.real - image * c.image;
            res.image = image * c.real + real * c.image;

            return res;
        }
    }

    static final double PI = Math.acos(-1.0);
    static int n = 1000000;
    static int N = 1 << 20;
    static int T;

    static Complex[] isPrime = new Complex[1<<21];
    static Complex[] oddPrime = new Complex[1<<20];

    static void fft(Complex[] v, boolean inv) {
        for (int i = 1, j = 0; i < N; ++i) {
            int b = N >> 1;
            while ((j & b) > 0) {
                j ^= b;
                b >>= 1;
            }
            j ^= b;
            
            if (i < j) {
                Complex tmp_i = v[i];
                Complex tmp_j = v[j];

                v[i] = tmp_j; v[j] = tmp_i;
            }
        }

        int k = 1;
        while (k < N) {
            double a = (PI/k) * (inv? 1.0 : -1.0);
            Complex w = new Complex(Math.cos(a), Math.sin(a));

            for (int i = 0; i < N; i += (k<<1)) {
                Complex wp = new Complex(1.0, 0.0);
                for (int j = 0; j < k; ++j) {
                    Complex x = v[i+j];
                    Complex y = v[i+j+k].mulComplex(wp);

                    v[i+j] = x.addComplex(y);
                    v[i+j+k] = x.subComplex(y);

                    wp = wp.mulComplex(w);
                }
            }

            k <<= 1;
        }

        if (inv) {
            for (int idx = 0; idx < N; ++idx) v[idx] = new Complex(v[idx].real/N, v[idx].image/N);
        }

        return;
    }


    static void fft_wrapper(Complex u[]) {
        fft(u, false);

        for (int i = 0; i < N; ++i) u[i] = u[i].mulComplex(u[i]);

        fft(u, true);

        return;
    }


    static void sieve() {
        for (int i = 0; i < n; ++i) isPrime[i] = new Complex(1, 0);
        for (int i = n; i < isPrime.length; ++i) isPrime[i] = new Complex(0, 0);
        for (int i = 0; i < oddPrime.length; ++i) oddPrime[i] = new Complex(0, 0);

        isPrime[0].real = 0;
        isPrime[1].real = 0;

        for (int i = 2; i < Math.sqrt(n)+1; ++i) {
            if (isPrime[i].real == 1) {
                for (int j = i*i; j < n+1; j += i) {
                    isPrime[j].real = 0;
                }
            }
        }

        for (int idx = 0; idx < N; ++idx) {
            oddPrime[idx].real = isPrime[idx*2+1].real;
        }

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        sieve();

        fft_wrapper(oddPrime);

        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; ++i) {
            int tmp = Integer.parseInt(br.readLine());

            if (tmp == 4) {
                System.out.println(1);
            }
            else {
                System.out.println((int) Math.round(oddPrime[(int) (tmp-2)/2].real + 1)/2);
            }
        }
    }
}

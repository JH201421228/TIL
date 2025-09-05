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
            res.real = real*c.real - image*c.image;
            res.image = real*c.image + image*c.real;
            return res;
        }
    }

    static double PI = Math.acos(-1.0);
    static int N = 1 << 21, n = 1000000;
    static Complex[] prime, semi;

    static void sieve() {
        prime[0].real = 0.0;
        prime[1].real = 0.0;

        for (int i = 2; i < Math.sqrt(n) + 1; ++i) {
            if (prime[i].real == 1.0) {
                for (int j = i*i; j < n+1; j += i) {
                    prime[j].real = 0.0;
                }
            }
        }

        prime[2].real = 0.0;

        return;
    }

    static void fft(Complex[] u, boolean inv) {
        for (int i = 1, j = 0; i < N; ++i) {
            int bit = N >> 1;
            while ((j & bit) > 0) {
                j ^= bit;
                bit >>= 1;
            }
            j ^= bit;

            if (i < j) {
                Complex temp_i = u[i];
                Complex temp_j = u[j];
                u[i] = temp_j; u[j] = temp_i;
            }
        }

        int k = 1;
        while (k < N) {
            double ang = (PI/k) * (inv? 1.0 : -1.0);
            Complex w = new Complex(Math.cos(ang), Math.sin(ang));
            for (int i = 0; i < N; i += (k<<1)) {
                Complex wp = new Complex(1.0, 0.0);
                for (int j = 0; j < k; ++j) {
                    Complex x = u[i+j];
                    Complex y = u[i+j+k].mulComplex(wp);

                    u[i+j] = x.addComplex(y);
                    u[i+j+k] = x.subComplex(y);

                    wp = wp.mulComplex(w);
                }
            }

            k <<= 1;
        }

        if (inv) {
            for (int idx = 0; idx < N; ++idx) u[idx] = new Complex(u[idx].real/N, u[idx].image/N);
        }

        return;
    }

    static void fft_wrapper(Complex[] u, Complex[] v) {
        fft(u, false);
        fft(v, false);

        for (int idx = 0; idx < N; ++idx) u[idx] = u[idx].mulComplex(v[idx]);

        fft(u, true);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        prime = new Complex[N];
        semi = new Complex[N];

        for (int i = 0; i < N; ++i) {
            prime[i] = new Complex(0.0, 0.0);
            semi[i] = new Complex(0.0, 0.0);
        }

        for (int i = 0; i < n+1; ++i) prime[i].real = 1.0;

        sieve();

        for (int i = 0; i < n+1; ++i) {
            if (prime[i].real == 1.0 && 2*i < n+1) semi[2*i].real = 1.0;
        }
        semi[4].real = 1.0;

        fft_wrapper(prime, semi);
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; ++i) {
            // int q = Integer.parseInt(br.readLine());
            System.out.println(Math.round(prime[Integer.parseInt(br.readLine())].real));
        }
    }
}

import java.io.*;
import java.util.*;


public class Main {
    static class Complex {
        public double real = 0;
        public double image = 0;

        Complex(double r, double i) {
            real = r;
            image = i;
        }

        public Complex addComplex(Complex c) {
            Complex c0 = new Complex(0, 0);
            c0.real = real + c.real;
            c0.image = image + c.image;
            return c0;
        }

        public Complex subComplex(Complex c) {
            Complex c0 = new Complex(0, 0);
            c0.real = real - c.real;
            c0.image = image - c.image;
            return c0;
        }

        public Complex mulComplex(Complex c) {
            Complex c0 = new Complex(0, 0);
            c0.real = real * c.real - image * c.image;
            c0.image = real * c.image + image * c.real;
            return c0;
        }
    }

    static double PI = Math.acos(-1.0);
    static int N;
    static Complex[] u, v, res;

    static void fft(Complex[] v, int n, boolean inv) {
        for (int i = 1, j = 0; i < n; ++i) {
            int bit = n >> 1;
            while ((j & bit) > 0) {
                j ^= bit;
                bit >>= 1;
            }
            j ^= bit;

            if (i < j) {
                Complex v_temp = v[i];
                v[i] = v[j];
                v[j] = v_temp;
            }
        }

        int k = 1;
        while (k < n) {
            double ang = (PI/k) * (inv? 1.0 : -1.0);
            Complex w = new Complex(Math.cos(ang), Math.sin(ang));
            for (int i = 0; i < n; i += (k<<1)) {
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
            for (int idx = 0; idx < n; ++idx) v[idx] = new Complex(v[idx].real / n, v[idx].image / n);
        }

        return;
    }

    static void fft_wrapper(Complex[] u, Complex[] v, int n) {
        fft(v, n, false);
        fft(u, n, false);

        for (int idx = 0; idx < n; ++idx) res[idx] = u[idx].mulComplex(v[idx]);

        fft(res, n, true);

        int ans = 0;

        for (int idx = 0; idx < n; ++idx) ans = Math.max(ans, (int) Math.round(res[idx].real));

        System.out.println(ans);

        return;
    }

    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        int n = 1;
        while (n < 2*N) n <<= 1;
        n <<= 1;

        u = new Complex[n];
        v = new Complex[n];
        res = new Complex[n];

        for (int idx = 0; idx < n; ++idx) {
            u[idx] = new Complex(0.0, 0.0);
            v[idx] = new Complex(0.0, 0.0);
            res[idx] = new Complex(0.0, 0.0);
        }

        String[] u_temp = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) {
            u[idx] = new Complex(Double.parseDouble(u_temp[idx]), 0.0);
            u[idx+N] = u[idx];
        }

        String[] v_temp = br.readLine().split(" ");
        for (int idx = 0; idx < N; ++idx) v[N-1-idx] = new Complex(Double.parseDouble(v_temp[idx]), 0.0);

        fft_wrapper(u, v, n);

        return;
    }    
}

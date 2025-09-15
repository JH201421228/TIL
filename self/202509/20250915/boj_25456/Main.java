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
            res.image = real * c.image + image * c.real;

            return res;
        }
    }

    static Complex[] u, v;
    static int N;
    static double PI = Math.PI;

    static void fft(Complex[] v, boolean inv) {
        for (int i = 1, j = 0; i < N; ++i) {
            int b = N>>1;
            while ((j&b) > 0) {
                j ^= b;
                b >>= 1;
            }
            j ^= b;

            if (i < j) {
                Complex temp_i = v[i];
                Complex temp_j = v[j];

                v[i] = temp_j;
                v[j] = temp_i;
            }
        }

        int k = 1;
        while (k < N) {
            double a = (PI/k) * (inv? 1.0 : -1.0);
            Complex w = new Complex(Math.cos(a), Math.sin(a));

            for (int i = 0; i < N; i += (k<<1)) {
                Complex wp = new Complex(1, 0);
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
            for (int i = 0; i < N; ++i) {
                v[i] = new Complex(v[i].real / N, v[i].image / N);
            }
        }

        return;
    }


    static void fft_wrapper(Complex[] u, Complex[] v) {
        fft(u, false);
        fft(v, false);

        for (int i = 0; i < N; ++i) {
            u[i] = u[i].mulComplex(v[i]);
        }

        fft(u, true);

        int ans = 0;

        for (int i = 0; i < N; ++i) {
            ans = Math.max(ans, (int) Math.round(u[i].real));
        }

        System.out.println(ans);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] u_temp = br.readLine().split("");
        String[] v_temp = br.readLine().split("");

        N = 1;
        while (N < u_temp.length) {
            N <<= 1;
        }
        N <<= 1;

        u = new Complex[N];
        v = new Complex[N];

        for (int i = 0; i < N; ++i) {
            u[i] = new Complex(0, 0);
            v[i] = new Complex(0, 0);
        }

        int u_len = u_temp.length;

        for (int i = 0; i < u_len; ++i) {
            u[i] = new Complex(Integer.parseInt(u_temp[i]), 0);
            u[i+u_len] = new Complex(Integer.parseInt(u_temp[i]), 0);
            v[u_len-1-i] = new Complex(Integer.parseInt(v_temp[i]), 0);
        }

        fft_wrapper(u, v);

        return;
    }
}

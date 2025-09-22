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
            return new Complex(real + c.real, image + c.image);
        }

        public Complex subComplex(Complex c) {
            return new Complex(real - c.real, image - c.image);
        }

        public Complex mulComplex(Complex c) {
            return new Complex(real*c.real-image*c.image, real*c.image+image*c.real);
        }
    }

    static Complex[] u;
    static int[] v;
    static double PI = Math.PI;

    static void fft(Complex[] v, boolean inv) {
        int N = v.length;

        for (int i = 1, j = 0; i < N; ++i) {
            int b = N >> 1;
            while ((j&b) > 0) {
                j ^= b;
                b >>= 1;
            }
            j ^= b;

            if (i < j) {
                Complex temp_i = v[i], temp_j = v[j];
                v[i] = temp_j;
                v[j] = temp_i;
            }
        }

        int k = 1;
        while (k < N) {
            double a = (PI/k) * (inv? 1 : -1);
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
            for (int i = 0; i < N; ++i) v[i] = new Complex(v[i].real/N, v[i].image/N);
        }

        return;
    }

    static void fft_wrapper(Complex[] u, int[] v, int n) {
        int N = u.length;

        fft(u, false);

        for (int i = 0; i < N; ++i) {
            u[i] = u[i].mulComplex(u[i]);
        }

        fft(u, true);

        long ans = 0;

        for (int i = 0; i < N; ++i) {
            int tmp = (int) Math.round(u[i].real);
            if (tmp > 0 && v[i%n] > 0) {
                if (i%2 > 0) {
                    ans += (tmp/2) * v[i%n];
                }
                else {
                    ans += ((tmp-v[i/2])/2 + v[i/2]) * v[i%n];
                }
            }
        }

        System.out.println(ans);

        return;
    }

    static void solve(int N) {
        int M = 1;
        while (M < N) {
            M <<= 1;
        }
        M <<= 1;

        u = new Complex[M];
        for (int i = 0; i < M; ++i) u[i] = new Complex(0, 0);

        v = new int[N];
        Arrays.fill(v, 0);

        for (int i = 1; i < N; ++i) {
            ++u[(int) (1L*i*i%N)].real;
            ++v[(int) (1L*i*i%N)];
        }

        fft_wrapper(u, v, N);

        return;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        solve(Integer.parseInt(br.readLine()));

        return;
    }
}

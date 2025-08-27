import java.io.*;
import java.util.*;

public class Main {
    static final double PI = Math.acos(-1.0);

    static int N, M;
    static int[] shot, distance;
    static double[] re, im;

    static void fft(double[] re, double[] im, int n, boolean invert) {
        for (int i = 1, j = 0; i < n; ++i) {
            int bit = n >> 1;
            for (; (j & bit) != 0; bit >>= 1) j ^= bit;
            j ^= bit;

            if (i < j) {
                double tr = re[i]; re[i] = re[j]; re[j] = tr;
                double ti = im[i]; im[i] = im[j]; im[j] = ti;
            }
        }

        for (int len = 2; len <= n; len <<= 1) {
            double ang = 2.0 * PI / len * (invert ? -1.0 : 1.0);
            double wlenR = Math.cos(ang);
            double wlenI = Math.sin(ang);

            for (int i = 0; i < n; i += len) {
                double wr = 1.0, wi = 0.0;
                int half = len >> 1;

                for (int j = 0; j < half; ++j) {
                    int u = i+j;
                    int v = u+half;

                    double vr = re[v] * wr - im[v] * wi;
                    double vi = re[v] * wi + im[v] * wr;

                    double ur = re[u];
                    double ui = im[u];

                    re[u] = ur + vr;
                    im[u] = ui + vi;

                    re[v] = ur - vr;
                    im[v] = ui - vi;

                    double nwr = wr * wlenR - wi * wlenI;
                    double nwi = wr * wlenI + wi * wlenR;
                    wr = nwr; wi = nwi;
                }
            }
        }

        if (invert) {
            for (int i = 0; i < n; ++i) {
                re[i] /= n;
                im[i] /= n;
            }
        }

        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        shot = new int[N];
        for (int i = 0; i < N; ++i) shot[i] = Integer.parseInt(br.readLine());

        M = Integer.parseInt(br.readLine());
        distance = new int[M];
        for (int i = 0; i < M; ++i) distance[i] = Integer.parseInt(br.readLine());
        
        int maxS = 0;
        for (int x : shot) if (x > maxS) maxS = x;

        int base = maxS + 1;
        int n = 1;

        while (n < (base << 1)) n <<= 1;

        re = new double[n];
        im = new double[n];

        re[0] = 1.0;
        for (int x : shot) {
            if (x >= 0 && x < n) re[x] = 1.0;
        }

        fft(re, im, n, false);

        for (int i = 0; i < n; ++i) {
            double a = re[i], b = im[i];
            double nr = a*a - b*b;
            double ni = 2.0*a*b;
            re[i] = nr; im[i] = ni;
        }

        fft(re, im, n, true);

        long ans = 0;
        for (int i = 0; i < M; ++i) {
            int d = distance[i];
            if (0 <= d && d < n) {
                long cnt = Math.round(re[d]);
                if (cnt > 0) ++ans;
            }
        }

        System.out.println(ans);

        return;
    }
}

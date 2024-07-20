#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

char readbuf[1 << 20], writebuf[1 << 20];

void stdio_bufset() {
    setvbuf(stdin, readbuf, _IOFBF, 1 << 20);
    setvbuf(stdout, writebuf, _IOFBF, 1 << 20);
}

inline int readd() {
    int temp = 0;
    char c;
    while ((c = _getchar_nolock()) >= '0' && c <= '9') {
        temp = 10 * temp + (c - '0');
    }
    return temp;
}

inline void writeint(int x) {
    char buf[12];
    int i = 10;
    buf[11] = '\n';
    if (x == 0) {
        _putchar_nolock('0');
        _putchar_nolock('\n');
        return;
    }
    while (x) {
        buf[i--] = (x % 10) + '0';
        x /= 10;
    }
    while (++i < 12) {
        _putchar_nolock(buf[i]);
    }
}

int main() {
    stdio_bufset();

    int N = readd();
    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        nums[i] = readd();
    }

    vector<vector<int>> dp(N, vector<int>(N, 0));

    for (int i = 0; i < N; ++i) {
        dp[i][i] = 1;
        if (i + 1 < N && nums[i] == nums[i + 1]) {
            dp[i][i + 1] = 1;
        }
    }

    for (int length = 3; length <= N; ++length) {
        for (int i = 0; i <= N - length; ++i) {
            int j = i + length - 1;
            if (nums[i] == nums[j] && dp[i + 1][j - 1]) {
                dp[i][j] = 1;
            }
        }
    }

    int M = readd();
    for (int i = 0; i < M; ++i) {
        int S = readd();
        int E = readd();
        writeint(dp[S - 1][E - 1]);
    }

    return 0;
}

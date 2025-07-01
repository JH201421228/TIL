import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve():
    while True:
        B, P = map(int, input().split())
        B *= -1

        if not B and not P:
            break

        arr = [0] * (B + 1)
        arr[0] = P
        arr[B] = -P
        info = []
        G = [[0, 0] for _ in range(B)]

        for b in range(B):
            info.append(list(map(int, input().split())))

        total_time = 0

        while arr[B] < 0:
            time = float('inf')
            for b in range(B):
                if arr[b] and not G[b][0]:
                    G[b][0] = min(arr[b], info[b][0])
                    G[b][1] = info[b][1]
                    arr[b] -= G[b][0]

                if G[b][1] > 0:
                    time = min(G[b][1], time)

            total_time += time

            for b in range(B):
                if G[b][1] > 0:
                    G[b][1] -= time
                    if G[b][1] == 0:
                        arr[b + 1] += G[b][0]
                        G[b][0] = 0

        print(total_time)


if __name__ == "__main__":
    solve()

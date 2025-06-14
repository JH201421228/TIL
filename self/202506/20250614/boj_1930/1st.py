import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


index_transformer = {
    0: [1, 2, 3],
    1: [0, 3, 2],
    2: [0, 1, 3],
    3: [0, 2, 1],
}


def solve():
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        first, second = arr[:4], arr[4:]

        flag = 0
        for idx in range(4):
            if second[idx] == first[0]:
                second_ = [second[idx], second[index_transformer[idx][0]], second[index_transformer[idx][1]], second[index_transformer[idx][2]]]

                q = deque(second_[1:])

                for _ in range(3):
                    if first[1:] == list(q):
                        flag = 1
                        print(1)
                        break
                    q.append(q.popleft())

                if flag: break

        else: print(0)

    return


if __name__ == "__main__":
    solve()
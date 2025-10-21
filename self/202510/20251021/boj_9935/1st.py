import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    Q = deque(list(input().rstrip()))
    S = []

    bomb_word = input().rstrip()
    bomb_word_length = len(bomb_word)

    print(bomb_word)

    while Q:
        S.append(Q.popleft())

        if len(S) >= bomb_word_length and ''.join(S[-bomb_word_length:]) == bomb_word:
            for _ in range(bomb_word_length): S.pop()
            
    print(''.join(S) if ''.join(S) else "FRULA")

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def charger(idx, chemicals):
    if idx == 0:
        n = min(chemicals[0], chemicals[1])
        chemicals[0] -= n
        chemicals[1] -= n

    elif idx == 1:
        n = min(chemicals[1], chemicals[2])
        chemicals[1] -= n
        chemicals[2] -= n

    else:
        n = min(chemicals[0], chemicals[2])
        chemicals[0] -= n
        chemicals[2] -= n

    return chemicals, n


def solve():
    for _ in range(int(input())):
        chemicals = list(map(int, input().split()))
        charges = list(map(int, input().split()))
        states = [0] * 3

        max_charge = max(charges)
        for max_idx in range(3):
            if max_charge == charges[max_idx]: break

        chemicals, n = charger(max_idx, chemicals)

        states[max_idx] += n

        for idx in range(3):
            if not chemicals[idx]: break

        if idx == 0:
            chemicals, n = charger(1, chemicals)
            states[1] += n
        elif idx == 1:
            chemicals, n = charger(2, chemicals)
            states[2] += n
        else:
            chemicals, n = charger(0, chemicals)
            states[0] += n

        ans = 0
        for idx in range(3):
            ans += charges[idx] * states[idx]

        if 2*max_charge < sum(charges):
            if max_idx == 0: n = chemicals[2]
            elif max_idx == 1: n = chemicals[0]
            else: n = chemicals[1]

            n //= 2

            ans += min(n, states[max_idx]) * (sum(charges)-2*max_charge)

        print(ans)


if __name__ == "__main__":
    solve()
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


number_to_sign = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM",
}

sign_to_number = {}
for k, v in number_to_sign.items():
    sign_to_number[v] = k


def solve():
    signs = [input().rstrip() for _ in range(2)]
    numbers = []

    for sign in signs:
        length = len(sign)
        cur = 0
        temp = 0

        while cur < length:
            nxt = min(length, cur+4)

            while True:
                s = sign[cur:nxt]
                if s in sign_to_number:
                    temp += sign_to_number[s]
                    break
                nxt -= 1

            cur = nxt

        numbers.append(temp)

    number = sum(numbers)
    print(number)

    sign = ""
    for i in range(len(str(number))):
        if (number%10) * (10**i) in number_to_sign: sign = number_to_sign[(number%10) * (10**i)] + sign
        number //= 10

    print(sign)

    return


if __name__ == "__main__":
    solve()
def number_to_word(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"]
    hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred",
                "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]

    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        return tens[n // 10] + ones[n % 10]
    else:
        h = n // 100
        rest = n % 100
        return hundreds[h] + number_to_word(rest)

def solve():
    N = int(input())
    words = [input().strip() for _ in range(N)]

    base_length = sum(len(word) for word in words if word != "$")

    for num in range(1, 1000):
        word_num = number_to_word(num)
        total_length = base_length + len(word_num)
        if total_length == num:
            result = [word_num if word == "$" else word for word in words]
            print(" ".join(result))
            return

solve()

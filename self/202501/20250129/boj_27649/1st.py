import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def splitter(w, s):
    return f" {s} ".join(w.split(s))


separator = ["<", ">", "&&", "||", "(", ")"]

S = input().rstrip()

for sep in separator:
    S = splitter(S, sep)

print(" ".join(S.split()))
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = input().split()

    first_chars = set()
    second_chars = set()
    first_letters, second_letters = [0] * 26, [0] * 26

    for gene in arr:
        first_chars.add(gene[0])
        second_chars.add(gene[1])

        first_letters[ord(gene[0])-65] += 1
        second_letters[ord(gene[1])-65] += 1

    phenotypes = set()
    for a in first_chars:
        for b in second_chars:
            phenotypes.add(max(a, b))

    first_min_char = min(first_chars)
    second_min_char = min(second_chars)

    cnt = 0
    for gene in arr:
        if gene[0] == first_min_char and gene[1] == second_min_char and first_letters[ord(gene[0])-65] == 1 and second_letters[ord(gene[1])-65] == 1:
            cnt += 1

    if cnt == 1:
        phenotypes.remove(max(first_min_char, second_min_char))

    result = sorted(phenotypes)
    print(len(result))
    print(' '.join(result))

solve()

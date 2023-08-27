import sys
sys.stdin = open('input.txt')


def tower(n, odd_or_even):
    if n == 1 and odd_or_even:
        return [[1, 3]]
    elif n == 1 and not odd_or_even:
        return [[1, 2]]

    tower_list = tower(n - 1, odd_or_even)
    if tower_list[-1][1] == 3:
        tower_list.append([1, 2])
        idx = [0, 3, 1, 2]
    else:
        tower_list.append([1, 3])
        idx = [0, 2, 3, 1]

    length = len(tower_list)
    for i in range(length - 1):
        tower_list.append([idx[tower_list[i][0]], idx[tower_list[i][1]]])

    return tower_list


n = int(input())
print(2**n - 1)

for inner in tower(n, n % 2):
    print(*inner)
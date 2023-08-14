import sys
input = sys.stdin.readline

M, N = map(int, input().split())

pokemon_dict1 = {}
pokemon_dict2 = {}

for i in range(1, M + 1):
    input_value = input().rstrip()
    pokemon_dict1[i] = input_value
    pokemon_dict2[input_value] = i

for i in range(N):
    input_value2 = input().rstrip()

    if input_value2.isdigit():
        ans = pokemon_dict1[int(input_value2)]

    else:
        ans = pokemon_dict2[input_value2]

    print(ans)

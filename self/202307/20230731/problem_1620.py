N, M = map(int, input().split())
pokemon_list = []

for i in range(N):
    pokemon_list.append(str(input()))

for i in range(M):
    input_value = str(input())
    
    if input_value.isdigit():
        print(pokemon_list[int(input_value) - 1])
    
    else:
        print(pokemon_list.index(input_value) + 1)
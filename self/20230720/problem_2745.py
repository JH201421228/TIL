
total = 0

info_num = list(map(int, range(10, 36)))
info_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# info_dict = list(map((lambda x, y: {x: y}),info_alph, info_num))

N, B = map(str, input().split())

for i in range(len(N)):
    if N[i] in info_alph:
        total += info_num[info_alph.index(N[i])] * (int(B) ** (len(N) - i - 1))
    
    else:
        total += int(N[i]) * (int(B) ** (len(N) - i - 1))
        
print(total)
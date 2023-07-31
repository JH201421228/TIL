N = int(input())
have_card = set(map(int, input().split()))

M = int(input())
check_card = list(map(int, input().split()))

output_list = []

for card in check_card:
    if card in have_card:
        output_list.append(1)
    
    else:
        output_list.append(0)

print(*output_list)
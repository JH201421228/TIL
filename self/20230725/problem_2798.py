N, M = map(int, input().split())

card_list = list(map(int, input().split()))
card_length = len(card_list)

sum_val = 0
ans = 0

for i in range(card_length-2):
    for j in range(i+1, card_length-1):
        for k in range(j+1, card_length):
            sum_val = card_list[i] + card_list[j] + card_list[k]
            if sum_val <= M and sum_val > ans:
                ans = sum_val

print(ans)
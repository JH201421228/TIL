import sys
sys.stdin = open('input.txt')

num_of_cake, customer_length = map(int, input().split())
cake_length_list = list(map(int, input().split()))

max_length = max(cake_length_list)

for cut_length in range(max_length - 1, 0, -1):
    total = 0
    for cake_length in cake_length_list:
        if cake_length > cut_length:
            total += cake_length - cut_length

    if total >= customer_length:
        print(cut_length)
        break

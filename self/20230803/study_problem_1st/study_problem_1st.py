import sys
sys.stdin = open('input.txt')

have_num = int(input())
merchant_item = list(map(int, input().split()))

need_num = int(input())
customer_item = list(map(int, input().split()))

for item in customer_item:
    if item in merchant_item:
        print('yes')
    else:
        print('no')
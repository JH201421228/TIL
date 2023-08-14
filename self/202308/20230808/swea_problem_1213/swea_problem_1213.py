import sys
sys.stdin = open('input.txt', encoding='UTF8')

for _ in range(10):
    test_num = int(input())
    search_str = input()
    raw_data = input()
    ans = raw_data.split(search_str)
    print(f'#{test_num} {len(ans) - 1}')
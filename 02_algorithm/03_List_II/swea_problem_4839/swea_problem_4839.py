import sys
sys.stdin = open('input.txt')

def binary_search(end_page, find_page):
    start_page = 1
    cnt = 0
    while start_page <= end_page:
        mid_page = (start_page + end_page) // 2
        if mid_page == find_page:
            return cnt
        elif mid_page > find_page:
            end_page = mid_page
        else:
            start_page = mid_page

        cnt += 1

Test_Case = int(input())

for test_case in range(Test_Case):
    P, A, B = map(int, input().split())

    if binary_search(P, A) == binary_search(P, B):
        print(f'#{test_case+1} 0')
    elif binary_search(P, A) > binary_search(P, B):
        print(f'#{test_case+1} B')
    else:
        print(f'#{test_case+1} A')
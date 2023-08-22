import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    num = int(input())
    num_list = list(map(int, input().split()))
    # print(num_list)
    heap_list = [0] * (num + 1)
    last = 1
    for i in range(num):
        if not heap_list[i]:
            heap_list[last] = num_list[i]
        else:
            last += 1
            heap_list[last] = num_list[i]
            child = last
            parent = child // 2

            while parent and heap_list[parent] > heap_list[child]:
                heap_list[parent], heap_list[child] = heap_list[child], heap_list[parent]
                child = parent
                parent = child // 2
    # print(heap_list)
    ans = 0
    parent = (len(heap_list) - 1) // 2
    while parent:
        ans += heap_list[parent]
        parent //= 2
    print(f'#{test+1} {ans}')
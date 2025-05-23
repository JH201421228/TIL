import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


order = dict()
temp = []
V = [0] * 9
cnt = 0

def order_maker(o):
    global cnt
    if o == 8:
        cnt += 1
        order[''.join(temp)] = cnt
        return

    for n in range(1, 9):
        if not V[n]:
            V[n] = 1
            temp.append(str(n))
            order_maker(o+1)
            temp.pop()
            V[n] = 0

def first_move(arr):
    temp = arr[::-1]
    return temp

def second_move(arr):
    temp = [arr[3], *arr[:3], *arr[5:], arr[4]]
    return temp

def third_move(arr):
    temp = [*arr]
    temp[1], temp[2], temp[5], temp[6] = temp[2], temp[5], temp[6], temp[1]
    return temp

def forth_move(arr):
    temp = [*arr]
    temp[0], temp[4] = temp[4], temp[0]
    return temp

def bfs(dest):
    V = [0] * 40321
    V[1] = 1
    q = deque([['1', '2', '3', '4', '5', '6', '7', '8']])

    while q:
        n = q.popleft()

        if n == dest: break

        temp = first_move(n)
        if not V[order[''.join(temp)]]:
            q.append(temp)
            V[order[''.join(temp)]] = V[order[''.join(n)]] + 1

        temp = second_move(n)
        if not V[order[''.join(temp)]]:
            q.append(temp)
            V[order[''.join(temp)]] = V[order[''.join(n)]] + 1

        temp = third_move(n)
        if not V[order[''.join(temp)]]:
            q.append(temp)
            V[order[''.join(temp)]] = V[order[''.join(n)]] + 1

        temp = forth_move(n)
        if not V[order[''.join(temp)]]:
            q.append(temp)
            V[order[''.join(temp)]] = V[order[''.join(n)]] + 1

    return V[order[''.join(dest)]]-1

order_maker(0)

arr = ['1', '2', '3', '4', '5', '6', '7', '8']
dest = list(map(str, input().rstrip().split()))

print(bfs(dest))
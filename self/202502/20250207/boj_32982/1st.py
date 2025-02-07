import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
times = list(map(int, input().split()))

cur = times[1]
meal = 1

while True:
    if meal % 3 == 0:
        if (cur + K) % 1440 >= times[1]:
            cur = times[1]
        elif (cur + K) % 1440 >= times[0]:
            cur += K
        else:
            print("NO")
            break

    elif meal % 3 == 1:
        if (cur + K) >= times[3]:
            cur = times[3]
        elif (cur + K) >= times[2]:
            cur += K
        else:
            print("NO")
            break

    else:
        if (cur + K) >= times[5]:
            cur = times[5]
        elif (cur + K) >= times[4]:
            cur += K
        else:
            print("NO")
            break

    cur %= 1440
    meal += 1

    if meal // 3 == N-1:
        print("YES")
        break
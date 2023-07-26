N = int(input())
count5 = N // 5
count3 = 0

while True:

    if (N - 5*count5) % 3 == 0:
        ans = count5 + (N - 5*count5) // 3
        break

    else:
        count5 -= 1

    if count5 < 0:
        ans = -1
        break
    
print(ans)


for k in range(int(input())):

    a, b = map(int, input().split())

    c = []

    d = []

    e = []

    c = list(map(int, input().split()))
    
    d = list(map(int, input().split()))

    if a > b:

        for i in range(a - b + 1):

            sum = 0

            for j in range(b):

                sum += c[i + j] * d[j]

            e.append(sum)
    else:

        for i in range(b - a + 1):

            sum = 0

            for j in range(a):

                sum += c[j] * d[i + j]

            e.append(sum)

    print('#', k,' ' ,max(e),sep='')



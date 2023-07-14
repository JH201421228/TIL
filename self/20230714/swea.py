from collections import Counter

m = []

k = int(input())

for _ in range(k):

    n = int(input())
    a = list(map(int, input().split()))
    
    if Counter(a).most_common(2)[0][1] == Counter(a).most_common(2)[1][1]:

        #print('#', n,' ', sep='',end='')
        m.append(Counter(a).most_common()[0][0])

    else:

        #print('#', n,' ', sep='',end='')
        m.append(Counter(a).most_common()[0][0])

for i in range(k):

    print('#', i+1, ' ', m[i], sep='')


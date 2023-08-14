arr = list(range(1, 11))
n = len(arr)

for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & 1<<j:
            subset.append(arr[j])
    if sum(subset) == 10:
        print(subset)
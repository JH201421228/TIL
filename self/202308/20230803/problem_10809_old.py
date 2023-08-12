a = input()
b = 'abcdefghijklmnopqrstuvwxyz'
for i in b :
    if i in a :
        print(a.index(i), end=' ')
    else :
        print(-1, end=' ')


def ro90(m, n):

    mat = [[0] * m for _ in range(m)]

    for i in range(m):

        for j in range(m):

            mat[i][j] = n[m-j-1][i]

    return mat

def ro270(m, n):

    mat = [[0] * m for _ in range(m)]

    for i in range(m):

        for j in range(m):

            mat[i][j] = n[j][m-i-1]

    return mat

def ro180(m, n):

    mat = [[0] * m for _ in range(m)]

    for i in range(m):

        for j in range(m):

            mat[i][j] = n[m-i-1][m-j-1]

    return mat

def emg(a, b, c, d):

    mat = [[0] * 3 for _ in range(d)]

    for i in range(d):

        mat[i][0] = ''.join(map(str, a[i]))
        mat[i][1] = ''.join(map(str, b[i]))
        mat[i][2] = ''.join(map(str, c[i]))

    return mat

mat = []

a = []

n = int(input()) 

for i in range(n):
    
    a += [int(input())]

    b = [list(map(int, input().split())) for _ in range(a[i])]
    
    mat += emg(ro90(a[i], b), ro180(a[i], b), ro270(a[i], b), a[i])

# print(mat)
# print(a)

k = 0

l = a[0]

for i in range(n):

    print(f'#{i+1}')
    
    for j in range(k, k+a[i]):
        
        print(f'{mat[j][0]} {mat[j][1]} {mat[j][2]}')

    k += a[i]    
# for i in range(a):

#     for j in range(3):

#         print(emg(ro90(a, b), ro180(a, b), ro270(a, b), a)[i][j], end=' ')
        
#     print('')
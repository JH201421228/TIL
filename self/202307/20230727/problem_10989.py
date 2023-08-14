import sys
N = int(sys.stdin.readline())
ans_list = [0] * 10001

for _ in range(N):
    where = int(sys.stdin.readline())
    ans_list[where] += 1
    
for i in range(len(ans_list)):
    
    for j in range(ans_list[i]):
        print(i)
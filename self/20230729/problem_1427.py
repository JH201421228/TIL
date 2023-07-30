N = str(input())
ans_list = []
ans = 0

for i in N:
    ans_list.append(int(i))
    
ans_list.sort()

for i in range(len(ans_list)):
    ans += (ans_list[i]) * (10)**i
    
print(ans)
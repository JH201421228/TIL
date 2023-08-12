A, B, V = map(int, input().split())

if (V - A) % (A - B) == 0:
    ans = (V - A) // (A - B) + 1
else:
    ans = (V - A) // (A - B) + 2
    
print(ans)
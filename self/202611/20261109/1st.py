crypt = "label"

ans = ""

for c in crypt:
    # print(c)
    # print(ord(c))
    # print(ord(c) ^ 13)
    # print(chr(ord(c) ^ 13))
    ans += chr(ord(c) ^ 13)
    
print(f"crypto{{{ans}}}")
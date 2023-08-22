import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    char_list = [[False] * 15 for _ in range(5)]
    for i in range(5):
        inner_list = list(map(str, input()))
        char_list[i][:len(inner_list)] = inner_list
    ans = []
    for i in range(15):
        for j in range(5):
            if char_list[j][i]:
                ans.append(char_list[j][i])
    ans_str = ''.join(ans)
    print(f'#{test+1} {ans_str}')
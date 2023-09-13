import sys
sys.stdin = open('input.txt')


def teach_u(start, cnt):
    if cnt == K - 5: # 배울 수 있는 문자 개수에서 필수 알파벳 수를 뺀 값
        num = 0
        for inner_str in str_list: # 해당 단어를 읽을 수 있는지 없는지 체크
            for small_str in inner_str:
                if not alpha_list[ord(small_str)-ord('a')]: 
                   break
            else:
                num += 1
        global ans # 결과값 변경
        if ans < num:
            ans = num

        return

    for idx in range(start, 26): # 26개의 알파벳을 각각 익혀가며
        if not alpha_list[idx]:
            alpha_list[idx] = 1
            teach_u(idx + 1, cnt + 1) # 재귀
            alpha_list[idx] = 0

N, K = map(int, input().split())
str_list = [list(input()[4:-4]) for _ in range(N)] # 앞뒤 네개 빼고 받아옴
# print(str_list)
alpha_list = [0] * 26 # 배운 알파벳 번호를 저장할 리스트
init_alpha = list('antic') # 필수 알파벳
for char in init_alpha:
    alpha_list[ord(char) - ord('a')] = 1 # 필수 알파벳 저장
# print(alpha_list)

ans = 0
if K >= 5: 
    teach_u(0, 0)
    print(ans)
elif K == 26: # 26개의 알파벳을 모두 배울 수 있는 경우
    print(N)
else:
    print(0) # 필수 알파벳을 못 배우면 아무것도 못 읽음
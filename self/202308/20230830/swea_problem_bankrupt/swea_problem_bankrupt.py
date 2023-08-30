import sys
sys.stdin = open('input.txt')


def why_python_do_not_have_this_func(num, length): # 10진수를 3진수로 변환하는 함수
    no_name_list = []

    while num:
        no_name_list.insert(0, str(num % 3))
        num //= 3

    if len(no_name_list) > length:
        return False

    return (''.join(no_name_list)).zfill(length)


T = int(input())
for test in range(T): # 이진수 삼진수 둘 모두 반드시 한자리는 잘못됨
    # 1. 이진수에서 한자리만 바뀐 값들을 모두 저장
    # 2. 바뀐 값들을 모두 3진수로 변환
    # 3. 받은 3진수와 한자리만 다른 값을 출력

    bi = list(map(str, input()))
    tri = list(map(str, input()))
    # print(bi, int(tri))
    bi_list = []
    for idx in range(len(bi)):
        temp = bi[:]
        temp[idx] = str(1 - int(temp[idx]))
        bi_list.append(int(''.join(temp), 2)) # 한자리만 바뀐 2진수를 10진수로 변경해서 모두 넣음
    # print(bi_list)
    for num in bi_list:
        # print(why_python_do_not_have_this_func(num, len(tri)), type(why_python_do_not_have_this_func(num, len(tri))))
        ten_to_tri = why_python_do_not_have_this_func(num, len(tri))
        checker = 0
        if ten_to_tri:
            for idx in range(len(tri)):
                if ten_to_tri[idx] != tri[idx]:
                    checker += 1
                if checker > 1:
                    break
            if checker == 1:
                print(f'#{test+1} {int(ten_to_tri, 3)}')
                break
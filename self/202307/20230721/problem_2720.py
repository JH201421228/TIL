T = int(input()) # 테스트 케이스의 개수

for i in range(T):
    cent = int(input()) # 거슬러 줄 돈
    print(f'{cent // 25} {(cent % 25) // 10} {((cent % 25) % 10) // 5} {((cent % 25) % 10) % 5}')
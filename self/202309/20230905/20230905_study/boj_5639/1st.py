import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)

def tree_maker(start, end):
    if start > end:
        return

    mid = end + 1 # mid를 정의함과 동시에 break에 걸리지 않으면 리턴할 수 있는 조건
    for i in range(start, end + 1):
        if preorder_list[start] < preorder_list[i]: # 하위 노드의 좌우 자식을 가르는 조건
            mid = i # 부모 노드의 인덱스
            break

    tree_maker(start + 1, mid - 1) # 왼쪽 하위 트리
    tree_maker(mid, end) # 오른쪽 하위 트리
    print(preorder_list[start])


preorder_list = [] # 입력값을 받을 리스트 생성
while True: # 입력 제한을 주기 위해 해당 방법을 사용
    try:
        preorder_list.append(int(input()))
    except EOFError:
        break
# print(preorder_list)
tree_maker(0, len(preorder_list) - 1)
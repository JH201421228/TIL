import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)

def tree_maker(start, end):
    if start > end:
        return

    mid = end + 1 # mid를 정의함과 동시에 break에 걸리지 않으면 리턴할 수 있는 조건
    for i in range(start, end + 1): # end 값 까지 조사하기 위해 end + 1
        if preorder_list[start] < preorder_list[i]:
            mid = i
            break

    tree_maker(start + 1, mid - 1)
    tree_maker(mid, end)
    print(preorder_list[start])


preorder_list = []
while True:
    try:
        preorder_list.append(int(input()))
    except EOFError:
        break
# print(preorder_list)
tree_maker(0, len(preorder_list) - 1)

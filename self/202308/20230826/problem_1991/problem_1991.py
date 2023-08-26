import sys
sys.stdin = open('input.txt')


def preorder(start):
    if start == 0:
        return
    print(appendix[start], end='')
    preorder(left_list[start])
    preorder(right_list[start])


def inorder(start):
    if start == 0:
        return
    inorder(left_list[start])
    print(appendix[start], end='')
    inorder(right_list[start])


def postorder(start):
    if start == 0:
        return
    postorder(left_list[start])
    postorder(right_list[start])
    print(appendix[start], end='')


appendix = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
appendix_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
n = int(input())
left_list = [0] * (n+1)
right_list = [0] * (n+1)
for _ in range(n):
    parents, left, right = map(str, input().split())
    if left != '.':
        left_list[appendix_dict[parents]] = appendix_dict[left]
    if right != '.':
        right_list[appendix_dict[parents]] = appendix_dict[right]
# print(left_list)
# print(right_list)
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
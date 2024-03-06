import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
chars = [[] for _ in range(10)]
chars_weight = {}
chars_length = []
chars_to_num = {}
chars_set = set()
for _ in range(N):
    temp = list(map(str, input().rstrip()))
    temp.reverse()
    for idx in range(len(temp)):
        multi = 10**idx
        chars[idx].append(temp[idx])
        if temp[idx] in chars_weight:
            chars_weight[temp[idx]] += multi
        else:
            chars_weight[temp[idx]] = multi
sorted_dict = sorted(chars_weight.items(), key = lambda x: -x[1])

num = 9
for tu in sorted_dict:
    chars_to_num[tu[0]] = num
    num -= 1

# print(chars_to_num)

total = 0
for idx in range(10):
    multi = 10**idx
    if chars[idx]:
        for char in chars[idx]:
            total += chars_to_num[char] * multi

print(total)

# 가장 길이가 긴 숫자 배열을 찾는다
# 두번째로 긴 숫자 배열과 길이차이만큼의 인덱스는 숫자를 줄 수 있다.
# 길이가 같은 배열이 있는 경우
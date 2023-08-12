import sys
input = sys.stdin.readline

aggre = set()
check_dict = {}

N, M = map(int, input().split())

for i in range(N):
    aggre.add(input().rstrip())

for i in range(M):
    input_str = input().rstrip()
    check_dict[input_str] = check_dict.get(input_str, 0) + 1

total = 0

for key in check_dict.keys():
    if key in aggre:
        total += check_dict[key]

print(total)
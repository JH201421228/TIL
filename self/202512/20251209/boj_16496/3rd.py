import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())

arr = list(map(str, input().split()))

arr.sort(key=lambda x: x * 9, reverse=True)

print(arr[1] * 9)


result = "".join(arr)

print(str(int(result)))

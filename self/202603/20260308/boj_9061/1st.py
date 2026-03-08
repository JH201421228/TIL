import sys
from collections import defaultdict
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    x_dict = defaultdict(list)
    y_dict = defaultdict(list)
    
    for _ in range(N):
        x, y = map(int, input().split())
        x_dict[x].append(y)
        y_dict[y].append(x)
        
    x_list = []
    y_list = []
    
    for k, v in x_dict.items():
        x_list.append((k, max(v), min(v)))
        
    for k, v in y_dict.items():
        y_list.append((k, max(v), min(v)))

    x_list.sort()
    y_list.sort()
    
    x_min_list, x_max_list = [x_list[0][2]], [x_list[0][1]]
    x_min_reverse, x_max_reverse = [x_list[-1][2]], [x_list[-1][1]]

    y_min_list, y_max_list = [y_list[0][2]], [y_list[0][1]]
    y_min_reverse, y_max_reverse = [y_list[-1][2]], [y_list[-1][1]]
    
    for idx in range(1, len(x_list)):
        x_min_list.append(min(x_min_list[-1], x_list[idx][2]))
        x_max_list.append(max(x_max_list[-1], x_list[idx][1]))
        
        x_min_reverse.append(min(x_min_reverse[-1], x_list[-1-idx][2]))
        x_max_reverse.append(max(x_max_reverse[-1], x_list[-1-idx][1]))
        
    
    for idx in range(1, len(y_list)):
        y_min_list.append(min(y_min_list[-1], y_list[idx][2]))
        y_max_list.append(max(y_max_list[-1], y_list[idx][1]))
        
        y_min_reverse.append(min(y_min_reverse[-1], y_list[-1-idx][2]))
        y_max_reverse.append(max(y_max_reverse[-1], y_list[-1-idx][1]))
    
    ans = float("inf")
    
    x_len = len(x_list)
    y_len = len(y_list)
    
    for i in range(x_len-1):
        ans = min(ans, max((x_list[i][0] - x_list[0][0]) * (x_max_list[i] - x_min_list[i]), (x_list[-1][0] - x_list[i+1][0]) * (x_max_reverse[x_len-i-2] - x_min_reverse[x_len-i-2])))
    
    for i in range(y_len-1):
        ans = min(ans, max((y_list[i][0] - y_list[0][0]) * (y_max_list[i] - y_min_list[i]), (y_list[-1][0] - y_list[i+1][0]) * (y_max_reverse[y_len-i-2] - y_min_reverse[y_len-i-2])))
    
    if N == 1: print(0)
    else: print(ans)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()
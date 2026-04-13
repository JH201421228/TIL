import sys
import heapq
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    string = input().rstrip()
    
    hq = []
    string_dict = {}
    
    for idx in range(N):
        if string[idx] not in string_dict:
            string_dict[string[idx]] = deque([idx])
        else:
            string_dict[string[idx]].append(idx)
    
    for k, v in string_dict.items():
        if len(v) > N//2:
            print(-1)
            return
        
        heapq.heappush(hq, (-len(v), k))
    
    cnt = 0
    ans = ""
    
    if N%2:
        temp = []
        for _ in range(3):
            temp.append(heapq.heappop(hq))
        ans += f"{min(string_dict[temp[0][1]][0] + 1, string_dict[temp[1][1]][0] + 1)} {max(string_dict[temp[0][1]][0] + 1, string_dict[temp[1][1]][0] + 1)} \n"
        ans += f"{min(string_dict[temp[1][1]][0] + 1, string_dict[temp[2][1]][0] + 1)} {max(string_dict[temp[1][1]][0] + 1, string_dict[temp[2][1]][0] + 1)} \n"
        cnt = 2
        string_dict[temp[0][1]].popleft()
        string_dict[temp[1][1]].popleft()
        string_dict[temp[2][1]].popleft()
        
        for t in temp:
            if -t[0] > 1:
                heapq.heappush(hq, (t[0]+1, t[1]))
    
    while hq:
        temp = []
        for _ in range(2):
            temp.append(heapq.heappop(hq))
            
        ans += f"{min(string_dict[temp[0][1]][0] + 1, string_dict[temp[1][1]][0] + 1)} {max(string_dict[temp[0][1]][0] + 1, string_dict[temp[1][1]][0] + 1)} \n"
        string_dict[temp[0][1]].popleft()
        string_dict[temp[1][1]].popleft()
        
        cnt += 1
        
        for t in temp:
            if -t[0] > 1:
                heapq.heappush(hq, (t[0]+1, t[1]))

        
    print(cnt)
    print(ans)
    
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
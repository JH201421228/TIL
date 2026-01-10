import sys, copy
sys.stdin = open("input.txt")
input = sys.stdin.readline


def checker(length, candid, origin):
    if len(candid) < length: return False
    
    temp = copy.deepcopy(origin)
    
    for k in candid[:length]:
        temp[k] -= 1
        
    one_cnt, minus_cnt, else_cnt = 0, 0, 0
    for k, v in temp.items():
        if v == 1: one_cnt += 1
        elif v == -1: minus_cnt += 1
        elif v != 0: else_cnt += 1
        
    if length == len(candid):
        if one_cnt == 1 and minus_cnt == 1: return True
        else: return False
    else:
        if one_cnt == 1 and minus_cnt == 1 and not else_cnt: return True
        if not one_cnt and not minus_cnt and not else_cnt: return True
        
    for idx in range(len(candid) - length):
        cur, nxt = candid[idx], candid[length+idx]
        
        if temp[cur] == 1:
            one_cnt -= 1
            else_cnt += 1
        elif temp[cur] == 0:
            one_cnt += 1
        elif temp[cur] == -1:
            minus_cnt -= 1
        elif temp[cur] == -2:
            else_cnt -= 1
            minus_cnt += 1
            
        temp[cur] += 1
    
        if temp[nxt] == 2:
            else_cnt -= 1
            one_cnt += 1
        elif temp[nxt] == 1:
            one_cnt -= 1
        elif temp[nxt] == 0:
            minus_cnt += 1
        elif temp[nxt] == -1:
            minus_cnt -= 1
            else_cnt += 1
            
        temp[nxt] -= 1
        
        if one_cnt == 1 and minus_cnt == 1 and not else_cnt: return True
        if not one_cnt and not minus_cnt and not else_cnt: return True
        
    return False


def solve():
    S = input().rstrip()
    l = len(S)
    
    origin = {chr(i): 0 for i in range(97, 123)}
    
    for s in S: origin[s] += 1
    
    for _ in range(int(input())):
        if checker(l, input().rstrip(), origin): print("YES")
        else: print("NO")
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
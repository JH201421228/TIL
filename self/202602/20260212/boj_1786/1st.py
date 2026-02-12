import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    T = list(input().rstrip("\n"))
    P = list(input().rstrip("\n"))
    
    p_len = len(P)
    
    preprocess = [0] * p_len
    stack_n = 0
    
    for idx in range(1, len(P)):
        while stack_n > 0 and P[stack_n] != P[idx]:
            stack_n = preprocess[stack_n-1]
        
        if P[stack_n] == P[idx]:
            stack_n += 1
            preprocess[idx] = stack_n
    
    cnt = 0
    ans_list = []
    
    p_idx = 0
    
    for idx in range(len(T)):
        while p_idx > 0 and T[idx] != P[p_idx]:
            p_idx = preprocess[p_idx-1]
            
        if T[idx] == P[p_idx]:
            if p_idx == p_len-1:
                cnt += 1
                ans_list.append(idx-p_len+2)
                p_idx = preprocess[p_idx]
            else:
                p_idx += 1
                
    print(cnt)
    print(*ans_list)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
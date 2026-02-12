import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, A, B, C, D = map(int, input().split())
    X, Y = [], []
    
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    xmin = min(X)
    xmax = max(X)
    ymin = min(Y)
    ymax = max(Y)
        
    x_list = [0] * (xmax-xmin+1)
    y_list = [0] * (ymax-ymin+1)
    
    x_cost = [0] * (xmax-xmin+1)
    y_cost = [0] * (ymax-ymin+1)
    
    for x in X:
        x_list[x-xmin] += 1
        x_cost[0] += A*(x-xmin)
    for y in Y:
        y_list[y-ymin] += 1
        y_cost[0] += C*(y-ymin)
    
    n, m, x_cur = N-x_list[0], x_list[0], x_cost[0]
    for idx in range(1, xmax-xmin+1):
        x_cur -= A*n
        x_cur += B*m
        x_cost[idx] = x_cur
        m += x_list[idx]
        n -= x_list[idx]
        
    n, m, y_cur = N-y_list[0], y_list[0], y_cost[0]
    for idx in range(1, ymax-ymin+1):
        y_cur -= C*n
        y_cur += D*m
        y_cost[idx] = y_cur
        m += y_list[idx]
        n -= y_list[idx]
        
    print(min(x_cost) + min(y_cost))
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
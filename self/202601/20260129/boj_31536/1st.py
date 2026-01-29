import sys, heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    Mx, My, a = map(int, input().split())
    Kx, Ky, b = map(int, input().split())
    M, K = map(int, input().split())
    Mat = [tuple(map(int, input().split())) for _ in range(M)]
    Kor = [tuple(map(int, input().split())) for _ in range(K)]
    
    Mx_c, My_c = Mx + 0.5*a, My + 0.5*a
    Kx_c, Ky_c = Kx + 0.5*b, Ky + 0.5*b
    
    Mat_q, Kor_q = [], []
    
    for x, y in Mat:
        heapq.heappush(Mat_q, ((Kx_c-x)**2+(Ky_c-y)**2, x, y))
        
    for x, y in Kor:
        heapq.heappush(Kor_q, ((Mx_c-x)**2+(My_c-y)**2, x, y))
        
    Mat_cor, Kor_cor = [], []
    
    for _ in range(min(a+1, M)):
        _, x, y = heapq.heappop(Mat_q)
        Mat_cor.append((x, y))
        
    for _ in range(min(b+1, K)):
        _, x, y = heapq.heappop(Kor_q)
        Kor_cor.append((x, y))
        
    dist = float("inf")
    Matx, Maty, Korx, Kory = 0, 0, 0, 0
        
    for i in range(min(a+1, M)):
        ix, iy = Mat_cor[i]
        for j in range(min(b+1, K)):
            jx, jy = Kor_cor[j]
            
            if (ix-jx)**2+(iy-jy)**2 < dist:
                dist = (ix-jx)**2+(iy-jy)**2
                Matx, Maty, Korx, Kory = ix, iy, jx, jy
                
    print(dist)
    print(Matx, Maty)
    print(Korx, Kory)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
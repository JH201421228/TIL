import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    genre = tuple(input().rstrip().split())
    
    genre_dict = {genre[i]: i for i in range(N)}
    books = []
    
    for _ in range(int(input())):
        info = tuple(input().rstrip().split())
        res = 0
        for g in info[2:]: res += (1<<genre_dict[g])
        books.append(res)

    for _ in range(int(input())):
        req = tuple(input().rstrip().split())
        que = 0
        for r in req[1:]: que += (1<<genre_dict[r])
        
        ans = 0
        
        for b in books:
            if b&que == que: ans += 1
            
        print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
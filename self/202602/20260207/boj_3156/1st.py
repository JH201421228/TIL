import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    statement = [tuple(input().rstrip().split()) for _ in range(N)]
    
    statement.sort(key=lambda x: int(x[2]))
    
    song_set = set()
    song_list = [""] * 500
    set_len = 0
    ans = []
    
    for s in statement:
        for name in s[3:]:
            if name not in song_set:
                for i in range(int(s[2])-1, -1, -1):
                    if not song_list[i]:
                        song_list[i] = name
                        song_set.add(name)
                        set_len += 1
                        break
                if i == int(s[2])-1 and set_len == int(s[2]): ans.append(s[2] + " " + name)
                
    for a in ans: print(a)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
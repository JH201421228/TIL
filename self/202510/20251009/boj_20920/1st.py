import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    tar_dict = {}
    tar_set = set()
    
    for _ in range(N):
        tmp = input().rstrip()
        if len(tmp) >= M:
            tar_set.add(tmp)
            tar_dict[tmp] = tar_dict.get(tmp, 0) + 1
            
    tar_list = list(tar_set)
    tar_list.sort(key=lambda x: ( -tar_dict[x], -len(x), x))
    
    for tar in tar_list:
        print(tar)
    
    return


def main():
    solve()
    return



if __name__ == "__main__":
    main()
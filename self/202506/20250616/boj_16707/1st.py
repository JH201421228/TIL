import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 1 시작, 2 자유의, N 숙소

class Edge:
    def __init__(self, x, c, d, inv):
        self.x = x
        self.c = c
        self.d = d
        self.inv = inv

def set_edge(u, v, c, d, G):
    G[u].append(Edge(v, c, d, len(G[v])))
    G[v].append(Edge(u, 0, -d, len(G[u])-1))

    return

def solve():
    N, M = map(int, input().split())

    return


if __name__ == "__main__":
    solve()
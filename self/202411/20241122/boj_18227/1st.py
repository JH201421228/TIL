# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline
#
#
# def dfs(n, dep):
#     global cnt
#     A[n] = cnt = cnt+1
#     D[cnt] = dep
#     for x in G[n]:
#         dfs(x, dep+1)
#         if n == C:
#             dep = 1
#     E[n] = cnt
#
# def lazy_U(s, e, idx):
#     if lazy[idx]:
#         if s == e:
#             tree[idx] += D[s]
#         else:
#             lazy[idx*2] = 1
#             lazy[idx*2+1] = 1
#         lazy[idx] = 0
#
# def U(s, e, idx, l, r):
#     lazy_U(s, e, idx)
#
#     if s > r or e < l:
#         return
#
#     if s >= l and e <= r:
#         lazy[idx] = 1
#         lazy_U(s, e, idx)
#         return
#
#     mid = (s+e) >> 1
#
#     U(s, mid, idx*2, l, r)
#     U(mid+1, e, idx*2+1, l, r)
#
# def S(s, e, idx, i):
#     lazy_U(s, e, idx)
#
#     if s > i or e < i:
#         return 0
#
#     if s == e:
#         return tree[idx]
#
#     mid = (s+e) >> 1
#
#     return S(s, mid, idx*2, i) + S(mid+1, e, idx*2+1, i)
#
#
# N, C = map(int, input().split())
# G = [[] for _ in range(N+1)]
# A = [0] * (N+1)
# E = [0] * (N+1)
# D = [0] * (N+1)
# tree = [0] * (4*N+1)
# lazy = [0] * (4*N+1)
# cnt = 0
#
# for _ in range(N-1):
#     temp = tuple(map(int, input().split()))
#     G[temp[0]].append(temp[1])
#
# dfs(C, 1)
#
# for _ in range(int(input())):
#     temp = list(map(int, input().split()))
#
#     if temp[0] == 1:
#         U(1, N, 1, A[])
#     else:
#         pass
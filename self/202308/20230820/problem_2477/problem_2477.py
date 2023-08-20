import sys
sys.stdin = open('input.txt')

unit_per_acer = int(input())
farm_info = [list(map(int, input().split())) for _ in range(6)]

where = []
lengths = []
for vector, length in farm_info:
    where.append(vector)
    lengths.append(length)
if where.count(1) == 1:
    horizon = lengths[where.index(1)]
    idx1 = where.index(1)
else:
    horizon = lengths[where.index(2)]
    idx1 = where.index(2)

if where.count(3) == 1:
    vertical = lengths[where.index(3)]
    idx2 = where.index(3)
else:
    vertical = lengths[where.index(4)]
    idx2 = where.index(4)

if (idx1 == 0 and idx2 == 5) or (idx1 == 5 and idx2 == 0):
    idx0 = 1
    idx3 = 4
elif idx1 < idx2:
    idx0 = idx1 - 1
    idx3 = idx2 + 1
else:
    idx0 = idx2 - 1
    idx3 = idx1 + 1

if idx0 == -1:
    idx0 = 5
if idx3 == 6:
    idx3 = 0

idx_list = [i for i in range(6)]
idx_list.remove(idx0)
idx_list.remove(idx1)
idx_list.remove(idx2)
idx_list.remove(idx3)
# print(horizon, vertical)
# print(idx0, idx1, idx2, idx3)
# print(idx_list)
ans = (horizon * vertical - farm_info[idx_list[0]][1] * farm_info[idx_list[1]][1]) * unit_per_acer
print(ans)
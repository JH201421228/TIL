import sys
sys.stdin = open('input.txt')

horizon, vertical = map(int, input().split())
num_of_store = int(input())
store_list = [list(map(int, input().split())) for _ in range(num_of_store + 1)]
# where = list(map(int, input().split()))
# 1 북쪽, 2 남쪽, 3 서쪽, 4 동쪽

total_length = 2 * (horizon + vertical)
where_is_store = []
for news, cordinate in store_list:
    if news == 1:
        where_is_store.append(cordinate)
    elif news == 4:
        where_is_store.append(cordinate + horizon)
    elif news == 2:
        where_is_store.append(horizon * 2 + vertical - cordinate)
    else:
        where_is_store.append(total_length - cordinate)
ans_list = []
person_cordinate = where_is_store.pop()
for cordinate in where_is_store:
    if person_cordinate - cordinate > 0:
        ans_list.append(min(person_cordinate - cordinate, total_length - (person_cordinate - cordinate)))
    else:
        ans_list.append(min(-(person_cordinate - cordinate), total_length + (person_cordinate - cordinate)))
print(sum(ans_list))


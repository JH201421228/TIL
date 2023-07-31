for i in range(10):
    num_of_buildings = int(input())
    building_status = list(map(int, input().split()))
    total = 0

    for j in range(2, num_of_buildings - 2):
        if (building_status[j]) != 0 and (building_status[j] > building_status[j - 2]) and (building_status[j] > building_status[j - 1]) and (building_status[j] > building_status[j + 1]) and (building_status[j] > building_status[j + 2]):
            total += building_status[j] - max(building_status[j - 2], building_status[j - 1], building_status[j + 1], building_status[j + 2])

    print(f'#{i + 1} {total}')
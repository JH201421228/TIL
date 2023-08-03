import sys

num_of_person_and_window = int(sys.stdin.readline())

window_list = [0] * num_of_person_and_window

for i in range(1, num_of_person_and_window + 1):
    for j in range(i, num_of_person_and_window, i):
        if window_list[j-1]:
            window_list[j-1] = 0
        else:
            window_list[j-1] = 1

print(sum(window_list))
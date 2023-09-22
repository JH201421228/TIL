import sys
import heapq

# Avoid shadowing the built-in input function
sys.stdin = open('input.txt')
readline = sys.stdin.readline

# Read input values
N, D = map(int, readline().split())

# Initialize the graph with a list of lists
graph = [[] for _ in range(10_001)]

# Read road information
road_info = [list(map(int, readline().split())) for _ in range(N)]

# Initialize the gogo list with infinity values
gogo = [float('inf')] * (10_001)
gogo[0] = 0  # Starting point

# Process road_info
while road_info:
    start, end, weight = heapq.heappop(road_info)

    # Check if the road is within bounds
    if start > D or end > D:
        continue

    # Update gogo if a shorter path is found
    if gogo[start] + weight < gogo[end]:
        gogo[end] = gogo[start] + weight

        # Update gogo for subsequent points
        for idx in range(end + 1, 10_001):
            gogo[idx] = gogo[idx - 1] + 1

# Print the shortest travel time to D
print(gogo[D])
def tsp_nearest_neighbor(distance):
    n = len(distance)
    visited = [False] * n

    current = 0
    visited[current] = True
    tour = [current]
    total_distance = 0

    for _ in range(n - 1):
        nearest = -1
        min_dist = float('inf')

        for city in range(n):
            if not visited[city] and distance[current][city] < min_dist:
                min_dist = distance[current][city]
                nearest = city

        tour.append(nearest)
        visited[nearest] = True
        total_distance += min_dist
        current = nearest

    total_distance += distance[current][0]
    tour.append(0)

    return tour, total_distance

# Distance Matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour, cost = tsp_nearest_neighbor(distance)

print("Tour:", tour)
print("Total Distance:", cost)

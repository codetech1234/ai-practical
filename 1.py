def tsp(graph, start):

    n = len(graph)
    visited = [False]*n
    path = []
    cost = 0

    current = start
    visited[current] = True
    path.append(current)

    for i in range(n-1):

        min_dist = 999
        next_city = -1

        for j in range(n):
            if not visited[j] and graph[current][j] < min_dist:
                min_dist = graph[current][j]
                next_city = j

        visited[next_city] = True
        path.append(next_city)
        cost += min_dist
        current = next_city

    cost += graph[current][start]
    path.append(start)

    print("Path:", path)
    print("Minimum Cost:", cost)


graph = [
[0,10,15,20],
[10,0,35,25],
[15,35,0,30],
[20,25,30,0]
]

tsp(graph,0)
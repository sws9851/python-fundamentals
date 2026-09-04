INF = float("inf")

adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def shortest_path(matrix: list, start_node: int) -> tuple:
    size = len(matrix)
    distances = [INF] * size
    distances[start_node] = 0
    paths = [[node] for node in range(size)]
    visited = [False] * size

    for _ in range(size):
        min_distance = INF
        current = -1
        for node in range(size):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                current = node

        # nothing reachable left, so the rest of the graph is disconnected
        if current == -1:
            break

        visited[current] = True

        for node in range(size):
            weight = matrix[current][node]
            if weight != INF and not visited[node]:
                new_distance = distances[current] + weight
                if new_distance < distances[node]:
                    distances[node] = new_distance
                    paths[node] = paths[current] + [node]

    return distances, paths


def print_route(distances: list, paths: list, start_node: int, target_node: int) -> None:
    if target_node == start_node or distances[target_node] == INF:
        return
    route = " -> ".join(str(node) for node in paths[target_node])
    print(f"\n{start_node}-{target_node} distance: {distances[target_node]}\nPath: {route}")


if __name__ == "__main__":
    distances, paths = shortest_path(adj_matrix, 0)
    for target in range(len(adj_matrix)):
        print_route(distances, paths, 0, target)

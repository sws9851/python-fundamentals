def dfs(adj_matrix: list, node_label: int) -> list:
    size = len(adj_matrix)
    stack = [node for node in range(size) if adj_matrix[node_label][node] == 1]
    visited = [node_label]
    seen = {node_label}
    on_stack = set(stack)

    while stack:
        visiting = stack.pop()
        on_stack.discard(visiting)
        visited.append(visiting)
        seen.add(visiting)

        for node in range(size):
            # dedupe on insertion rather than on removal, so a node already queued
            # keeps its original position instead of floating back to the top
            if adj_matrix[visiting][node] == 1 and node not in seen and node not in on_stack:
                stack.append(node)
                on_stack.add(node)

    return visited


if __name__ == "__main__":
    print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))

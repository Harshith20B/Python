visited = []
def dfs(graph, n, u):
    visited[u] = 1
    print(u)
    for v in range(n):
        if graph[u][v] and not visited[v]:
            dfs(graph, n, v)

def main():
    graph = [
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    n = len(graph[0])
    source = 0
    global visited
    visited = [0] * n
    print("Adjacency Matrix")
    for row in graph:
        print(row)
    print("DFS Order")
    dfs(graph, n, source)

main()

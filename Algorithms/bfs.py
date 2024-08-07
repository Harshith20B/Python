visited = []
queue = []
def bfs(graph,n,u):
    for i in range(n):
        visited.append(0)
    queue.append(u)
    visited[u]=1
    while queue:
        u=queue.pop(0)
        print(u)
        for v in range(n):
            if (not visited[v] and graph[u][v]):
                visited[v]=1
                queue.append(v)

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
    print("Adjacency Matrix")
    for row in graph:
        print(row)
    print("BFS Order")
    bfs(graph, n, source)

main()


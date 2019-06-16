def bfs(u, M, visited, distances, n):
    queue = []
    distances[u] = 0
    visited[u] = 1
    queue.append(u)

    while len(queue) > 0:
        u = queue.pop(0)
        for v in range(n):
            if M[u][v] == 1 and visited[v] == 0:
                distances[v] = distances[u] + 1
                visited[v] = 1
                queue.append(v)

    return distances


if __name__ == '__main__':
    n = int(input())
    M = [[0] * n for _ in range(n)]
    distances = [-1] * n
    visited = [0] * n
    for _ in range(n):
        u, k, *vs = input().split()
        u, k, vs = int(u) - 1, int(k), list(map(int, vs))
        vs = [v - 1 for v in vs]
        for v in vs:
            M[u][v] = 1

    distances = bfs(0, M, visited, distances, n)

    for i in range(n):
        print('{} {}'.format(i + 1, distances[i]))

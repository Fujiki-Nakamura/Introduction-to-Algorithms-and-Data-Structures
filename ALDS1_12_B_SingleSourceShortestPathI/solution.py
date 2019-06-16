import math


def dijkstra(start, distances, vertices, n):
    costs = [math.inf] * n
    for v in vertices:
        costs[v] = distances[start][v]
    remains = vertices - set([start])
    while len(remains) > 0:
        w, c_min = -1, math.inf
        for v in remains:
            c = costs[v]
            if c < c_min:
                w = v
                c_min = c
        remains = remains - set([w])
        for v in remains:
            costs[v] = min(
                costs[v],
                costs[w] + distances[w][v])
    return costs


if __name__ == '__main__':
    n = int(input())
    distances = [[math.inf] * n for _ in range(n)]
    for _ in range(n):
        u, k, *vcs = input().split()
        u, k, vcs = int(u), int(k), list(map(int, vcs))
        distances[u][u] = 0
        for i in range(k):
            v = vcs[i*2]
            c = vcs[i*2 + 1]
            distances[u][v] = c

    vertices = set([i for i in range(n)])
    costs = dijkstra(0, distances, vertices, n)
    for i in range(n):
        print('{} {}'.format(i, costs[i]))

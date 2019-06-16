if __name__ == '__main__':
    n = int(input())
    M = [[0] * n for _ in range(n)]
    for _ in range(n):
        v, n_adj, *adjs = input().split()
        v = int(v)
        n_adj = int(n_adj)
        adjs = [int(e) for e in adjs]
        for i in range(n_adj):
            M[v - 1][adjs[i] - 1] = 1

    for row in M:
        print(' '.join([str(e) for e in row]))

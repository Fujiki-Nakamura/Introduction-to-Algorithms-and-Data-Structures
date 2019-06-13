def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    table = [[0] * n for _ in range(m)]
    for xi in range(1, m):
        for yi in range(1, n):
            if X[xi] == Y[yi]:
                table[xi][yi] = table[xi-1][yi-1] + 1
            else:
                table[xi][yi] = max(table[xi-1][yi], table[xi][yi-1])
    return table[-1][-1]


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        X = ' ' + input()
        Y = ' ' + input()
        lcs = longest_common_subsequence(X, Y)
        print(lcs)

def dfs(u):
    global NOT_VISITED, VISITED, SEARCHED, t, L, stack

    stack.append(u)
    states[u] = VISITED
    discovered[u] = t = t + 1

    while len(stack) > 0:
        u = stack[-1]
        if len(L[u]) > 0:
            v = L[u].pop(0)
            if states[v] == NOT_VISITED:
                states[v] = VISITED
                discovered[v] = t = t + 1
                stack.append(v)
        else:
            stack.pop()
            states[u] = SEARCHED
            finished[u] = t = t + 1


if __name__ == '__main__':
    NOT_VISITED = 0
    VISITED = 1
    SEARCHED = 2
    t = 0

    n = int(input())
    stack = []
    L = [None]*n
    states = [NOT_VISITED]*n
    discovered = [0]*n
    finished = [0]*n
    for _ in range(n):
        u, k, *vs = input().split()
        u = int(u) - 1
        vs = [int(v) - 1 for v in vs]
        L[u] = vs

    for u in range(n):
        if states[u] == NOT_VISITED:
            dfs(u)

    for i in range(n):
        print('{} {} {}'.format(i+1, discovered[i], finished[i]))

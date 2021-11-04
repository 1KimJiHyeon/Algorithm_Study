import heapq

def dijkstra():
    q = []
    cost[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        c, node = heapq.heappop(q)
        c *= -1
        if cost[node] < c:
            continue

        for next_node, next_c in ls[node]:
            next_c += c
            if cost[next_node] > next_c:
                cost[next_node] = next_c
                heapq.heappush(q, (-next_c, next_node))
    return cost

def check_back(d):
    global s
    remove_ls = [d]
    while remove_ls:
        d = remove_ls.pop()
        for i in range(len(ls)):
            for v, p in ls[i]:
                if v == d and (cost[i] + p == cost[d]):  # 간선 중 도착지가 같고 출발점 최소비용 + 거리 == 도착점 최소비용
                    # print(v,p)
                    ls[i].remove((v, p))
                    remove_ls.append(i)

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    s, d = map(int, input().split())

    ls = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        ls[u].append((v,p))

    cost = [1e9 for _ in range(n)]
    cost = dijkstra()

    check_back(d)

    # print(ls)
    # print(cost)
    cost = [1e9 for _ in range(n)]
    cost = dijkstra()
    print(cost[d] if cost[d] != 1e9 else -1)
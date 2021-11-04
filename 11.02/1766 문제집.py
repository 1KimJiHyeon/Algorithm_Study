import heapq

n, m = map(int, input().split())
inDegree = {i:0 for i in range(1, n+1)}
priority = {i:[] for i in range(1, n+1)}
for i in range(m):
    a, b = map(int, input().split())
    priority[a].append(b)
    inDegree[b] += 1
q = []
for i in range(1, n+1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

result = []
while q:
    x = heapq.heappop(q)
    result.append(x)
    ls = sorted(priority[x])
    for i in ls:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)

for i in result:
    print(i, end=' ')
from collections import deque
n, m, s = map(int, input().split())
lines = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

for i in range(1,n+1):
    lines[i].sort()



def bfs(num):
    visited = [False for _ in range(n + 1)]
    q = [num]
    visited[num] = True
    while q:
        x = q.pop(0)
        for i in lines[x]:
            if visited[i] == False:
                result.append(i)
                q.append(i)
                visited[i] = True

def dfs(num, visited):
    visited[num] = True
    result.append(num)
    if q:
        x = q.pop()
        for i in lines[x]:
            if visited[i] == False:
                q.append((i))
                dfs(i, visited)


for i in lines:
    print(i)

result = []
visited = [False for _ in range(n + 1)]
q = [s]
dfs(s, visited)
for i in result:
    print(i, end=' ')
print()
result = [s]
bfs(s)
for i in result:
    print(i, end=' ')
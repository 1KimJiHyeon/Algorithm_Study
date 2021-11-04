n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visit = [False for _ in range(n+1)]
def dfs(v):
    visit[v] = True
    for i in adj[v]:
        if not visit[i]:
            dfs(i)

def bfs(v):
    q = [v]
    while q:
        x = q.pop(0)
        visit[x] = True
        for i in adj[x]:
            if not visit[i]:
                q.append(i)
dfs(1)
print(sum(visit)-1)
visit = [False for _ in range(n+1)]
dfs(1)
print(sum(visit)-1)
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

case = int(input())
direction = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(x,y):
    q = [(x,y)]

    while q:
        x,y = q.pop(0)

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

def dfs(x,y):
    visited[x][y] = True
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(case):
    m, n, k = map(int, input().split())
    array = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y,x = map(int, input().split())
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i,j)
                result += 1
    print(result)



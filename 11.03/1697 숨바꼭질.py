from collections import deque
n, k = map(int, input().split())

visited = [False for _ in range(100001)]
cnt = 0
def bfs(v):
    global cnt
    visited[v] = True
    q = deque([[v]])
    while q:
        x = q.popleft()
        # print(x)
        qq = []
        for i in x:
            if i == k:
                return cnt
            visited[i] = True


            if i-1 >= 0 and i-1 <= 100000 and visited[i-1] == False:
                qq.append(i-1)
            if i+1 >= 0 and i+1 <= 100000 and visited[i+1] == False:
                qq.append(i+1)
            if i*2 >= 0 and i*2 <= 100000 and visited[i*2] == False:
                qq.append(i*2)
        q.append(qq)
        cnt += 1

print(bfs(n))


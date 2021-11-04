import heapq

n = int(input())
ls = []
for i in range(n):
    heapq.heappush(ls, int(input()))

total = 0
while len(ls) >= 2:
    x = heapq.heappop(ls)
    y = heapq.heappop(ls)
    total += x+y
    heapq.heappush(ls, x+y)

print(total)
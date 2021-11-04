import heapq

n = int(input())

ls = []
result = []
def heap(val):
    if val == 0:
        if ls:
            result.append(heapq.heappop(ls))
        else:
            result.append(0)
    else:
        heapq.heappush(ls, val)

for i in range(n):
    val = int(input())
    heap(val)

for data in result:
    print(data)
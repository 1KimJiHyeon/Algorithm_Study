n, k = int(input()), int(input())
ls = list(map(int,input().split()))

ls.sort()
dist = [(ls[i+1]-ls[i], i) for i in range(n-1)]

dist.sort(key = lambda x:x[0], reverse=True)
cut = dist[:k-1]
cut.sort(key = lambda x:x[1])
# print(cut)
start = 0
total = 0
for i,idx in cut:
    end = idx
    # print(ls[start:end+1], ls[end] - ls[start])
    total += ls[end] - ls[start]
    start = end+1
# print(ls[start:-1], ls[-1] - ls[start])
total += ls[-1] - ls[start]
print(total)

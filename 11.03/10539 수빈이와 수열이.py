n, ls = int(input()), list(map(int, input().split()))

a = [ls[0]]

for i in range(1, n):
    a.append(ls[i]*(i+1) - sum(a))

for i in a:
    print(i, end=' ')

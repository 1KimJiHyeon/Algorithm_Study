n, k = map(int, input().split())
value_t = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    w, v = map(int, input().split())
    for weight in range(1, k+1):
        if w > weight:
            value_t[i][weight] = value_t[i-1][weight]
        else:
            value_t[i][weight] = max(value_t[i-1][weight-w] + v, value_t[i-1][weight])

print(max(value_t[n])) 
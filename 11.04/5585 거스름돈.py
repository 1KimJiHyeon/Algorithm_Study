n = 1000 - int(input())

back = [ 500, 100, 50, 10, 5, 1]
cnt = 0
for i in back:
    b_n = n // i
    n -= i*b_n
    cnt += b_n
print(cnt)
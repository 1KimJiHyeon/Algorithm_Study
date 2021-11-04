n, s, m = map(int, input().split())

ls = list(map(int, input().split()))

check = [s]
next = []
def func(check, val):
    possible = set()
    for i in check:
        v1 = i + val
        v2 = i - val
        if v1 >= 0 and v1 <= m:
            possible.add(v1)
        if v2 >= 0 and v2 <=m:
            possible.add(v2)
    return possible

for i in ls:
    check = func(check, i)

if len(check) == 0:
    print(-1)
else:
    print(max(check))
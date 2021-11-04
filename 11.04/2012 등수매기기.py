n = int(input())
ls = [int(input()) for _ in range(n)]

ls.sort()

unsatisfied = 0
for i in range(len(ls)):
    unsatisfied += abs(ls[i] - (i+1))

print(unsatisfied)
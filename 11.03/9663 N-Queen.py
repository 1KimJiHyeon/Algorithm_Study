def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        #대각선 체크
        if abs(row[x]-row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            #해당 위치에 퀸을 두어도 괜찮은 경우
            if check(x):
                # 다음 행으로 넘어가기
                dfs(x+1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
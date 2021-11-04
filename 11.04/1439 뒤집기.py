n = input()

pre = n[0]
zero_one = [0, 0]
zero_one[int(pre)] +=1
for i in n[1:]:
    if i == pre:
        continue
    else:
        pre = i
        zero_one[int(pre)] += 1

print(min(zero_one))
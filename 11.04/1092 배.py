n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        cnt += 1
        del_list= []
        for crane in range(len(cranes)):
            if not boxes:
                break
            for i in range(len(boxes)):
                if cranes[crane] >= boxes[i]:
                    boxes.pop(i)
                    break
            else:
                del_list.append(crane)
        aa = 0
        for i in del_list:
            del cranes[i-aa]
            aa += 1
    print(cnt)




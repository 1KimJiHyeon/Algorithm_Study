class Node:
    def __init__(self, val, left, right):
        self.parent = -1
        self.val = val
        self.left = left
        self.right = right

nodes = {}
n = int(input())

for i in range(1, n+1):
    nodes[i] = Node(i, -1, -1)

for _ in range(n):
    val, left, right = map(int, input().split())
    nodes[val].left = left
    nodes[val].right = right

    if left != -1:
        nodes[left].parent = val
    if right != -1:
        nodes[right].parent = val

for i in range(1, n+1):
    if nodes[i].parent == -1:
        root = i
        break



width = {}

cnt = 1
def preorder(val, depth):
    global cnt
    if nodes[val].left != -1:
        preorder(nodes[val].left, depth + 1)

    if width.get(depth) == None:
        width[depth] = [cnt,cnt]
    else:
        min_w, max_w = width[depth]
        width[depth] = [min(min_w, cnt), max(max_w, cnt)]
    cnt += 1
    # print(val, cnt, depth)
    if nodes[val].right != -1:
        preorder(nodes[val].right, depth + 1)


preorder(root, 1)

# print(width)
max_row = 100001
max_width = 1
for key, val in width.items():
    width = val[1] - val[0] + 1
    if width >= max_width and max_row >= key:
        max_width = width
        max_row = key
print(max_row, max_width)
n = int(input())
ls = []
class Node:
    def __init__(self, value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right
#
# class Node_mgmt:
#     def __init__(self):
#         self.nodes = []
#
#     def find_value(self, val):
#         if
# nodes = Node_mgmt()

def find_node(val, start_node):
    ls = [start_node]
    while ls:
        node = ls.pop()
        if node.value == val:
            return node
        else:
            if node.left != None:
                ls.append(node.left)
            if node.right != None:
                ls.append(node.right)
    return None


val, left, right = input().split()
start_node = Node(val)
start_node.left = Node(left) if left != '.' else None
start_node.right = Node(right) if right != '.' else None
for i in range(n-1):
    val, left, right = input().split()
    this_node = find_node(val, start_node)
    if this_node == None:
        node = Node(val)
        node.left = Node(left) if left != '.' else None
        node.right = Node(right) if right != '.' else None
    else:
        this_node.left = Node(left) if left != '.' else None
        this_node.right = Node(right) if right != '.' else None



def priorder(node):
    if node != None:
        print(f'{node.value}', end='')
        priorder(node.left)
        priorder(node.right)

def inorder(node):
    if node != None:
        inorder(node.left)
        print(f'{node.value}', end='')
        inorder(node.right)

def postorder(node):
    if node != None:
        postorder(node.left)
        postorder(node.right)
        print(f'{node.value}', end='')

priorder(start_node)
print()
inorder(start_node)
print()
postorder(start_node)


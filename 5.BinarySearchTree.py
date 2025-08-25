class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.equity = 0

def ifNodeExists(root,key):
    if root is None:
        return False
    if root.data == key:
        return True
    res1 = ifNodeExists(root.left,key)

    if res1:
        return True
    res2 = ifNodeExists(root.right,key)

    return res2

def insert(root, data):
  if root is None:
    return Node(data)
  if ifNodeExists(root, data):
      return root

  if data < root.data:
    root.left = insert(root.left, data)
  else:
    root.right = insert(root.right, data)
  return root

root = Node(data[0][0])
for i in range(1,len(data)):
 insert(root,data[i][0])

def sumCountMax(node):
    if node is None:
        return 0, 0, float('-inf')

    left_sum, left_count, left_max = sumCountMax(node.left)
    right_sum, right_count, right_max = sumCountMax(node.right)

    current_sum = node.data + left_sum + right_sum
    current_count = 1 + left_count + right_count
    current_max = max(node.data, right_max, left_max)

    return current_sum, current_count, current_max

def processInorder(node):
    if node is None:
        return
    # process left
    processInorder(node.left)
    # process root
    if node.left is not None or node.right is not None:
      avgL = 0
      maxL = float('-inf')
      if node.left:
          sumL, numL, maxL = sumCountMax(node.left)
          avgL = sumL / numL if numL > 0 else 0
      else:
          avgL,maxL = 1,1
      avgR = 0
      maxR = float('-inf')
      if node.right:
          sumR, numR, maxR = sumCountMax(node.right)
          avgR = sumR / numR if numR > 0 else 0
      else:
        avgR,maxR = 1,1
      node.equity = 1 - abs((avgL / maxL) - (avgR / maxR))
      # print(f"Equity of {node.data} is {node.equity}")
    else:
      node.equity = 1
      # print(f"Equity of {node.data} is {node.equity}")

    # process right
    processInorder(node.right)

def find_max_equity(root):
    if root is None:
        return float('-inf')

    max_equity = root.equity if (root.left or root.right) else float('-inf')

    left_max_equity = find_max_equity(root.left)
    right_max_equity = find_max_equity(root.right)

    return max(max_equity, left_max_equity, right_max_equity)

def print_nodes_with_equity(root, target_equity):
    if root is None:
        return

    if (root.left or root.right) and root.equity == target_equity:
        print(f"Node: {root.data}, Equity: {root.equity}")

    print_nodes_with_equity(root.left, target_equity)
    print_nodes_with_equity(root.right, target_equity)

filename = input("Enter the filename: ")
data = []
with open(filename,'r') as file:
  for line in file:
    row = [float(num) for num in line.strip().split()]
    data.append(row)

processInorder(root)
max_equity_value = find_max_equity(root)

if max_equity_value != float('-inf'):
    print(f"\nNon-leaf node(s) with maximum equity ({max_equity_value}):")
    print_nodes_with_equity(root, max_equity_value)


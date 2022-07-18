# Q. 11725
import sys
from collections import defaultdict
class Node(data, connected_node):
    self.data = data
    self.connected_node = connected_node
    
n = int(sys.stdin.readline())
tree = defaultdict(list)

for _ in range(n):
    a, b = sys.stdin.readline().split()
    tree[a].append(b)
    tree[b].append(a)
    

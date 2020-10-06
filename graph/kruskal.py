import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n, m = map(int, input().split())
parent = [0]*(n+1)
edges = []
result = 0

for _ in range(m):
  a, b, c = map(int, input().split())  # a에서 b로 연결할 때 비용이 c
  edges.append((c, a, b))             

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
  
print(result)
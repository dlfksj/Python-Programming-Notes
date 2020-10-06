# 트리를 이용해 서로소 집합을 계산하는 알고리즘
# 1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다
#    1-1. A와 B의 루트 노드 A', B'을 찾는다
#    1-2. A'을 B'의 부모 노드로 설정한다.
# 2. 모든 union 연산을 처리할 때까지 1번 과정을 반복한다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아닐 때
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1)
for i in range(1, v+1):    # 부모를 자기 자신으로 초기화
  parent[i] = i

# union 연산을 각각 수행
for i in range(e) :
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v+1):
  print(parent[i], end=' ')
from collections import deque

def topology_sort(graph, v):
  result = []
  q = deque()
  # 진입차수가 0인 노드를 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기 (간선 제거)
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  return result


v, e = map(int, input().split())  # 노드, 간선 수 
indegree = [0]*(v+1)              # 모든 노드에 대한 진입차수 초기화
graph = [[] for _ in range(v+1)]  

# 간선 정보 입력 받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)              # a에서 b로 이동
  indegree[b] += 1

# 위상 정렬
result = topology_sort(graph, v)
for i in result:
  print(i, end=' ')

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())    # n: 노드 개수, m: 간선 개수
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if i==j: graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())  # a번 노드에서 b번 노드로 가는 비용이 c일 때
    graph[a][b] = c

# 플로이드-워셜 알고리즘
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과 출력
for a in range(1,n+1):
  for b in range(1,n+1):
    # 도달할 수 없는 경우
    if graph[a][b] == INF:
      print("INFINITY", end=' ')
    else:
      print(graph[a][b], end=' ')
  print()

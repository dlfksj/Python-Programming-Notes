import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, n, start):
    """
    Dijkstra shortest path
    :param graph:
    :param n: number of nodes
    :param start: start node
    :return: shortest distance from the start node to the end node
    """
    # initialize the distance
    distance = [INF]*(n+1)

    # Set the start node
    q = []
    heapq.heappush(q, (0, start))
    distance[start] =0

    # Until the queue is empty
    while q:
        # Pop the node who has the shortest path
        dist, now = heapq.heappop(q)
        # 현재 노드가 처리된적 있으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 인접해있는 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


n, m = map(int, input().split())    # n: 노드 개수, m: 간선 개수
start = int(input())                # 시작 노드
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # a번 노드에서 b번 노드로 가는 비용이 c일 때
    graph[a].append((b, c))

# Run the Dijkstra algorithm to find the shortest distance
distance = dijkstra(graph, n, start)
print(distance)
# Print all the shortest paths to all nodes
for i in range(1, n+1):
    # 시작 노드에서 i번 노드로 갈 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 시작 노드에서 i번 노드로 갈 수 있으면 최단 거리 출력
    else:
        print(distance[i])
        
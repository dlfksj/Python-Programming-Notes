import sys
input = sys.stdin.readline

n = int(input())                         # 수열 길이
data = list(map(int, input().split()))   # 수열

# i번째 원소를 마지막으로 하는 LIS의 길이를 dp 리스트에 저장
dp = [1]*n   

for i in range(1, n):
  for j in range(0, i):
    if data[j] < data[i]:
      dp[i] = max(dp[i], dp[j]+1)

# 가장 긴 부분 수열의 길이 출력
print(max(dp))
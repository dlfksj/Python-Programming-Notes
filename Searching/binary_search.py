def binary_search(ary, target, start, end):
  while(start <= end):  
    mid = (start+end)//2
    if ary[mid] == target:
      return mid
    elif ary[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

# 원소 개수와 찾으려는 숫자
n, target = list(map(int, input().split()))
# 전체 원소
ary = list(map(int, input().split()))

result = binary_search(ary, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않음")
else:
  print(result+1)
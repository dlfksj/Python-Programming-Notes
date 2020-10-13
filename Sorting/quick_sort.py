ary = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(ary):
  if len(ary) <= 1:
    return ary
  
  pivot = ary[0]   # 맨 첫번째 원소가 pivot
  tail = ary[1:]   # pivot을 제외한 나머지가 리스트

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(ary))
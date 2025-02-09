# O(n log n) 알고리즘의 코드이다.
#
# n : 수열의 길이
# a[] : 수열
# tempArr[] : 임시로 수를 저장하는 공간, 초기값 = [a[0]]
#     - 항상 정렬된 형태이다.
# resultArr[] : 증가하는 부분 수열, 초기값 = [a[0]]


#
# 0 <= i < n 에 대하여:
#   tempArr 에서 a[i] 가 들어갈 공간을 binarySearch 로 찾는다.
#
#     Case 1. a[i] 가 tempArr 에서 제일 큰 값일 경우
#       - 가장 긴 부분수열이 갱신된 상황이다.
#       - tempArr 맨 뒤에 a[i] 를 추가한다.
#       - resultArr 에 tempArr 를 복사한다.
#
#     Case 2. tempArr[k] == a[i]
#       - 아무것도 안해도 된다.
#       - 코드의 일관성을 위해 tempArr[k] 에 a[i] 를 넣었다.
#
#     Case 3. tempArr[k] < a[i] <= tempArr[k + 1]
#       - tempArr[k] 에 a[i] 를 넣는다.
#
#     Case 4. a[i] < tempArr[0]
#       - tempArr[0] 에 a[i] 를 넣는다.


import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

tempArr = [a[0]]
resultArr = [a[0]]

# tempArr[] 에서 val 이 들어갈 위치를 찾는다.
# tempArr[k] == val 이면 k 를 리턴한다.
def findPlace(e):
  start = 0
  end = len(tempArr) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if tempArr[mid] == e:
      return mid
    elif tempArr[mid] < e:
      start = mid + 1
    else:
      end = mid - 1
  return start
  
for i in range(1, n):
  val = a[i]
  if val > tempArr[-1]:
    tempArr.append(val)
  else:
    valIdx = findPlace(val)
    tempArr[valIdx] = val
    
print(len(tempArr))
  
  
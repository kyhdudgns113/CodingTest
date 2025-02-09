# n : 정사각형 배열 한 변의 길이
# k : 임의의 수
#
# 상황
#   - A[i][j] = i * j, (1 <= i, j <= n)
#   - B[] : A[i][j] 를 오름차순으로 정렬한 일차원 배열
#
# 구하는것
#   - B[k] (B[] 의 인덱스는 1부터 시작한다.)
#
# 아이디어
#   - 주어진 범위의 값 중에서
#   - 그것보다 작은 A[][] 원소의 갯수가 (k - 1) 이하 인 값을 찾는다.
#     - 그 경우는 여러개가 있는데, 그 중 최대값으로 한다.
#
#   Q) 기준이 k - 1 이하 인 이유?
#   A) A[][] 원소가 B[k] 보다는 작은 값들만 세야하기 때문이다.
#   
#   Q) 그 중 최대값이여야 하는 이유?
#   A) 본인보다 작은 A[][] 의 갯수가 같은 숫자가 여럿 존재할 수 있다.
#      그 중 최대값이 아닌 것들은 A[][] 에 존재하지 않는다.
#        그 중 최대값을 x 라고 하자.
#        f(x + 1) = x + 1 보다 작은 A[][] 원소의 갯수는
#         = "x 보다 작은 A[][] 의 갯수" + "A[][] 에서 x 의 개수"
#         = f(x) + "A[][] 에서 x 의 개수"
#        f(x + 1) 이랑 f(x) 가 같다면 "A[][] 에서 x 의 개수" 가 0이라는 뜻이다.
#        따라서 x 는 A[][] 에 없다는 뜻이 된다.
#      
#         n = 3 이라고 하면
#           [1 2 3]
#           [2 4 6]
#           [3 6 9]
#         5 랑 6 모두 본인보다 작은 원소 개수는 6이다.
#         
#
# 풀이
#   start=0, end=min(10^9, n*n) 의 범위에서
#     mid = (start + end) // 2
#     A[][] 에서 mid 보다 작은 원소의 갯수를 구한다.
#       = lessThenMid
#     Case 1.
#       lessThenMid > k - 1 
#         A[][] 의 원소중에서
#         mid 보다 작은 원소의 갯수가
#         B[k] 보다 작은 원소의 갯수보다 큰 경우
#         mid 는 무조건 B[k] 보다 크다. 
#         따라서 범위를 (start, mid - 1) 로 한다.
#     Case 2.
#         lessThenMid <= k - 1
#         mid 도 가능하다.
#         mid 보다 큰 수도 가능하다.
#         범위를 (mid, end) 로 한다.
#     종료조건에 대해서는 findBk 함수 내에서 설명했다.

import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

n = int(input())
k = int(input())

# A[][] 원소중, val 보다 작은 원소의 갯수를 리턴한다.
# 각 행(row) 에 대하여 다음 연산을 수행한다.
#   1 <= row <= n
#     A[row][...] 의 원소중에서 (val - 1) 이하인 갯수를 다 더한다.
#     (val - 1) // row 들을 더하면 된다.
def findLessCnt(val):
  global n
  result = 0
  for i in range(1, n + 1):
    if (val - 1) >= n * i:
      result += n
    elif val - 1 >= i:
      result += (val - 1) // i
    else:
      break
  return result

def findBk(start, end):
  global k
  # start 랑 end 가 같으면 리턴해야지...
  if start == end:
    return start
  
  # end = start + 1 일 때때
  # end 보다 작은 A[][] 의 갯수가 k - 1 보다 크다는건
  # B[k] 는 end 보다는 작다는 뜻이다.
  # 따라서 이 경우에는 start 를 리턴하고, 아니면 end 를 리턴한다.
  if start + 1 == end:
    if findLessCnt(end) > k - 1:
      return start
    return end
  
  mid = (start + end) // 2
  
  lessThenMid = findLessCnt(mid)
  
  if lessThenMid > k - 1:
    return findBk(start, mid - 1)
  else:
    return findBk(mid, end)
  
print(findBk(0, min(10 ** 9, n * n)))
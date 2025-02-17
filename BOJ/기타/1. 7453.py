#
# n : 배열의 크기 (n <= 4,000)
# a[], b[], c[], d[] : 크기가 n 인 배열. abs(a[i]) <= 2^28
#
# 구하는것
#   a[ia] + b[ib] + c[ic] + d[id] = 0 인 쌍의 갯수
#
# 풀이
#   ab 라는 dictionary 자료구조를 만든다.
#   모든 ia, ib 에 대하여
#     ab[ a[ia] + a[ib] ] 를 1 더한다.
#       a[ia] + b[ib] 를 만드는 경우가 1 있다는 의미다.
#   모든 ic, id 에 대하여
#     -(c[ic] + d[id]) 가 ab 에 있는지 여부를 확인하면 된다.
#
# 연산량
#   첫 번째 단계 : O(n) * O(n) * O(log 숫자범위)
#   두 번째 단계 : O(n) * O(n) * O(log 숫자범위)
#   = 대략 1억정도이다.
#   주어진 시간이 12초라서 간당간당하다.
#   pypy 로 돌려야 돌아간다.

import sys

input = sys.stdin.readline

n = int(input())
a, b, c, d = [[0 for i in range(n)] for j in range(4)]

for i in range(n):
  aa, bb, cc, dd = map(int, input().split())
  a[i] = aa
  b[i] = bb
  c[i] = cc
  d[i] = dd
  
a.sort()
b.sort()
c.sort()
d.sort()

ab = {}

for i in range(n):
  for j in range(n):
    try:
      ab[a[i] + b[j]] += 1
    except:
      ab[a[i] + b[j]] = 1

result = 0
for i in range(n):
  for j in range(n):
    try:
      result += ab[-(c[i] + d[j])]
    except:
      result += 0
      
print(result)
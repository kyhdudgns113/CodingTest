# n : 사람 수
# p[] : 사람마다 돈 뽑는데 걸리는 시간
#
# result : 모든 사람들이 돈 뽑을때까지 걸리는 시간의 최소값.
#
# result = sum(p[i] * (n - i)) (0 <= i < n) 이다.
# i 가 작을수록 (n - i) 가 커진다.
# i 가 작을수록 p[i] 가 작아야 result 가 최소값을 갖는다.
#   -> p[i] 를 오름차순으로 정렬해야 한다.

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(n):
  result += (n - i) * p[i]
  
print(result)

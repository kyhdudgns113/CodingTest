# f[0] = 0, f[1] = 1, f[2] = 1
# f[n] = f[n - 1] + f[n - 2]
#      = 2*f[n - 2] + f[n - 3]
#      = 3*f[n - 3] + 2*f[n - 4]
#      = f[k]*f[n - k + 1] + f[k - 1]f[n - k]
#
# 1. n 대신에 2n, k 대신에 n 을 넣으면
#   f[2n] = f[n]*f[n + 1] + f[n - 1]*f[n]
#         = f[n]*(f[n] + f[n - 1]) + f[n]*f[n - 1]
#         = f[n]*(f[n] + 2*f[n - 1])
#
# 2. n 대신에 2n+1, k 대신에 n 을 넣으면
#   f[2n + 1] = f[n + 1]*f[n + 1] + f[n]*f[n]
#
# 이를 재귀함수로 구현했다.

import sys

input = sys.stdin.readline

n = int(input())

dic = {}

def fibonacci(n):
  g = 1000000007
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  
  try:
    if dic[n] > 0:
      return dic[n]
  except:
    a = 1
  
  m = n // 2
  if n % 2 == 0:
    fm = fibonacci(m)
    fm1 = fibonacci(m - 1)
    dic[n] = fm * (fm + 2*fm1) % g
    return dic[n]
  else:
    f0 = fibonacci(m)
    f1 = fibonacci(m + 1)
    dic[n] = (f1*f1 + f0*f0) % g
    return dic[n]
  
print(fibonacci(n))
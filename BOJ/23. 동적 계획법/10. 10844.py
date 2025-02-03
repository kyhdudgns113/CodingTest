#
# results[n : 자릿수][a : 0~9]
#   - n번째 자릿수가 a 인 계단수의 경우
# = results[n - 1][a - 1] + results[n - 1][a + 1]
#
# a 의 범위에만 유의하면 된다.

n = int(input())

results = [[0 for i in range(10)] for j in range(n)]

g = 10 ** 9

for i in range(1, 10):
  results[0][i] = 1

for i in range(1, n):
  for j in range(10):
    res = 0
    if j > 0:
      res += results[i - 1][j - 1]
    if j < 9:
      res += results[i - 1][j + 1]
    results[i][j] = res % g
    
print(sum(results[n - 1]) % g)
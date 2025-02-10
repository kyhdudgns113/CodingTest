import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for i in range(n))

result = [0 for i in range(10001)]

for i in range(n):
  if coins[i] > k:
    continue
  result[coins[i]] += 1
  for w in range(1, k + 1 - coins[i]):
    result[w + coins[i]] += result[w]      

print(result[k])
  
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
  coins.append(int(input()))
  
# coins[i] = 정수*coins[i - 1] 임을 이용한다.

result = 0
remain = k
for i in range(n):
  spendCoin = remain // coins[n - 1 - i]
  result += spendCoin
  remain -= spendCoin * coins[n - 1 - i]

print(result)
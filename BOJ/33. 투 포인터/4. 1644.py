#
# n : 임의의 수 (n <= 4,000,000)
#
# 상황
#   n = 5 일때, 연속된 소수의 합으로 나타내는 경우는 다음과 같다
#     1. 2 + 3
#     2. 5
#
# 구하는것
#   n 을 연속된 소수로 나타내는 경우의 수
#
# 풀이
#   오름차순 소수의 배열을 구한다.
#   left = 0, right = 0 으로 두고 각각 한 칸씩 우측으로 이동하며 구간합을 구한다.
#   그것이 n 이 될때마다 카운팅을 한다.
#
#   if 구간합 <= n:
#     구간합을 더 키워야 한다.
#     구간합 개수가 많아져야 하므로 right 를 1 늘릴 수 있으면 늘린다.
#     right 가 벽면에 닿았으면 left 를 1 늘린다.
#   if 구간합 > n:
#     구간합을 줄여야 한다.
#     left 를 1 늘리면 된다.

CONST = 4000003

n = int(input())

isPrime = [1 for i in range(CONST)]

isPrime[0] = 0
isPrime[1] = 0

# 소수가 아닌것들을 구한다
for i in range(2, 2001):
  if isPrime[i] == 0:
    continue
  for j in range(2, CONST // i):
    isPrime[i * j] = 0
    
# 소수들만 선별하여 넣는다.
primes = [val for val in range(CONST) if isPrime[val] == 1]
lenPrime = len(primes)

l = 0
r = 0
tempSum = primes[0]
result = 0

while l < lenPrime:
  if tempSum == n:
    result += 1
  
  if tempSum <= n:
    if r < lenPrime - 1:
      r += 1
      tempSum += primes[r]
    else:
      tempSum -= primes[l]
      l += 1
  else:
    tempSum -= primes[l]
    l += 1
    
print(result)
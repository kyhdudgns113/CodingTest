# nCk % g
# n, k = 입력
# g = 1000000007 (10억 7)
#  
# nCk = (n * (n - 1) * (n - 2) ... (n - k + 1)) / k!
#
# 분자를 N, 분모를 K 라고 두면
# nCk % g = (N/K) % g
# = (N % g) * (K^-1 % g) % g
#
# g 가 소수일때
#
# K^g % g = K
# K^(g - 1) % g = 1
#
# 여기서 K^(g - 1) = K*K^(g - 2) 이므로
# 위의 식은
# [K * K^(g - 2)] % g = 1
# [(K % g) * (K^(g - 2) % g)] % g = 1
#
# 그런데
# [(K % g) * (K^(-1) % g)] = 1 이므로
# K^(-1) % g = K^(g - 2) % g 이다.
#
# 그러면 
# (N % g) * (K^(-1) % g) % g
# = (N % g) * (K^(g - 2) % g) % g 이다.
#
# K^(g - 2) 에서 G 는 매우 큰 수 이므로 분할정복으로 구한다.
n, k = map(int, input().split())
g = 1000000007

N = 1
K = 1

m = min(k, n - k)

for i in range(0, m):
  N = (N * (n - i)) % g
  K = (K * (i + 1)) % g

print(N, K)
  
Kexps = [1, K % g]
temp = 1
while temp <= g:
  val = Kexps[-1]
  Kexps.append((val * val) % g)
  temp *= 2
  
KexpP2modG = 1
idx = 0
g2 = g - 2
while g2 > 0:
  if g2 % 2 == 1:
    KexpP2modG = (KexpP2modG * Kexps[idx]) % g
  g2 //= 2
  idx += 1
  
result = (N * KexpP2modG) % g
print(result)

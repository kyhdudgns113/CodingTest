# n > 5 일때
# f[n] : n 번째 정삼각형의 한 변의 길이
# f[n] = f[n - 5] + f[n - 1] 이다.

t = int(input())

p = [0 for i in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2

for i in range(6, 101):
  p[i] = p[i - 1] + p[i - 5]

for _ in range(t):
  n = int(input())
  print(p[n])
n = int(input())

# f[1] = 1, f[2] = 1
# f[n] = f[n - 1] + f[n - 2]
# 위 점화식을 재귀로 한 번 풀어봤다.

f = [0 for i in range(n + 1)]
f[1] = 1
f[2] = 1
def func(n):
  if f[n] > 0:
    return f[n]
  f[n] = func(n - 1) + func(n - 2)
  return f[n]

print(func(n), n - 2)
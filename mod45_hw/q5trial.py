def f(k):
    k5 = 5**k
    k4 = 4**k
    k3 = 3**k
    k2 = 2**k
    k1 = 1**k
    num = k5 - 5 * k4 + 10 * k3 - 10 * k2 + 5 * k1
    return num / k5

ans = 0
for k in range(5, 1000):
    ans += k * (f(k) - f(k - 1))
print(ans)

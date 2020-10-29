def f(k):
    k5 = 5**k
    k4 = 4**k
    k3 = 3**k
    k2 = 2**k
    k1 = 1**k
    num = k5 - 5 * k4 + 10 * k3 - 10 * k2 + 5 * k1
    return num / k5

exp = 0
exp2 = 0
for k in range(5, 10000):
    exp += k * (f(k) - f(k - 1))
    exp2 += k * k * (f(k) - f(k - 1))
print(exp)
print(exp2 - exp * exp)

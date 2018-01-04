def sumOfGP(a, r, n):
    sum = 0
    i = 0
    while i < n:
        sum = sum + a
        a = a * r
        i = i + 1

    return sum




a = 1
r = (float)(1 / 2.0)
n = 10

print("%.5f" % sumOfGP(a, r, n)),
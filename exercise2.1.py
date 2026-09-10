# Exercise 2.1
def minarray(xs):
    m = xs[0]

    for x in xs:
        if x < m:
            m = x

    return m


data = [4, 1, 5, 0, 3, 2]
minimum = minarray(data)

print(minimum)
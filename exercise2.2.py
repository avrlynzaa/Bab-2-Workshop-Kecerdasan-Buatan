# Exercise 2.2
def sortarray(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] > xs[j]:
                xs[i], xs[j] = xs[j], xs[i]

    return xs


data = [4, 1, 5, 0, 3, 2]
sorted_data = sortarray(data)

print(sorted_data)
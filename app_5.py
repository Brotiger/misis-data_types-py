x = float(input("x:"))
y = float(input("y:"))
z = float(input("z:"))

result = x**2 * (y ** 0.5 + z ** 0.5) * (1 / (x ** 6 + y ** 0.5) ** 0.5) - ((3 * x) ** 0.5) + z ** 11
print("{:.3f}".format(result))
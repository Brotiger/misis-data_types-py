input_number = int(input("Введите число:"))

x1 = (input_number // 100000) % 10
x2 = (input_number // 10000) % 10
x3 = (input_number // 1000) % 10

y1 = input_number % 10
y2 = (input_number // 10) % 10
y3 = (input_number // 100) % 10

print(int(((x1 & y1) / x1) and ((x2 & y2) / x2) and ((x3 & y3) / x3)))
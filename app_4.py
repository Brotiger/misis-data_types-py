input_number = int(input("Введите число:"))
first_half = (input_number // 100000) % 10 * 100 + (input_number // 10000) % 10 * 10 + (input_number  // 1000) % 10
second_half = (input_number // 100) % 10 + (input_number // 10) % 10 * 10 + input_number % 10 * 100
print(round(first_half / second_half))

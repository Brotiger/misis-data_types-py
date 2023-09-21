input_number = int(input("Введите число:"))
even = (input_number % 10) * 100 + (input_number // 100) % 10 * 10 + (input_number // 10000) % 10
odd = (input_number // 100000) % 10 * 100 + (input_number // 1000) % 10 * 10 + (input_number // 10) % 10
product = even * odd
print(f"{even}#{odd}#{product}")
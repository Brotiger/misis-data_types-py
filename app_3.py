input_minutes = int(input("Введите количество минут:"))
days_count = (input_minutes // (60 * 24))
print(f"{(input_minutes - days_count * 24 * 60) // 60:02}:{input_minutes % 60:02}")
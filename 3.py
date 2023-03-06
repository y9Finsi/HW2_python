# наши переменные
count = 0
sum = 0

# считываем числа из данных
while True:
    num = int(input())
    if num == 0:
        break
    sum += num
    count += 1

# вычисляем среднее арифметическое
if count > 0:
    average = sum / count
    print(average)
else:
    print("Ошибка!")

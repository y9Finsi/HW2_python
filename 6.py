n = int(input())
summa = 1
f = 1
for i in range(1, n + 1):
    f=f/i # вычисляем значение дроби 1/i и сохраняем в f
    summa+=f # добавляем значение f к сумме s
print(((summa*100000)//1)/100000) # выводим результат с округлением до 5 знаков после запятой
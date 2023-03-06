# получаем колво N
N = int(input())

# устанавливаеем флаг на тру. 
flag = False

# Тут цикл где мы просим ввести N
for i in range(N):
    num = int(input())
    if num == 0: # Если число равно 0, меняем флаг и выходим из цикла
        flag = False 
        break

# А теперь проверяем флаг и выводим рез.
if flag:
    print("YES")
else:
    print("NO")
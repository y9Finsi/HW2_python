# генератор списка по условию a % i == 0 для i в диапазоне от 1 до (a//2)+1. Затем функция sum суммирует все элементы списка.
a = int(input())
k = sum(1 for i in range(1, (a//2)+1) if a % i == 0) + 1
print(k)

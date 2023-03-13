prev = int(input()) # первое 
curr = int(input()) # второе
max_len = curr_len = 1 # ин. переменные максимальной и теуущей

while curr != 0 and prev != 0:  # пока оба значения не равны 0
    if curr == prev: # если значения равны
        curr_len = 1
    elif curr > prev: # если текущее значение больше предыдущего
        curr_len += 1
    else:
        max_len = max(max_len, curr_len) # если текущее значение меньше предыдущего
        curr_len = 1
    prev = curr
    curr = int(input())

max_len = max(max_len, curr_len)
print(max_len)

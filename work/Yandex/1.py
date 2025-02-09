import math
def eratosfen(n):
    a = set(range(2, n))
    for i in range(2, int(math.sqrt(n))):
        if i in a:
            a -= set(range(2*i, n, i))
    return len(a)
print(eratosfen(100))
#Возьмем массив чисел от двух (так как два первое простое число) до N не включительно.
#Далее начнем проверять массив на числа делящиеся на числа от начала массива до корня ( Так как один из делителей составного числа n обязательно <= корню N) от N. 
#При нахождении данного числа удаляем его из массива. Считаем количество оставшихся чисел в массиве.
def eratosfen(n):
    a = set(range(2, n))
    for i in range(2, int(math.sqrt(n))):
        if i in a:
            a -= set(range(2*i, n, i))
    return len(a)



# a = N/k  это длинна коротких подмассивов.
# b = остаток от N/k  это колличество подмассивов с длинной "a+1".
# с = k - b    это количество подмассивов с длинной "a".

# k может быть больше N в том случаи если нас устраивают массивы нуливой длинны


# Берем первые три элемента и определяем по ним направление возрастания чисел в массиве (Если два крайних меньше второго, то нашли сразу) . Далее проверяем центр массива, если меньше первых элементов, то идем против напротив направления возрастания чисел в массиве. Далее рекурсивно тоже самое. Сложность O(корень от N).

# Если массив содержит повторяющиеся числа сложность увеличиться на константу, но при оценки сложности через "O" константы не учитываются
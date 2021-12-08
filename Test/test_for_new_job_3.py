'''3. На языке Python или С/С++, написать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить почему вы считаете, что функция соответствует заданным критериям.'''

def quick_sort(arr):
    w = [None for x in range(4 + len(arr) // 2)]#создаём стек
    k = 0#позиция верха стека
    w[0] = 0#указатель на позицию левой границы половины
    w[1] = len(arr) - 1#-||- правой
    while (k >= 0):
        i1, i2 = quick_sort_pos(arr, w[k], w[k + 1]) # границы опорных элементов
        if(i2 != w[k + 1]):RL =i2 + 1#левая граница правого подъинтервала
        else:RL =w[k + 1]
        RR = w[k + 1]#Правая граница правого подъинтервала
        LL = w[k]#Левая граница левого подъинтервал
        if(i1 != w[k]):LR =i1 - 1#Правая граница левого подъинтервал
        else:LR =w[k]
        k -= 2#удалить текущий интервал
        if (RL != RR):k += 2; w[k] = RL; w[k + 1] = RR
        if (LL != LR):k += 2; w[k] = LL; w[k + 1] = LR

def quick_sort_pos(arr, left, right):
    j = left + 1
    k = left + 1
    l = 1
    for i in range(left + 1, right + 1):
        if arr[i] < arr[left]:
            if i != j: # для тех случаев когда перемещение не тредуеться
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        if arr[i] == arr[left]:
            if i != k: # для тех случаев когда перемещение не тредуеться
                arr[i], arr[k] = arr[k], arr[i]
            j += 1
            k += 1
            l += 1
    for i in range(left, left + l): # перемещяем опорный элемент и равные опорному элементу
        arr[i], arr[j-1-i+left] = arr[j-1-i+left], arr[i]
    return j-l, j-1



a = [5, 1, 5, 6, 5, 12, 5, 29, 17, 1, 6, 3, 19, 4]

if __name__ == "__main__":
    print(f'before sort {a}')
    # print('after sort quick_sort_pos ', quick_sort_pos(a, 0, 12))
    # print('after sort quick_sort_pos ', quick_sort_pos(a, 0, 3))
    # print('after sort quick_sort_pos ', quick_sort_pos(a, 0, 2))
    # print('after sort quick_sort_pos ', quick_sort_pos(a, 8, 12))
    print('after sort ', quick_sort(a))
    print(f'after sort {a}')
  
'''В среднем случаи время работы нашего алгоритма O(n log n) и в худшем O(n**2).
В теории асимптотически имеет такоеже время работы как и сортировка слиянием, но на практике обычно быстрее.
'''

def QuickSort(a):
    w = [x for x in range(4 + len(a) // 2)]#создаём стек
    k = 0#дно
    w[0] = 0#указатель на позицию левой границы половины
    w[1] = len(a) - 1#-||- правой
    while (k >= 0):
        i = QuickSortPos(a, w[k], w[k + 1])
        if(i != w[k + 1]):RL =i + 1#левая граница правого подъинтервала
        else:RL =w[k + 1]
        RR = w[k + 1]#Правая граница правого подъинтервала
        LL = w[k]#Левая граница левого подъинтервал
        if(i != w[k]):LR =i - 1#Правая граница левого подъинтервал
        else:LR =w[k]
        k -= 2#удалить текущий интервал
        if (RL != RR):k += 2; w[k] = RL; w[k + 1] = RR
        if (LL != LR):k += 2; w[k] = LL; w[k + 1] = LR

def QuickSortPos(a, left, right):
    i = left
    j = right - 1
    while (True):#чтобы поставить разделяющий элемент на свое место
        while (a[i] < a[right]): i+=1
        while (a[j] > a[right] and j > left): j-=1
        if (i >= j): break
        a[i],a[j] = a[j],a[i]
    a[right],a[i]  = a[i],a[right]
    print(a)
    return i

b = [243, 234, 244, 243, 1, 5, 3, 2, 5, 6, 8]
QuickSort(b)
print(b)
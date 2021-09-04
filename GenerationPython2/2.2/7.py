'''Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит Тимур, Руслан или они сыграют вничью.
Sample Input 1:

камень
бумага
Sample Output 1:

Руслан'''
a = input()
b = input()
if (a == b):
    print('ничья')
elif ((a == 'камень' and b == 'ножницы') or (a == 'ножницы' and b =='бумага') or (a == 'бумага' and b == 'камень')):
    print('Тимур')
else:
    print('Руслан')
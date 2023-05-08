"""
    Задача "клумбы"
    Даны координаты отрезков - начало и конец.
    Необходимо объединить все пересекающиеся отрезки.

    На вход подается:
    n - число отрезков.
    В остальных строках - сами отрезки.

    Пример входных данных:
    4
    2 3
    5 6
    3 4
    3 4
"""

n = int(input())
# входные данные превращаем в массив массивов: [[2, 3], [5, 6], [3, 4], [3, 4]]
# а так же переводим строки в числа
array = [[int(x) for x in input().split()] for _ in range(n)]

# сортируем по возрастанию первой координаты каждый отрезок:
array.sort(key=lambda x: x[0])
# В массив результатов добавляем первый отрезок:
result = [array[0]]
for i in range(1, n):  # перебираем со второго

    start = array[i][0]
    end = array[i][1]
    result_end = result[-1][1]
    if start <= result_end:  # если конец предыдущего > начало следующего - они пересекаются
        if end > result_end:
            result[-1][1] = end  # если конец текущего дальше чем конец предыдущего - обновляем
    else:
        result.append(array[i])  # если текущий отрезок и предыдущий не пересекаются - добавляем в results

for x, y in result:
    print(x, y)

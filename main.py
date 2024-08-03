'''Обратный порядок

Напишите программу, которая принимает произвольное количество строк
и в каждой введенной строке располагает все символы в обратном порядке.

https://stepik.org/lesson/520159/step/10?unit=512678'''


# import sys

# for line in sys.stdin.readlines():
#     print(line.strip()[::-1])

'''Размах данных
Дана последовательность дат. Напишите программу,
которая выводит количество дней между максимальной и минимальной датами 
данной последовательности.

Формат входных данных
На вход программе подается произвольное количество строк,
в каждой строке записана дата в ISO формате (YYYY-MM-DD).

https://stepik.org/lesson/520159/step/11?unit=512678'''

# import sys
# from datetime import date

# list_date = list(map(lambda x: date.fromisoformat(x.strip('\n')), sys.stdin))
# print((max(list_date) - min(list_date)).days)


'''Лемма о трёх носках

https://stepik.org/lesson/520159/step/12?unit=512678'''


# import sys

# lst_in = list(map(int, sys.stdin))
# if lst_in[-1] % 2 == 0 and len(lst_in) % 2 != 0:
#     print('Анри')
# elif lst_in[-1] % 2 != 0 and len(lst_in) % 2 == 0:
#     print('Анри')
# else:
#     print('Дима')


'''Урок статистики

https://stepik.org/lesson/520159/step/13?unit=512678'''


# import sys

# lst_in = list(map(int, sys.stdin))
# if lst_in == []:
#     print('нет учеников')
# else:
#     print(f'Рост самого низкого ученика: {min(lst_in)}')
#     print(f'Рост самого высокого ученика: {max(lst_in)}')
#     print(f'Средний рост: {sum(lst_in)/len(lst_in)}')


'''Комментатор

https://stepik.org/lesson/520159/step/14?unit=512678

'''

# import sys

# cnt = 0
# for line in sys.stdin:
#     if line.lstrip().startswith('#'):
#         cnt += 1
# print(cnt)


'''Без комментариев

https://stepik.org/lesson/520159/step/15?unit=512678

'''

# import sys

# cnt = 0
# for line in sys.stdin:
#     if not line.lstrip().startswith('#'):
#         print(line.rstrip())


'''Панорамное агенство

https://stepik.org/lesson/520159/step/16?unit=512678

'''


# import sys

# f = sys.stdin.read()
# res = [line.split(' / ') for line in f.splitlines()]
# target = res[-1][0]
# del res[-1]
# res.sort()
# res.sort(key= lambda x: float(x[-1]))
# for row in res:
#     if row[1] == target:
#         print(row[0])


'''Это точно Python?

https://stepik.org/lesson/520159/step/17?unit=512678

'''


# import sys
# from datetime import date, time


# dt_in = sys.stdin
# res = []

# for d in dt_in:
#     d, m, y = d.split('.')
#     d = date(int(y), int(m), int(d))
#     res.append(d)
    
# if res == sorted(res) and len(res) == len(set(res)):
#     print('ASC')
    
# elif res == sorted(res)[::-1] and len(res) == len(set(res)):
#     print('DESC')
    
# else:
#     print('MIX')


'''Гуру прогрессий

https://stepik.org/lesson/520159/step/18?unit=512678

'''

# import sys

# def is_arithmetic_progression(lst):
#     dif = lst[1] - lst[0]
#     j = 1
#     flag = True
#     for i in range(2, len(lst)):
#         if lst[i] - lst[j] == dif:
#             flag
#             j += 1
#         else:
#             flag = False
#             break
#     return flag
        
# def is_geometric_progression(lst):
#     flag = True
#     div = lst[1] / lst[0] 
#     j = 1
#     for i in range(2, len(lst)):
#         if lst[i] / lst[j] == div:
#             flag
#             j += 1
#         else:
#             flag = False
#             break
#     return flag

# data = list(map(int, sys.stdin.readlines()))

# def main():
#     if is_arithmetic_progression(data):
#         return 'Арифметическая прогрессия'
#     if is_geometric_progression(data):
#         return 'Геометрическая прогрессия'
#     else:
#         return 'Не прогрессия'
    
# print(main())



    
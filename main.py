# Заданное количество партий

# количество партий
N = 10 ** 5

import random

print('started...')

available_list = list(range(1, 10))  # список доступных ходов
win_list = ['123', '456', '789', '147', '258', '369', '159', '357']  # список выигрышных комбинаций

tableX = []  # таблица комбинаций X
tableO = []  # таблица комбинаций O
previous_tableX_length = len(tableX)
previous_tableO_length = len(tableO)
# tableX_procents = []
tableX_quantity = []

for k in range(N):
    # print('Party', (k+1))

    available_list = list(range(1, 10))
    current_status = 'start'  # текущий статус партии
    current_side = 'X'  # текущая сторона
    combination_code = 'C---------'  # код комбинации
    combination_code_history = []  # история комбинаций

    # цикл делания ходов
    while len(available_list):
        side_step = random.choice(available_list)
        # print(side_step)
        combination_code = combination_code[:side_step] + current_side + combination_code[side_step + 1:]
        # print(combination_code)
        combination_code_history.append(combination_code)

        for key in win_list:
            if combination_code[int(key[0])] == current_side and combination_code[int(key[1])] == current_side and \
                    combination_code[int(key[2])] == current_side:
                current_status = 'win' + current_side
                # print(key)
                break
        if current_status == 'winX' or current_status == 'winO': break

        available_list.remove(side_step)
        # print(available_list)
        current_side = 'O' if current_side == 'X' else 'X'

    if current_status != 'winX' and current_status != 'winO':
        current_status = 'draw'

    # фиксация в базу

    # для каждой комбинации в истории
    for index, value in enumerate(combination_code_history):

        #    print()

        # ищем комбинацию в крестиках
        if index % 2 == 0:
            # print(index,value)
            # перебираем таблицу tableX
            find_status = False
            # print('tableX',tableX, len(tableX))
            # print('value',value)
            for index2, value2 in enumerate(tableX):
                # print(value,value2[0])
                # если находим
                if value == value2[0]:
                    find_status = True
                    # print('нашли X', value)
                    previous_tableX_length = previous_tableX_length - 1
                    # print(index,value,tableX[int(index2)][1],tableX[int(index2)][2],tableX[int(index2)][3])
                    if current_status == 'winX': tableX[int(index2)][1] = tableX[int(index2)][1] + 1
                    if current_status == 'winO': tableX[int(index2)][2] = tableX[int(index2)][2] + 1
                    if current_status == 'draw': tableX[int(index2)][3] = tableX[int(index2)][3] + 1
                    # print(index,value,tableX[int(index2)][1],tableX[int(index2)][2],tableX[int(index2)][3])
                    # print(tableX)
                    break

            # если всю историю прошли и не нашли, то добавляем
            if not find_status:
                tableX.append([value, 0, 0, 0])
                # print('не нашли X')
                # print(index,value,current_status,tableX[int(index/2+previous_tableX_length)][1],tableX[int(index/2)+previous_tableX_length][2],tableX[int(index/2)+previous_tableX_length][3])
                if current_status == 'winX': tableX[int(index / 2) + previous_tableX_length][1] = \
                tableX[int(index / 2) + previous_tableX_length][1] + 1
                if current_status == 'winO': tableX[int(index / 2) + previous_tableX_length][2] = \
                tableX[int(index / 2) + previous_tableX_length][2] + 1
                if current_status == 'draw': tableX[int(index / 2 + previous_tableX_length)][3] = \
                tableX[int(index / 2) + previous_tableX_length][3] + 1
                # print(index,value,current_status,tableX[int(index/2)+previous_tableX_length][1],tableX[int(index/2)+previous_tableX_length][2],tableX[int(index/2)+previous_tableX_length][3])

        # то же самое в ноликах
        else:
            # print(index,value)
            # перебираем таблицу tableO
            find_status = False
            for index2, value2 in enumerate(tableO):
                # print(value,value2[0])
                # если находим
                if value == value2[0]:
                    find_status = True
                    # print('нашли O', value)
                    previous_tableO_length = previous_tableO_length - 1
                    # print(index,value,tableO[int(index2)][1],tableO[int(index2)][2],tableO[int(index2)][3])
                    if current_status == 'winO': tableO[int(index2)][1] = tableO[int(index2)][1] + 1
                    if current_status == 'winX': tableO[int(index2)][2] = tableO[int(index2)][2] + 1
                    if current_status == 'draw': tableO[int(index2)][3] = tableO[int(index2)][3] + 1
                    # print(index,value,tableO[int(index2)][1],tableO[int(index2)][2],tableO[int(index2)][3])
                    # print(tableO)
                    break
            # если всю историю прошли и не нашли, то добавляем
            if not find_status:
                tableO.append([value, 0, 0, 0])
                # print('не нашли O')
                # print(index,value,current_status,tableO[int(index/2+previous_tableO_length)][1],tableO[int(index/2+previous_tableO_length)][2],tableO[int(index/2)+previous_tableO_length][3])
                if current_status == 'winO': tableO[int(index / 2) + previous_tableO_length][1] = \
                tableO[int(index / 2) + previous_tableO_length][1] + 1
                if current_status == 'winX': tableO[int(index / 2) + previous_tableO_length][2] = \
                tableO[int(index / 2) + previous_tableO_length][2] + 1
                if current_status == 'draw': tableO[int(index / 2) + previous_tableO_length][3] = \
                tableO[int(index / 2) + previous_tableO_length][3] + 1
                # print(index,value,current_status,tableO[int(index/2)+previous_tableO_length][1],tableO[int(index/2+previous_tableO_length)][2],tableO[int(index/2)+previous_tableO_length][3])

    previous_tableX_length = len(tableX)
    previous_tableO_length = len(tableO)

    # tableX_procents.append(100*previous_tableX_length/(3**9))
    tableX_quantity.append(previous_tableX_length)

    if (k + 1) % 10 ** 4 == 0: print(k + 1)

tableO.insert(0, ['C---------', '-', '-', '-'])

with open("tableX.txt", "w") as output:
    output.write(str(tableX))

with open("table0.txt", "w") as output:
    output.write(str(tableO))

print('Party', (k + 1))
print()
print('tableX', len(tableX))
print('table0', len(tableO))

import os
import json
from ImportData import ImportData

IMPORTDATA = ImportData()

def load_data_ajax(CORE):
    CORE.debug('PATH: /import_data/load_data.py')

    IMPORTDATA.db = CORE.db

    dir = 'files/data'

    # Инициализация при первом подключении загрузки, обрабатываем названия регионов
    if not IMPORTDATA.dir_list:
        IMPORTDATA.initial()
        IMPORTDATA.clearData()
        path_list = os.listdir(dir)

        # Перебираем все папки
        dir_list = []
        for p in path_list:
            dir_path = dir + '/' + p
            if os.path.isdir(dir_path):
                dir_list.append(p)

        IMPORTDATA.dir_list = dir_list  # Не читаем в терминале русские буквы => utf-8
        IMPORTDATA.num_sum = len(dir_list)
        IMPORTDATA.num_current = 0

    # Текущий path обрабатываемого файла
    file_path = dir + '/' + IMPORTDATA.dir_list[IMPORTDATA.num_current] + '/DATTSVT.csv'
    if os.path.isfile(file_path):
        IMPORTDATA.setData(file_path)

    # Условие следующего хода
    IMPORTDATA.num_current += 1
    if IMPORTDATA.num_current > IMPORTDATA.num_sum:
        IMPORTDATA.initial()  # Сбрасываем настройки импорта, импорт окночен

    answer = {'answer': 'success', 'num_sum': IMPORTDATA.num_sum, 'num_current': IMPORTDATA.num_current}
    return {'ajax': json.dumps(answer)}
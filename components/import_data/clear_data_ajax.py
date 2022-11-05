import json
from ImportData import ImportData


def clear_data_ajax(CORE):
    CORE.debug('PATH: /clear_data_ajax/load_data.py')

    IMPORTDATA = ImportData()
    IMPORTDATA.db = CORE.db
    IMPORTDATA.clearData()  # Очищаем базу данных

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}
import json
# from Users import Users

def settings_save_ajax(CORE):
    CORE.debug('PATH: /import_data/settings_save.py')

    # ТУТ БУДЕТ РЕАЛИЗАЦИЯ КОДА ПОД КОНКРЕТНУЮ СИСТЕМУ 
    # БУДЕМ РАБОТАТЬ С "CRON"

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}
import json
# from Users import Users

def settings_save_ajax(CORE):
    CORE.debug('PATH: /import_data/settings_save.py')

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}
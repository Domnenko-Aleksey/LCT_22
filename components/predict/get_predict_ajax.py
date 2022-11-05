import json
# from ImportData import ImportData

# IMPORTDATA = ImportData()

def get_predict_ajax(CORE):
    CORE.debug('PATH: /predict/get_predict_ajax.py')
    
    print('============ POST: ', CORE.post)

    # IMPORTDATA = ImportData()
    # IMPORTDATA.db = CORE.db
    # IMPORTDATA.clearData()  # Очищаем базу данных

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}
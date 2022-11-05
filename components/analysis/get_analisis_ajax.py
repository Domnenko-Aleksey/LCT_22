import json
from Analisis import Analisis


def get_analisis_ajax(CORE):
    CORE.debug('PATH: /analisis/get_analisis_ajax.py')
    
    print('============ POST: ', CORE.post)


    GETDATA = GetData(CORE)
    GETDATA.getData = ''

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}
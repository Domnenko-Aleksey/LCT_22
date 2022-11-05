import random
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from GetData import GetData


def get_promising_ajax(CORE):
    CORE.debug('PATH: /predict/get_promising_ajax.py')
    
    print('============ POST: ', CORE.post)

    GETDATA = GetData(CORE)

    data = {
        'napr': 'ИМ',  # all / ИМ / ЭК
        'tnved': '',  # Не используем 
        'tnved_2': '',  # Не используем 
        'strana': '',  # Не используем
        'region': '12',  # CORE.post['region'],  # Строка id региона
        'period': {
            'start': '',  # Не используем
            'end': ''  # Не используем
        }
    }

    data_list = GETDATA.getData(data)

    if len(data_list) == 0:
        html = '<b>НЕТ ДАННЫХ</b>'
        answer = {'answer': 'success', 'content': html}
        return {'ajax': json.dumps(answer)} 

    print('ДЛИНА ДАННЫХ', len(data_list))

    df = pd.DataFrame(data_list)


    # --- HTML ---
    html =  '<h1>Перспективные направления</h1>'


    # --- HTML По объёму --- 
    title = 'По стоимости'
    description = 'Первые 100 операций по стоимости'
    df_sort = df.sort_values(by=['stoim'], ascending=False)
    df_sort.reset_index()
    html += get_html_table(title, description, df_sort)

    answer = {'answer': 'success', 'content': html}
    return {'ajax': json.dumps(answer)}






# Возвращает таблицу, заполненную данными в формате HTML
def get_html_table(title, description, df):
    html = f'<h3>{title}</h3>'
    html += f'<div>{description}</div>'  
    html += '<table class="admin_table dan_even_odd">'
    html +=     '<tr>'
    html +=         '<th style="width:50px">№</th>'
    html +=         '<th style="width:100px">Направление<br>перемещения</th>'
    html +=         '<th style="width:200px">Страна</th>'
    html +=         '<th style="width:200px">Федеральный округ</th>'
    html +=         '<th style="width:150px">Субъект РФ</th>'
    html +=         '<th style="width:100px">ТНВЭД</th>'
    html +=         '<th style="width:100px">Кол-во</th>'
    html +=         '<th style="width:100px">Вес</th>'
    html +=         '<th>Стоимость</th>'
    html +=     '</tr>'

    i = 0
    for idx, d in df.iterrows():
        html += '<tr>'
        html +=     f'<td>{i}</td>'
        html +=     f'<td>импорт</td>'
        html +=     f'<td>{d["nastranapr"]}</td>'
        html +=     f'<td>{d["region_s"]}</td>'
        html +=     f'<td>{d["region_id"]}</td>'
        html +=     f'<td>{d["tnved"]}</td>'
        html +=     f'<td>{d["kol"]}</td>'
        html +=     f'<td>{d["netto"]}</td>'
        html +=     f'<td>{d["stoim"]}</td>'
        html += '</tr>'

        if i > 100:
            html += '</table>'
            break

        i += 1

    return html
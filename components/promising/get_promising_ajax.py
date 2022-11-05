from datetime import datetime
import random
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from GetData import GetData
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.linear_model import LinearRegression


def get_promising_ajax(CORE):
    CORE.debug('PATH: /predict/get_promising_ajax.py')
    
    print('============ POST: ', CORE.post)

    GETDATA = GetData(CORE)

    data = {
        'napr': 'ИМ',  # all / ИМ / ЭК
        'tnved': '',  # Не используем 
        'tnved_2': '',  # Не используем 
        'strana': '',  # Не используем
        'region': CORE.post['region'],  # CORE.post['region'],  # Строка id региона
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

    # ======= ДИАПАЗОН ДАТ ======= 
    # Формируем диапазон дат для заполнения пропусков
    period_start_list = str(df['period'].min()).split('-')
    period_end_list = str(df['period'].max()).split('-')
    d_start = datetime(int(period_start_list[0]), int(period_start_list[1]), 1)
    d_end = datetime(int(period_end_list[0]), int(period_end_list[1]), 1)
    d_delta = (d_end.year - d_start.year) * 12 + d_end.month - d_start.month + 1

    d_list = []  # В формате строки
    dt_list = []  # В формате datetime
    for m in range(d_delta):
        dt = datetime(d_start.year, d_start.month + m, 1)
        dt_str = dt.strftime('%Y-%m-%d')
        dt_list.append(dt)
        d_list.append(dt_str)
    # df_date = pd.DataFrame(d_list, columns=['period'])




    # ======= ФОРМИРУЕМ ЗАПОЛНЕННЫЕ ДАННЫЕ =======
    # --- Группируем данные по ключам "tnved", "period" и сумме в значении ---
    for i in range(df.shape[0]):
        dt_str = df.loc[i, 'period'].strftime('%Y-%m-%d')
        df.loc[i, 'period'] = dt_str

    grouped = df.groupby(["tnved", "period"])[['stoim']].sum()

    # --- Получаем уникальные значения TNVED -> tnved_set ---
    tnved_list = []
    for i in range(grouped.index.shape[0]):
        tnved_list.append(grouped.index[i][0])
    tnved_set = set(tnved_list)
    tnved_set

    # --- Перебираем tnved_set, формируем словарь с регрессией, извлекаем признаки ---
    i = 0
    data_dict = {}
    data_dict_plus = {}
    supernova_list = []
    for t in tnved_set:
        t_item = grouped['stoim'][t]

        # Перебираем даты и пытаемся найти ключи
        sum_list = []
        for d in d_list:
            if d in t_item:
                sum_list.append(grouped['stoim'][t, d])
            else:
                sum_list.append(0)

        coef = round(lin_reg(sum_list)*100, 2)

        data_dict[t] = coef
        if coef > 0:
            # Только те отрасли, которые показали рост
            data_dict_plus[t] = coef

        supernova = get_supernovae(sum_list)
        if supernova:
            supernova_list.append([t, supernova])
        
        i += 1
        if i > 10:
            break


    # --- HTML ---
    html =  '<h1>Перспективные направления</h1>'


    # --- HTML По стоимости --- 
    df_stoim = df.groupby(df['tnved'])[['stoim']].sum()
    df_stoim = df_stoim.copy()
    df_stoim = df_stoim.sort_values(by=['stoim'], ascending=False)

    html += f'<h3>По объёму денежных средств (звёзды первой величины)</h3>'
    html += '<table class="admin_table dan_even_odd">'
    html +=     '<tr>'
    html +=         '<th style="width:50px">№</th>'
    html +=         '<th style="width:200px">ТНВЭД</th>'
    html +=         '<th>Сумма</th>'
    html +=     '</tr>'

    i = 1
    for idx, row in df_stoim.iterrows():
        html += '<tr>'
        html +=     f'<td>{i}</td>'
        html +=     f'<td>{idx}</td>'
        html +=     f'<td>{row["stoim"]}</td>'
        html += '</tr>'

        i += 1
        if i > 100:
            break

    html += '</table>'
    html += '<div style="height:50px;">&nbsp;</div>'


    # --- HTML По месячному тренду роста ---
    html += f'<h3>Растущие тренды (восходящие звёзды)</h3>'
    html += '<div>Расчёт % месячного роста, методом линейной регрессии</div>'
    html += '<table class="admin_table dan_even_odd">'
    html +=     '<tr>'
    html +=         '<th style="width:50px">№</th>'
    html +=         '<th style="width:200px">ТНВЭД</th>'
    html +=         '<th>% роста / мес.</th>'
    html +=     '</tr>'

    sorted_keys = sorted(data_dict_plus, key=data_dict_plus.get, reverse=True)
    i = 0
    for k in sorted_keys:
        html += '<tr>'
        html +=     f'<td>{i}</td>'
        html +=     f'<td>{k}</td>'
        html +=     f'<td>{data_dict_plus[k]} %</td>'
        html += '</tr>'

        i += 1
        if i > 100:
            break

    html += '</table>'
    html += '<div style="height:50px;">&nbsp;</div>'

    # --- Сверхновые ---
    html += f'<h3>Сверхновые</h3>'
    if len(supernova_list) == 0:
        html += '<div>Сверхновых нет</div>'
    else:       
        html += '<table class="admin_table dan_even_odd">'
        html +=     '<tr>'
        html +=         '<th style="width:50px">№</th>'
        html +=         '<th style="width:200px">ТНВЭД</th>'
        html +=         '<th>Сумма</th>'
        html +=     '</tr>'

        i = 1
        for row in supernova_list:
            html += '<tr>'
            html +=     f'<td>{i}</td>'
            html +=     f'<td>{row[0]}</td>'
            html +=     f'<td>{row[1]}</td>'
            html += '</tr>'

            i += 1
            if i > 100:
                break
    html += '</table>'


    answer = {'answer': 'success', 'content': html}
    return {'ajax': json.dumps(answer)}









# Линейная регрессия
def lin_reg(lst):
    # Нормализуем данные
    d = np.array(lst).reshape(-1, 1)
    data = normalize(d)
    x = np.arange(len(lst)).reshape(-1, 1)

    reg = LinearRegression().fit(x, data)
    coef = reg.coef_[0][0]
    return coef



# Сверхновые
def get_supernovae(lst):
  a = np.array(lst)

  if a[:-3].sum() == 0 and a[-3:].sum() > 0:
    return a[-3:].sum()
  else:
    return False
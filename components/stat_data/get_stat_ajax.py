from datetime import datetime
import random
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from GetData import GetData


def get_stat_ajax(CORE):
    CORE.debug('PATH: /stat_data/get_stat_ajax.py')
    
    print('============ POST: ', CORE.post)

    GETDATA = GetData(CORE)

    data = {
        'napr': CORE.post['napr'],  # all / ИМ / ЭК
        'tnved': '',  # Не используем # '3808932300,3301299100', Строка с перечислением tnved, через запятую, без пробелов
        'tnved_2': CORE.post['tnved_2'],  # Строка с перечислением tnved_2 (сокращённый вариант), через запятую, без пробелов
        'strana': CORE.post['strana'],  # Строка стран, через запятую, без пробелов
        'region': CORE.post['region'],  # Строка id регионов, через запятую, без пробелов
        'period': {
            'start': CORE.post['period_start'] + '-01', 
            'end':  CORE.post['period_end'] + '-01'
        }
    }

    print('DATA', data)

    GETDATA.getRegions()  # Получаем словарь сокращений регионов
    data_list = GETDATA.getData(data)  # Рлдучаем данные

    if len(data_list) == 0:
        html = '<b>НЕТ ДАННЫХ</b>'
        answer = {'answer': 'success', 'content': html}
        return {'ajax': json.dumps(answer)}       


    # --- Создаём датафрейм диапазона дат --- 
    period_start_list = CORE.post['period_start'].split('-')
    period_end_list = CORE.post['period_end'].split('-')
    d_start = datetime(int(period_start_list[0]), int(period_start_list[1]), 1)
    d_end = datetime(int(period_end_list[0]), int(period_end_list[1]), 1)
    d_delta = (d_end.year - d_start.year) * 12 + d_end.month - d_start.month + 1

    d_list = []
    for m in range(d_delta):
        dt = datetime(d_start.year, d_start.month + m, 1)
        dt_str = dt.strftime('%Y-%m-%d')
        d_list.append([dt_str])

    df_date = pd.DataFrame(d_list, columns=['period'])


    # --- Создаём датафрейм данных ---
    df = pd.DataFrame(data_list)
    df_export = df[df['napr'] == 'ЭК']
    df_import = df[df['napr'] == 'ИМ']

    rnd = random.randrange(1, 1000000)  # Случайное число в url картинки


    # --- КРУГОВАЯ ДИАГРАММА - ИМПОРТ, ЭКСПОРТ ---
    pie_html = ''
    if CORE.post['napr'] == 'ИМЭК':
        export_sum = df_export['stoim'].sum()
        import_sum = df_import['stoim'].sum()

        sum = import_sum + export_sum
        export_frac = round(export_sum/sum, 2)
        import_frac = round(import_sum/sum, 2)
        fracs = [import_frac, export_frac]
        labels = ['Экспорт', 'Импорт']

        plt.figure(figsize=(7, 7))
        plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True, explode=(0, 0.1), 
            textprops = {"fontsize":16}, colors=[CORE.color_1, CORE.color_2])
        plt.title('Экспорт / Импорт')
        plt.show()
        plt.savefig('files/stat/export_import_pie.png')
        plt.close()

        pie_html =    '<div class="graph_block">'
        pie_html +=       f'<image src="files/stat/export_import_pie.png?{rnd}">' 
        pie_html +=   '</div>'        



    # --- МЕСЯЧНАЯ ДИАГРАММА - ЭКСПОРТ И ИМПОРТ ---
    df_export_sum = df_export.groupby(df['period'])[['stoim']].sum()
    df_export_sum = prepare_data(df_export_sum, df_date)

    df_import_sum = df_import.groupby(df['period'])[['stoim']].sum()
    df_import_sum = prepare_data(df_import_sum, df_date)

    df_export_import_sum = df.groupby(df['period'])[['stoim']].sum()
    df_export_import_sum = prepare_data(df_export_import_sum, df_date)



    m_list = []
    for m in d_list:
        m_list.append(m[0][0:7])

    if CORE.post['napr'] == 'ИМЭК':
        label = 'Экспорт / импорт по месяцам'


    if CORE.post['napr'] == 'ЭК':
        label = 'Экспорт по месяцам'
    
    if CORE.post['napr'] == 'ИМ':
        label = 'Импорт по месяцам'

    x = np.arange(len(m_list))
    width = 0.4  # the width of the bars
    plt.figure(figsize=(10, 7))
    plt.title(label = label, fontsize=20)
    plt.xlabel('Месяца', fontsize=16)
    plt.ylabel('Оборот', fontsize=16)

    if CORE.post['napr'] == 'ИМЭК' or CORE.post['napr'] == 'ЭК':
        plt.bar(x-0.4, df_export_sum['stoim'], width, label='Экспорт', color=CORE.color_1)
    if CORE.post['napr'] == 'ИМЭК' or  CORE.post['napr'] == 'ИМ':
        plt.bar(x, df_import_sum['stoim'], width, label='Импорт', color=CORE.color_2)
    plt.xticks(x, m_list, fontsize=10)
    plt.yticks(fontsize=16)
    plt.legend(loc='upper left', fontsize=16)
    plt.show()
    plt.savefig('files/stat/export_import_bar.png')
    plt.close()

    bar_html =    '<div class="graph_block">'
    bar_html +=       f'<image src="files/stat/export_import_bar.png?{rnd}">' 
    bar_html +=   '</div>'



    # --- ГИСТОГРАМА ---
    # Экспорт
    hist_export_html = ''
    if CORE.post['napr'] == 'ИМЭК' or CORE.post['napr'] == 'ЭК':
        plt.figure(figsize=(10, 7))
        plt.title(label = 'ЭКСПОРТ, распределение по стоимости, логарифм.', fontsize=20)
        plt.hist(df_export['stoim'], bins=20, facecolor=CORE.color_1)
        plt.ylabel('Количество')
        plt.xlabel('Стоимость')
        plt.yscale('log')
        plt.show()
        plt.savefig('files/stat/export_hist.png')
        plt.close()

        hist_export_html =    '<div class="graph_block">'
        hist_export_html +=       f'<image src="files/stat/export_hist.png?{rnd}">' 
        hist_export_html +=   '</div>'

    # Импорт
    hist_import_html = ''
    if CORE.post['napr'] == 'ИМЭК' or CORE.post['napr'] == 'ИМ':
        plt.figure(figsize=(10, 7))
        plt.title(label = 'ИМПОРТ, распределение по стоимости, логарифм.', fontsize=20)
        plt.hist(df_import['stoim'], bins=20, facecolor=CORE.color_1)
        plt.ylabel('Количество')
        plt.xlabel('Стоимость')
        plt.yscale('log')
        plt.show()
        plt.savefig('files/stat/import_hist.png')
        plt.close()

        hist_import_html =    '<div class="graph_block">'
        hist_import_html +=       f'<image src="files/stat/import_hist.png?{rnd}">' 
        hist_import_html +=   '</div>'



    # --- HTML ---
    title = 'Экспорт / импорт'
    if CORE.post['napr'] == 'ЭК':
        title = 'Экспорт'
    if CORE.post['napr'] == 'ИМ':
        title = 'Импорт'

    countries = CORE.post['strana'].replace(',', ', ')

    html =  '<h1>' + title + '</h1>'
    html += '<div class="description">Страны: <b>' + countries + '</b></div>'
    html += '<div class="description">Регионы: <b>' + CORE.post['region'] + '</b></div>'
    html += '<div class="description">ТНВЕД: <b>' + CORE.post['tnved_2_name'] + '</b></div>'
    html += '<div class="description">Период от: <b>' + CORE.post['period_start'] + '</b> до: <b>' + CORE.post['period_end'] + '</b></div>'
    html += '<div class="dan_flex_row">'
    html += pie_html + bar_html + hist_export_html + hist_import_html
    html += '</div>'
    html += '<h3>Операции с максимальной стоимости</h3>'  
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

    # df_sort = df.sort_values(by='stoim', ascending=False)

    i = 1
    for idx, d in df.sort_values(by=['stoim'], ascending=False).iterrows():
        napr = 'импорт' if d['napr'] == 'ИМ' else 'экспорт'
        html += '<tr>'
        html +=     f'<td>{i}</td>'
        html +=     f'<td>{napr}</td>'
        html +=     f'<td>{d["nastranapr"]}</td>'
        html +=     f'<td>{d["region_s"]}</td>'
        html +=     f'<td>{d["region_id"]}</td>'
        html +=     f'<td>{d["tnved"]}</td>'
        html +=     f'<td>{d["kol"]}</td>'
        html +=     f'<td>{d["netto"]}</td>'
        html +=     f'<td>{d["stoim"]}</td>'
        html += '</tr>'

        if i >= 100:
            html += '</table>'
            break

        i += 1

    answer = {'answer': 'success', 'content': html}
    return {'ajax': json.dumps(answer)}



# Форматируем данные для вывода баров
def prepare_data(df, df_date):
    # Дата в индексе, да ещё в формате datatime, поэтому такой трюк
    data_list = []
    for idx in df.index:
        data_list.append([str(idx), float(df.loc[idx, 'stoim'])])
    df = pd.DataFrame(data_list, columns=['period', 'stoim'])
    df_res = pd.merge(df_date, df, on='period', how='left')
    df_res = df_res.fillna(0)
    return df_res.fillna(0)
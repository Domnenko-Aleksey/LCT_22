'''
Описание формата передаваемых данных

data = {
    'napr': all,  # all / ИМ / ЭК
    'tnved': '3808932300,3301299100'  # Строка с перечислением tnved, через запятую, без пробелов
    'strana': 'AB,DE,GA'  # Строка стран, через запятую, без пробелов
    'region': '12,20,1'  # Строка id регионов, через запятую, без пробелов
    'period': {
        'start': '2022-02-01',  # Первая дата - 01 число, т.к. день не учитывается
        'end': '2022-03-02'
    }
}
'''

class GetData:
    def __init__(self, CORE):
        self.db = CORE.db


    # Реализует функцию фильтрации данных по условиям
    def getData(self, data):
        # Направление
        sql_napr = ''
        if data['napr'] == 'ИМ' or data['napr'] == 'ЭК':
            sql_napr = f'''AND napr = '{data["napr"]}' '''

        # tnved
        sql_tnved = ''
        if len(data['tnved']) > 0:
            sql_tnved = f"AND tnved IN ({data['tnved']})"

        # tnved_2
        sql_tnved_2 = ''
        if len(data['tnved_2']) > 0:
            sql_tnved_2 = f"AND tnved_2 IN ({data['tnved_2']})"

        # Страна
        sql_strana = ''
        if len(data['strana']) > 0:
            strana_list = data['strana'].split(',')
            sql_strana += 'AND ('
            for i in range(len(strana_list)):
                if i == 0:
                    sql_strana += f"nastranapr = '{strana_list[i]}' "
                else:
                    sql_strana += f"OR nastranapr = '{strana_list[i]}' "
            sql_strana += ')'

        # Регион
        sql_region = ''
        if len(data['region']) > 0:
            sql_region = f"AND region_id IN ({data['region']}) "
    
        # Регион
        sql_period = ''
        if data['period']['start'] != '':
            sql_period += "AND period >= '" + data['period']['start'] + "' "
        if data['period']['end'] != '':
            sql_period += f"AND period <= '" + data['period']['end'] + "' "

        sql = f"SELECT * FROM data WHERE 1 {sql_napr} {sql_tnved} {sql_tnved_2} {sql_strana} {sql_region} {sql_period}"
        print('####################################################################')
        print(sql)

        self.db.execute(sql)
        return self.db.fetchall()



    # Получаем словарь {'ид региона': 'название региона'}
    def getRegions(self):
        sql = 'SELECT id, name FROM regions'
        self.db.execute(sql)

        sql_list = self.db.fetchall()
        result_dict = {}
        result_list = []
        for row in sql_list:
            result_dict[row['id']] = row['name']
            result_list.append([row['id'], row['name']])

        self.regions_dict = result_dict
        return result_list

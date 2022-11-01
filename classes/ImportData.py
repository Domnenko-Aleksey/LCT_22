import pandas as pd
import re

class ImportData:
    def __init__(self):
        self.dir_list = False
        self.initial()


    # Сбрасывает настройки при первом запуске
    def initial(self):
        self.dir_list = False  # False -> признак того, что не было прохода по данным
        self.num_sum = 0
        self.num_current = 0
        self.region_list = {}


    # Очищаем записи в базе данных
    def clearData(self):
        sql = 'DELETE FROM regions WHERE id > 0'
        self.db.execute(sql)

        sql = 'ALTER TABLE regions AUTO_INCREMENT = 1'
        self.db.execute(sql)

        sql = 'DELETE FROM data WHERE id > 0'
        self.db.execute(sql)

        sql = 'ALTER TABLE data AUTO_INCREMENT = 1'
        self.db.execute(sql)


    # Получаем все регионы из базы данныз
    def getRegions(self):
        sql = 'SELECT * FROM regions'
        self.db.execute(sql)
        arr = self.db.fetchall()
        for row in arr:
            self.region_list[row['name']] = True
        return arr


    # Проверяет, есть ли регион в БД и вносит запись в БД при отстутствии
    def setData(self, path):
        df = pd.read_csv(path, delimiter='	')
        pattern = re.compile('\d*\s\-\s')
        for i in range(df.shape[0]):
            row = df.iloc[i]
            region = pattern.sub('', row['Region'])
            # Проверяем - есть ли регион в базе данных? если нет - вносим
            if not region in self.region_list:
                self.insertRegion(region)
                self.region_list[region] = True 
            self.insertData(row)

    
    # Добавляет регион
    def insertRegion(self, name):
        sql = 'INSERT INTO regions SET name = %s, num = 0, date_last = NOW()'
        self.db.execute(sql, (name))


    # Получаем id региона по наименованию
    def getRegionIdByRegion(self, region):
        sql = 'SELECT id FROM regions WHERE name = %s LIMIT 1'
        self.db.execute(sql, (region))
        return self.db.fetchone()['id']


    # Добавляет данные в таблицу данных
    def insertData(self, df_row):
        pattern = re.compile('\d*\s\-\s')
        region = pattern.sub('', df_row['Region'])  # Получаем название региона
        region_id = self.getRegionIdByRegion(region)

        period_list = df_row['period'].strip().split('/')
        period = f'{period_list[1]}-{period_list[0]}-01'

        sql = '''
            INSERT INTO data SET 
            napr = %s, 
            period = %s, 
            nastranapr = %s, 
            tnved = %s, 
            edizm = %s, 
            stoim = %s, 
            netto = %s, 
            kol = %s, 
            region_id = %s, 
            region_s = %s
        '''

        self.db.execute(sql, (
            str(df_row['napr']).strip(),
            period,
            str(df_row['nastranapr']).strip(),
            str(df_row['tnved']).strip(),
            str(df_row['edizm']).strip(),
            str(df_row['Stoim']).strip(),
            str(df_row['Netto']).strip(),
            str(df_row['Kol']).strip(),
            region_id,
            str(df_row['Region_s']).strip()
        ))
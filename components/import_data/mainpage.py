def mainpage(CORE):
    CORE.debug('PATH: /import_data/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/import_data/css/mainpage.css')
    CORE.addHeadFile('/templates/general/js/DAN.js')
    CORE.addHeadFile('/templates/import_data/js/mainpage.js')

    tr_html = ''   




    CORE.content = f'''
        <div class="dan_flex_row_start">
            <div class="import_data_info">Дата последней загрузки:<span id="import_data_date">11111</span></div>
            <div id="import_data_settings_button">Настройки автоматической загрузки</div>
            <div id="import_data_manual_button">Ручная загрузка</div>
            <div id="clear_data_button">Очистить базу</div>
        </div>
        <h1>Данные</h1>
        <table class="admin_table dan_even_odd">
            <tr>
                <th style="width:50px">№</th>
                <th style="width:50px"></th>
                <th>Имя.</th>
                <th style="width:150px">Телефон</th>
                <th style="width:150px">Последний визит</th>
                <th style="width:150px">Регистрация</th>
                <th style="width:100px">Статус</th>
            </tr>
            {tr_html}
        </table>
    '''
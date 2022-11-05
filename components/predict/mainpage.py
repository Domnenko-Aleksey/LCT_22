# from Users import Users

def mainpage(CORE):
    CORE.debug('PATH: /predict/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/general/js/DAN.js')
    CORE.addHeadFile('/templates/contextmenu/css/contextmenu.css')
    CORE.addHeadFile('/templates/contextmenu/js/contextmenu.js')
    CORE.addHeadFile('/templates/predict/css/mainpage.css')
    CORE.addHeadFile('/templates/predict/js/mainpage.js')

    # USER = Users(CORE)
    # users = USER.getUsersList()


    CORE.content = f'''
        <h1>Предсказание</h1>
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
        </table>
    '''
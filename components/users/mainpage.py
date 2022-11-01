from Users import Users

def mainpage(CORE):
    CORE.debug('PATH: /users/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/general/js/DAN.js')
    CORE.addHeadFile('/templates/contextmenu/css/contextmenu.css')
    CORE.addHeadFile('/templates/contextmenu/js/contextmenu.js')
    CORE.addHeadFile('/templates/users/css/list.css')
    CORE.addHeadFile('/templates/users/js/users_list.js')

    USER = Users(CORE)
    users = USER.getUsersList()

    tr_html = ''   
    for u in users:
        tr_class = 'class="unpub"' if u['status'] == 0 else ''
        tr_html += f'''
         <tr {tr_class}>
            <td style="width:50px">{u['id']}</td>
            <td style="width:50px">
                <svg class="dan_contextmenu_ico contextmenu_menu" title="Действия" data-id="{u['id']}">
                    <use xlink:href="/templates/general/images/sprite.svg#menu"></use>
                </svg>
            </td>
            <td><a target="blank" href="/users/view/{u['id']}">{u['name']} {u['surname']}</a></td>
            <td style="width:150px">{u['phone']}</td>
            <td style="width:150px">{u['date_reg']}</td>
            <td style="width:150px">{u['date_last']}</td>
            <td style="width:100px">{u['status']}</td>
        </tr>
        '''



    CORE.content = f'''
        <div class="flex_row_start">
            <a href="/users/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/general/images/sprite.svg#add"></use></svg>
                <div class="ico_rectangle_text">Добавить пользователя</div>
            </a>
        </div>
        <h1>Пользователи</h1>
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
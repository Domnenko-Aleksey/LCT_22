from Users import Users

def view(CORE):
    CORE.debug('PATH: /users/view.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/users/css/view.css')
    
    id = CORE.p[2]
    USER = Users(CORE)
    user = USER.getUser(id)

    status = 'активен' if user['status'] == 1 else 'не активен'

    CORE.content = f'''
        <h1>{user['name']} {user['surname']}</h1>
        <div class="users_view_container">
            <div class="users_view_row dan_flex_row">
                <div class="tc_l">Email:</div>
                <div class="tc_r dan_flex_grow">{user['email']}</div>
            </div>
            <div class="users_view_row dan_flex_row">
                <div class="tc_l">Телефон:</div>
                <div class="tc_r dan_flex_grow">{user['phone']}</div>
            </div>
            <div class="users_view_row dan_flex_row">
                <div class="tc_l">Дополнительно:</div>
                <div class="tc_r dan_flex_grow">{user['text']}</div>
            </div>
            <div class="users_view_row dan_flex_row">
                <div class="tc_l">Статус:</div>
                <div class="tc_r dan_flex_grow">{status}</div>
            </div>
        </div>
    '''
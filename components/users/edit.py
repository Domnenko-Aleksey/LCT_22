from Users import Users

def edit(CORE):
    CORE.debug('PATH: /users/edit.py')

    CORE.addHeadFile('/templates/css/DAN.css')
    CORE.addHeadFile('/templates/js/DAN.js')
    CORE.addHeadFile('/templates/css/edit.css')

    if CORE.p[1] == 'add':
        title = 'Добавить'
        act = 'insert'
        user = {
            'name': '',
            'surname': '',
            'email': '',
            'phone': '',
            'image': '',
            'text': ''
        }
        status_checked = ''
        password_html = '''
        <div class="dan_flex_row">
            <div class="tc_l">Пароль</div>
            <div class="tc_r dan_flex_grow">
                <input class="dan_input w_400" type="password" name="psw" required="" minlength="8" maxlength="20" pattern="[0-9a-zA-Z]{8,20}"
       title="8 - 20 английских букв и цифр" value="">
            </div>
        </div>
        '''
    else:
        title = 'Редактировать'
        id = CORE.p[2]
        act = 'update/' + id
        USER = Users(CORE)
        user = USER.getUser(id)
        status_checked = 'checked=""' if user['status'] == 1 else '';
        password_html = ''

    tr_html = ''
    CORE.content = f'''
        <h1>{title} пользователя</h1>
        <form method="post" action="/users/{act}" enctype="multipart/form-data">
        <div class="dan_flex_row">
            <div class="tc_l">Имя</div>
            <div class="tc_r dan_flex_grow">
                <input class="dan_input w_400" name="name" type="text" placeholder="Имя" required="" value="{user['name']}">
            </div>
        </div>
        <div class="dan_flex_row">
            <div class="tc_l">Фамилия</div>
            <div class="tc_r dan_flex_grow">
                <input class="dan_input w_400" name="surname" type="text" placeholder="Фамилия" required="" value="{user['surname']}">
            </div>
        </div>
        <div class="dan_flex_row">
            <div class="tc_l">Email</div>
            <div class="tc_r dan_flex_grow">
                <input class="dan_input w_400" name="email" required="" value="{user['email']}">
            </div>
        </div>
        {password_html}
        <div class="dan_flex_row">
            <div class="tc_l">Телефон</div>
            <div class="tc_r dan_flex_grow">
                <input class="dan_input w_400" name="phone" value="{user['phone']}">
            </div>
        </div>
        <div class="dan_flex_row">
            <div class="tc_l">Дополнительно</div>
            <div class="tc_r dan_flex_grow">
                <textarea class="dan_input w_400" rows="5" name="text">{user['text']}</textarea>
            </div>
        </div>
        <div class="dan_flex_row">
            <div class="tc_l">Активен</div>
            <div class="tc_r dan_flex_grow">
                <input id="mp_user_status" class="dan_input" name="status" type="checkbox" value="1" {status_checked}>
                <label for="mp_user_status"></label>
            </div>
        </div>
        <div class="dan_flex_row m_40_0">
            <div class="tc_l">
                <input class="dan_button_green" type="submit" name="submit" value="Сохранить">
            </div>
            <div class="tc_r">
                <a href="/users" class="dan_button_white">Отменить</a>
            </div>
        </div>
        </form>
    '''
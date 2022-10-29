import hashlib
from Users import Users

def insert(CORE):
    CORE.debug('PATH: /users/insert.py')
    psw = (CORE.post['psw'] + CORE.config.salt).encode()  # В байты
    # psw = bytes(psw, encoding = 'utf-8')
    data = {
        'name': CORE.post['name'],
        'surname': CORE.post['surname'],
        'email': CORE.post['email'],
        'psw': hashlib.sha256(psw).hexdigest(),
        'phone': CORE.post['phone'],
        'text': CORE.post['text'],
        'ordering': CORE.post['text'],
        'status': 1 if 'status' in CORE.post else 0
    }
    
    if data['name'] == '' or data['email'] == '':
        CORE.content = '<h1>Ошибка - не заполнено поле</h1>'
    else:
        USER = Users(CORE)
        u = USER.getUserByEmail(data['email'])
        
        # Проверка того, что пользователь уже зарегистрирован.
        if u:
            CORE.content = '<h1>Пользователь уже зарегистрирован</h1>'
        else:
            USER.insert(data)
            return {'redirect': '/users'}

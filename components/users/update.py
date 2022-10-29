from Users import Users

def update(SITE):
    SITE.debug('PATH: /users/update.py')
    data = {
        'name': SITE.post['name'],
        'surname': SITE.post['surname'],
        'email': SITE.post['email'],
        'phone': SITE.post['phone'],
        'text': SITE.post['text'],
        'ordering': SITE.post['text'],
        'status': 1 if 'status' in SITE.post else 0,
        'id': SITE.p[2]
    }
    
    if data['name'] == '' or data['email'] == '':
        SITE.content = '<h1>Ошибка - не заполнено поле</h1>'
    else:
        USER = Users(SITE)
        USER.update(data)
        return {'redirect': '/users'}

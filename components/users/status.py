from Users import Users

def status(CORE):
    CORE.debug('PATH: /users/status.py')
    status = 1 if CORE.p[1] == 'pub' else 0
    id = CORE.p[2]
    USER = Users(CORE)
    USER.setStatus(id, status)
    return {'redirect': '/users'}

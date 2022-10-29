from Users import Users

def delete(CORE):
    CORE.debug('PATH: /users/delete.py')
    id = CORE.p[2]
    USER = Users(CORE)
    USER.delete(id)
    return {'redirect': '/users'}
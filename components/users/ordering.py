from Users import Users

def ordering(CORE):
    CORE.debug('PATH: /users/ordering.py')

    act = CORE.p[1]
    id = CORE.p[2]
    USER = Users(CORE)
    USER.setOrdering(id, act)
    return {'redirect': '/users'}
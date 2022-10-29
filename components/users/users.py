from aiohttp import web
from users import mainpage
from users import edit
from users import view
from users import insert
from users import update
from users import status
from users import ordering
from users import delete


def users(CORE):
    CORE.debug('PATH: /teplates/users/users.py (router)')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'add': edit.edit,
        'edit': edit.edit,
        'view': view.view,
        'insert': insert.insert,
        'update': update.update,
        'pub': status.status,
        'unpub': status.status,
        'up': ordering.ordering,
        'down': ordering.ordering,
        'delete': delete.delete
    }


    if (CORE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[CORE.p[1]](CORE)
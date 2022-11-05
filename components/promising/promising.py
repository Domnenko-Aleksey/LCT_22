from aiohttp import web
from promising import mainpage
from promising import get_promising_ajax


def promising(CORE):
    CORE.debug('PATH: /promising/promising.py (router)')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'get_promising_ajax': get_promising_ajax.get_promising_ajax
    }


    if (CORE.p[1] not in functions):
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[CORE.p[1]](CORE)
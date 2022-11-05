from aiohttp import web
from analisis import mainpage
from analisis import get_analisis_ajax


def analisis(CORE):
    CORE.debug('PATH: /analisis/analisis.py (router)')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'get_analisis_ajax': get_analisis_ajax.get_analisis_ajax
    }


    if (CORE.p[1] not in functions):
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[CORE.p[1]](CORE)
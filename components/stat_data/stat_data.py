from aiohttp import web
from stat_data import mainpage
from stat_data import get_stat_ajax


def stat_data(CORE):
    CORE.debug('PATH: /stat_data/stat_data.py (router)')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'get_stat_ajax': get_stat_ajax.get_stat_ajax
    }


    if (CORE.p[1] not in functions):
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[CORE.p[1]](CORE)
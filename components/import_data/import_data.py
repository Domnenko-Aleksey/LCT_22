from aiohttp import web
from import_data import mainpage
from import_data import settings_save_ajax
from import_data import load_data_ajax
from import_data import clear_data_ajax

def import_data(CORE):
    CORE.debug('PATH: /import_data/import_data.py (router)')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'settings_save_ajax': settings_save_ajax.settings_save_ajax,
        'load_data_ajax': load_data_ajax.load_data_ajax,
        'clear_data_ajax': clear_data_ajax.clear_data_ajax
    }

    if (CORE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[CORE.p[1]](CORE)
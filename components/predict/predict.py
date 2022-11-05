from aiohttp import web
from predict import mainpage
from predict import get_predict_ajax


def predict(CORE):
    CORE.debug('PATH: /predict/predict.py (router)')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'get_predict_ajax': get_predict_ajax.get_predict_ajax
    }


    if (CORE.p[1] not in functions):
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[CORE.p[1]](CORE)
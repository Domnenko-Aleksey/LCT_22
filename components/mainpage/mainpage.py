import json

def mainpage(CORE):
    CORE.debug('/components/mainpage/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/general/css/mainpage.css')

    CORE.content = f'''
        <h1>Дашбоард</h1>
        <div class="dan_flex_row_start">
            <div class="mp_panel">
                <div class="mp_panel_title">11111111111111</div>
            </div>
            <div class="mp_panel">
                <div class="mp_panel_title">22222222222222</div>
            </div>
        </div>
    '''

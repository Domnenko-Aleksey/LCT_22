import json
from GetData import GetData

def mainpage(CORE):
    CORE.debug('PATH: /promising/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/general/js/DAN.js')
    CORE.addHeadFile('/templates/contextmenu/css/contextmenu.css')
    CORE.addHeadFile('/templates/contextmenu/js/contextmenu.js')
    CORE.addHeadFile('/templates/promising/css/mainpage.css')
    CORE.addHeadFile('/templates/promising/js/mainpage.js')
    CORE.addHeadFile('/templates/general/js/pdf.js')

    GETDATA = GetData(CORE)
    regions = GETDATA.getRegions()

    region_options_html = ''
    for r in regions:
        region_options_html += f'''<option value="{r[0]}">{r[1]}</option>'''

    CORE.content = f'''
        <h1>Перспективные отрасли</h1>
        <h3>Выберите регион</h3>					
            <select id="select_region" class="select" name="region[]" value="">
                {region_options_html}
            </select><br><br>                
        <div id="send_result_button" class="dan_button_red">Применить</div>
        <div id="answer_content"></div>
    '''
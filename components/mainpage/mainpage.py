import json

def mainpage(CORE):
    CORE.debug('/components/mainpage/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/general/css/mainpage.css')

    CORE.content = f'''
        <h1>Дашбоард</h1>
        <div class="dan_flex_row_start">
            <div class="mp_panel">
                <div class="mp_panel_title">Внимание!</div>
                <div>
                    <p>Объём данных, загруженных в основную таблицу базы данных составляет <b>4 913 026</b> строк.</p>
                    <p>Требуется более чем полчаса на обработку и загрузку данных в MySQL (MariaDB).</p>
                    <p>Стирание данных тоже требуют некотрого времени.</p>
                    <p>&nbsp;</p>
                    <p>Выборка, обработка данных как правило занимает несколько секунд.</p>
                </div>
            </div>
            <div class="mp_panel">
                <div class="mp_panel_title">Презентация, документация</div>
                <div>
                    <div>
                        <a id="a_presentation" target="_blank" href="/files/docs/presentation.pdf">
                            <svg class="pdf_svg"><use xlink:href="/templates/general/images/sprite.svg#pdf_1"></use></svg>
                            <span>Презентация</span>
                        </a>
                    </div>
                    <div>
                        <a id="a_documentation" target="_blank" href="/files/docs/documentation.pdf">
                            <svg class="pdf_svg"><use xlink:href="/templates/general/images/sprite.svg#pdf_2"></use></svg>
                            <span>Документация</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    '''

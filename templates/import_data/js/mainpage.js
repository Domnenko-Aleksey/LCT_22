window.addEventListener('DOMContentLoaded', function(){
	IMPORT_DATA.init()
});


IMPORT_DATA = {
    // Инициализация
    init() {
        DAN.$('import_data_settings_button').onclick = IMPORT_DATA.settings_modal
        DAN.$('import_data_manual_button').onclick = IMPORT_DATA.load_data_progress
        DAN.$('clear_data_button').onclick = IMPORT_DATA.clear_data_modal
    },


    // Выводит модальное окно настроек
    settings_modal() {
        content = 
        '<h1>Настройка автоматической загрузки</h1>' +
        '<div class="dan_modal_row">' +
            '<div class="modal_tc_l">Время загрузки</div>' +
            '<div class="modal_tc_r">' +
                '<input class="dan_input" type="time" name="time" type="text" placeholder="Имя" value="">' +
            '</div>' +
        '</div>' +
        '<div class="dan_modal_row">' + 
            '<div class="modal_tc_l">' + 
                '<input id="modal_submit" class="dan_button_green" type="submit" name="submit" value="Сохранить">' + 
            '</div>' + 
            '<div class="modal_tc_r">' + 
                '<input id="modal_cancel" class="dan_button_white" type="submit" name="cancel" value="Отменить">' + 
            '</div>' + 
        '</div>'

        DAN.modal.add(content, 500)
        DAN.$('modal_submit').onclick = IMPORT_DATA.settings_save
        DAN.$('modal_cancel').onclick = DAN.modal.del
    },


    // Сохранение настроек
    settings_save() {
		let form = new FormData()
		DAN.ajax('/import_data/settings_save_ajax', form, function(data) {
			console.log(data)
		})
        DAN.modal.del()
    },


    // Загрузка данных ajax
    load_data_progress() {
		let form = new FormData()
        console.log('PFUH')
        let content =
        '<h1 id="modal_h1" style="text-align:center;">Загрузка данных</h1>' +
        '<div style="text-align:center;margin:20px 0px">Для загрузки потребуется некоторое продолжительное время.</div>' +
        '<div class="items_progress_html">' +
            '<span id="items_progress_html">' + 
                'Обработано: <b id="items_progress_current"></b> из <b id="items_progress_count"></b>' +
            '</span>' +
        '</div>' +
        '<div><progress id="items_progress" max="" value=""></progress></div>' + 
        '<div id="items_message"></div>'
        DAN.modal.add(content, 400)
        IMPORT_DATA.load_data_ajax()    
    },


    // Загрузка данных ajax
    load_data_ajax() {
		let form = new FormData()
		DAN.ajax('/import_data/load_data_ajax', form, function(data) {
			console.log(data)
            DAN.$('items_progress_count').innerHTML = data.num_sum
            DAN.$('items_progress_current').innerHTML = data.num_current
            DAN.$('items_progress').setAttribute('max', data.num_sum)
            DAN.$('items_progress').value = data.num_current

            if (data.num_current < data.num_sum) {
                IMPORT_DATA.load_data_ajax()
            } else {
                DAN.$('modal_h1').innerHTML = 'Загрузка завершена'
            }   
		})        
    },


    // Очищает базу данных
    clear_data_modal() {
		let content =
			'<div style="text-align:center;font-size:20px">Очистить базу данных</div>' +
			'<div style="text-align:center;margin:20px 0px">' +
				'<input id="modal_checkbox" type="checkbox" name="check"> Подтверждаю удаление данных' +
			'</div>' +
			'<div style="text-align:center;margin:20px 0px">База содержит несколько миллионов записей. Для удаления потребуется некоторое продолжительное время</div>' +
			'<div class="dan_flex_row">' +
				'<div style="margin-right:5px">' +
					'<input id="modal_submit" class="dan_button_red" type="submit" name="submit" value="Очистить">' +
				'</div>' +
				'<div style="margin-left:5px">' +
					'<input id="modal_cancel" class="dan_button_white" type="submit" name="cancel" value="Отменить">' +
				'</div>' +
			'</div>'
		DAN.modal.add(content, 400)
		DAN.$('modal_cancel').onclick = DAN.modal.del
		DAN.$('modal_submit').onclick = () => {
			let check = DAN.$('modal_checkbox')
			if (!check.checked) {
				alert('Вы не подтвердили удаление пользователя - необходимо поставить галочку')
				return
			} else {
				IMPORT_DATA.clear_data_ajax()
			}
		}
    },


    // Очистка базы данных ajax
    clear_data_ajax() {
		let form = new FormData()
		DAN.ajax('/import_data/clear_data_ajax', form, function(data) {
            DAN.modal.add('БАЗА ДАННЫХ ОЧИЩЕНА')
		}) 
        DAN.modal.spinner()
    }
}
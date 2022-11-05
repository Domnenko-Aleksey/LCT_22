window.addEventListener('DOMContentLoaded', () => {
	PROM.init(); 
});

PROM = {
	init() {	
		DAN.$('send_result_button').onclick = PROM.send_data_ajax
	},		
		
	// Отправка данных на ajax
	send_data_ajax() {
		if (DAN.$('select_region').value != '') {
			let form = new FormData()
			form.append('region', DAN.$('select_region').value)
			
			DAN.ajax('/promising/get_promising_ajax', form, (data)=>{							
				DAN.$('answer_content').innerHTML = data.content
				DAN.modal.del()
				if(!(DAN.$('generate_pdf_wrap'))) {
					DAN.$('answer_content').insertAdjacentHTML('beforeBegin', '<div id="generate_pdf_wrap" class="dan_flex_row"><div id="generate_pdf" class="dan_button_red generate_pdf_button"><svg><use xlink:href="/templates/general/images/sprite.svg#download"></use></svg>Скачать PDF</div></div>')
				}
				DAN.jumpTo("generate_pdf_wrap", 1000, -100);
				DAN.$('generate_pdf').onclick = PROM.html_to_pdf
				
			})
			DAN.modal.spinner()
		} else {
			alert('Выберите регион');
		}
		
	},	
		
	
	html_to_pdf() {
		console.log('pdf')
		let element = document.getElementById('answer_content');	
		let now = new Date()
		
		// Generate the PDF.
		html2pdf().from(element).set({
		  margin: 0.25,
		  filename: 'Перспективные отрасли (' + now.getDate() + '.' + now.getMonth() + '.' + now.getFullYear() + '; ' + now.getHours() + '.' + now.getMinutes() + ').pdf',
		  html2canvas: { scale: 2 },
		  jsPDF: {orientation: 'portrait', unit: 'in', format: 'letter', compressPDF: true}
		}).save();
	}	
}	


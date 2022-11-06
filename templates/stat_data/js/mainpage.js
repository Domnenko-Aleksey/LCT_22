window.addEventListener('DOMContentLoaded', () => {
	STAT_DATA.init(); 
});

STAT_DATA = {
	init() {
		DAN.$('send_result_button').onclick = STAT_DATA.send_data_ajax	
		
		
		/* country init */
		let s_country = DAN.$('select_country');		
		let r_country = DAN.$('result_country');		
		let arr_country = new Array();
		arr_country = [];
		let arr_country_name = new Array();
		arr_country_name = [];
		str_country_name = '';
		
		/**/
				
		/* region init */
		let s_region = DAN.$('select_region');
		let r_region = DAN.$('result_region');
		let arr_region = new Array();
		arr_region = [];
		let arr_region_name = new Array();
		arr_region_name = [];
		str_region_name = '';
		/**/
		
		/* tnved init */
		let s_tnved = DAN.$('select_tnved');
		let r_tnved = DAN.$('result_tnved');
		let arr_tnved = new Array();
		arr_tnved = [];
		let arr_tnved_name = new Array();
		arr_tnved_name = [];
		str_tnved_name = '';
		/**/
		
		/* calc remove init */
		let btn_close = document.getElementsByClassName('result_close');		
		let s_options = document.querySelectorAll('.stat_select option');
		/**/

		
		
		/* Select function */
		
		for (let i = 0; i < s_country.length; i++) { 		
		
		s_country.onchange = () => {
		
			active_num = s_country.selectedIndex;

				r_country.innerHTML += '<div class="filter_result filter_result_country" data-id="'+ s_country[active_num].value +'" data-num="'+ active_num +'">' + s_country[active_num].textContent + '<div class="result_close">x</div></div>';	
				STAT_DATA.country_calc();
				f_select_active(s_country, active_num);
			}
		}
		
		for (let i = 0; i < s_region.length; i++) { 		
		
		s_region.onchange = () => {
		
			active_num = s_region.selectedIndex;

				r_region.innerHTML += '<div class="filter_result filter_result_region" data-id="'+ s_region[active_num].value +'" data-num="'+ active_num +'">' + s_region[active_num].textContent + '<div class="result_close">x</div></div>';	
				STAT_DATA.region_calc();				
				f_select_active(s_region, active_num);
			}
		}
		
		for (let i = 0; i < s_tnved.length; i++) { 		
		
		s_tnved.onchange = () => {
		
			active_num = s_tnved.selectedIndex;

				r_tnved.innerHTML += '<div class="filter_result filter_result_tnved" data-id="'+ s_tnved[active_num].value +'" data-num="'+ active_num +'">' + s_tnved[active_num].textContent + '<div class="result_close">x</div></div>';	
				STAT_DATA.tnved_calc();
				f_select_active(s_tnved, active_num);
			}
		}
		
		function f_select_active(a, b) {
			a[b].classList.add('select_active');								
			a[b].setAttribute('data-active', active_num);
			f_remove_button();
		}
		

		function f_remove_button() {
			for (let b = 0; b < btn_close.length; b++) {				
				btn_close[b].addEventListener("click", f_remove_calc);							
			}
		}
		
		f_remove_calc = (e) => {		
			e.target.parentNode.remove();
			document.querySelectorAll('.stat_select option[data-active="' + e.target.parentNode.getAttribute('data-num') + '"]')[0].classList.remove('select_active');			
			STAT_DATA.country_calc();	
			STAT_DATA.region_calc();	
			STAT_DATA.tnved_calc();	
			f_remove_button()
		}


		/**/
		
	},
	
	// Calc array
	country_calc() {
		let country = document.getElementsByClassName('filter_result_country');
		STAT_DATA.arr_country = [];			
		STAT_DATA.arr_country_name = [];			
		for (let i = 0; i < country.length; i++) { 
			STAT_DATA.arr_country.push(country[i].getAttribute('data-id'));	
			STAT_DATA.arr_country_name.push(country[i].childNodes[0].textContent);		
			STAT_DATA.str_country_name = STAT_DATA.arr_country_name.join(', ');
		}
	},
	
	region_calc() {
		let region = document.getElementsByClassName('filter_result_region');
		STAT_DATA.arr_region = [];			
		STAT_DATA.arr_region_name = [];			
		for (let i = 0; i < region.length; i++) { 
			STAT_DATA.arr_region.push(region[i].getAttribute('data-id'));
			STAT_DATA.arr_region_name.push(region[i].childNodes[0].textContent)
			STAT_DATA.str_region_name = STAT_DATA.arr_region_name.join(', ');
		}
	},
	
	tnved_calc() {
		let tnved = document.getElementsByClassName('filter_result_tnved');
		STAT_DATA.arr_tnved = [];			
		STAT_DATA.arr_tnved_name = [];			
		for (let i = 0; i < tnved.length; i++) { 
			STAT_DATA.arr_tnved.push(tnved[i].getAttribute('data-id'))
			STAT_DATA.arr_tnved_name.push(tnved[i].childNodes[0].textContent)
			STAT_DATA.str_tnved_name = STAT_DATA.arr_tnved_name.join('. ');
		}
	},
	
	
	
	
	// Send data ajax
	send_data_ajax() {
		if (DAN.$('select_country').value != '') {
			let form = new FormData()
			
			
			if (STAT_DATA.arr_region == undefined) {
				STAT_DATA.arr_region = ""
			}
			
			if (STAT_DATA.str_region_name == undefined) {
				STAT_DATA.str_region_name = ""
			}
			
			if (STAT_DATA.arr_tnved == undefined) {
				STAT_DATA.arr_tnved = ""
			}
			
			if (STAT_DATA.str_tnved_name == undefined) {
				STAT_DATA.str_tnved_name = ""
			}
		
			form.append('strana', STAT_DATA.arr_country)
			form.append('strana_name', STAT_DATA.str_country_name)
			form.append('region', STAT_DATA.arr_region)
			form.append('region_name', STAT_DATA.str_region_name)
			form.append('tnved_2', STAT_DATA.arr_tnved)
			form.append('tnved_2_name', STAT_DATA.str_tnved_name)
			form.append('napr', DAN.$('select_napr').value)
			form.append('period_start', DAN.$('start').value)
			form.append('period_end', DAN.$('end').value)
			DAN.ajax('/stat_data/get_stat_ajax', form, (data)=>{			
				DAN.$('answer_content').innerHTML = data.content
				DAN.modal.del()
				if(!(DAN.$('generate_pdf_wrap'))) {
					DAN.$('answer_content').insertAdjacentHTML('beforeBegin', '<div id="generate_pdf_wrap" class="dan_flex_row"><div id="generate_pdf" class="dan_button_red generate_pdf_button"><svg><use xlink:href="/templates/general/images/sprite.svg#download"></use></svg>Скачать PDF</div></div>')
				}
				DAN.jumpTo("generate_pdf_wrap", 1000, -100);
				DAN.$('generate_pdf').onclick = STAT_DATA.html_to_pdf
				
			})
			DAN.modal.spinner()
		} else {
			alert('Выберите страну');
		}
		
	},	
		
	
	html_to_pdf() {
		let element = document.getElementById('answer_content');	
		let now = new Date()
		
		// Generate the PDF.
		html2pdf().from(element).set({
		  margin: 0.25,
		  filename: 'Статистика (' + now.getDate() + '.' + now.getMonth() + '.' + now.getFullYear() + '; ' + now.getHours() + '.' + now.getMinutes() + ').pdf',
		  html2canvas: { scale: 2 },
		  jsPDF: {orientation: 'portrait', unit: 'in', format: 'letter', compressPDF: true}
		}).save();
	}	
	

}
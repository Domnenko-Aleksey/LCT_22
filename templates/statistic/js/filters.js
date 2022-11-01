window.addEventListener('DOMContentLoaded', () => {
	init(); 
	country();
});


init = () => {
	let i_import = DAN.$('input_import');
	let i_import_export = DAN.$('input_import_export');
	let i_export = DAN.$('input_export');
	let i_kg = DAN.$('input_kg');
	let i_t = DAN.$('input_t');
	let rh_travel_direction = DAN.$('result_hidden_travel_direction');
	
	
	i_import.onchange = () => {
		rh_travel_direction.value = i_import.value
	}

	i_import_export.onchange = () => {
		rh_travel_direction.value = i_import_export.value
	}

	i_export.onchange = () => {
		rh_travel_direction.value = i_export.value
	}
	
};


country = () => {
	
	let s_country = DAN.$('select_country');
	let rv_country = DAN.$('result_country');
	let rh_country = DAN.$('result_hidden_country');
	let btn_close = document.getElementsByClassName('result_close');

	let s_country_options = document.querySelectorAll('#select_country option');
	let arr_country = new Array();
	arr_country = [];
	
	for (let i = 0; i < s_country_options.length; i++) { 
		s_country_options[i].addEventListener("click", function () {
			rv_country.innerHTML += '<div class="filter_result" data-id="'+ s_country_options[i].value +'">' + s_country_options[i].textContent + '<div class="result_close">x</div></div>';
			
			arr_country.push(s_country_options[i].value); 
			
			f_rh_country();
		
			for (let b = 0; b < btn_close.length; b++) {
				btn_close[b].addEventListener("click", function () {
					arr_country.pop(btn_close[b].parentNode.getAttribute('data-id'));
					btn_close[b].parentNode.remove();
					f_rh_country();
				}
			)}

		}, false);
	}

	function f_rh_country() {	
		rh_country.value = arr_country;
	}
};
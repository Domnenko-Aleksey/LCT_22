import json
from GetData import GetData

def mainpage(CORE):
	CORE.debug('PATH: /stat_data/mainpage.py')

	CORE.addHeadFile('/templates/general/css/DAN.css')
	CORE.addHeadFile('/templates/general/js/DAN.js')
	CORE.addHeadFile('/templates/contextmenu/css/contextmenu.css')
	CORE.addHeadFile('/templates/contextmenu/js/contextmenu.js')
	CORE.addHeadFile('/templates/stat_data/css/mainpage.css')
	CORE.addHeadFile('/templates/stat_data/js/mainpage.js')
	CORE.addHeadFile('/templates/stat_data/js/pdf.js')

	GETDATA = GetData(CORE)
	regions = GETDATA.getRegions()

	region_options_html = ''
	for r in regions:
		region_options_html += f'''<option value="{r[0]}">{r[1]}</option>'''



	CORE.content = f'''
		<h1>Статистика</h1>
		<h3>Настроить фильтры</h3>
		<div class="stat_filters dan_flex_row">		
			<div class="flex_50">				
				<div class="dan_flex_row filters_row">				
					<div class="flex_50"><div>Направление перемещения</div></div>
					<div class="flex_50 dan_flex_row flex_end" style="gap:10px;">
						<select id="select_napr" class="select" name="select_napr" value="ИМЭК">
								<option value="ИМЭК" select>Импорт и экспорт</option>
								<option value="ИМ">Импорт</option>								
								<option value="ЭК">Экспорт</option>								
						</select>					
					</div>	
				</div>
				<div class="filters_row">
					<details><summary>Выберите ТН ВЭД</summary>
						<select id="select_tnved" class="stat_select" size="10" name="tnved[]" value="">
								<option value="01">01-ШТ-ЖИВЫЕ ЖИВОТНЫЕ</option>
								<option value="02">02-МЯСО И ПИЩЕВЫЕ МЯСНЫЕ СУБПРОДУКТЫ</option>
								<option value="03">03-РЫБА И РАКООБРАЗНЫЕ, МОЛЛЮСКИ И ПРОЧИЕ ВОДНЫЕ БЕСПОЗВОНОЧНЫЕ</option>
								<option value="04">04-МОЛОЧНАЯ ПРОДУКЦИЯ; ЯЙЦА ПТИЦ; МЕД НАТУРАЛЬНЫЙ; ПИЩЕВЫЕ ПРОДУКТЫ ЖИВОТНОГО ПРОИСХОЖДЕНИЯ, В ДРУГОМ МЕСТЕ НЕ ПОИМЕНОВАННЫЕ ИЛИ НЕ ВКЛЮЧЕННЫЕ</option>
								<option value="05">05-ПРОДУКТЫ ЖИВОТНОГО ПРОИСХОЖДЕНИЯ, В ДРУГОМ МЕСТЕ НЕ ПОИМЕНОВАННЫЕ ИЛИ НЕ ВКЛЮЧЕННЫЕ</option>
								<option value="06">06-ЖИВЫЕ ДЕРЕВЬЯ И ДРУГИЕ РАСТЕНИЯ; ЛУКОВИЦЫ, КОРНИ И ПРОЧИЕ АНАЛОГИЧНЫЕ ЧАСТИ РАСТЕНИЙ; СРЕЗАННЫЕ ЦВЕТЫ И ДЕКОРАТИВНАЯ ЗЕЛЕНЬ</option>
								<option value="07">07-ОВОЩИ И НЕКОТОРЫЕ СЪЕДОБНЫЕ КОРНЕПЛОДЫ И КЛУБНЕПЛОДЫ</option>
								<option value="08">08-СЪЕДОБНЫЕ ФРУКТЫ И ОРЕХИ; КОЖУРА ЦИТРУСОВЫХ ПЛОДОВ ИЛИ КОРКИ ДЫНЬ</option>
								<option value="09">09-КОФЕ, ЧАЙ, МАТЕ, ИЛИ ПАРАГВАЙСКИЙ ЧАЙ, И ПРЯНОСТИ</option>
								<option value="10">10-ЗЛАКИ</option>
								<option value="11">11-ПРОДУКЦИЯ МУКОМОЛЬНО-КРУПЯНОЙ ПРОМЫШЛЕННОСТИ; СОЛОД; КРАХМАЛЫ; ИНУЛИН; ПШЕНИЧНАЯ КЛЕЙКОВИНА</option>
								<option value="12">12-МАСЛИЧНЫЕ СЕМЕНА И ПЛОДЫ; ПРОЧИЕ СЕМЕНА, ПЛОДЫ И ЗЕРНО; ЛЕКАРСТВЕННЫЕ РАСТЕНИЯ И РАСТЕНИЯ ДЛЯ ТЕХНИЧЕСКИХ ЦЕЛЕЙ; СОЛОМА И ФУРАЖ</option>
								<option value="13">13-ШЕЛЛАК ПРИРОДНЫЙ НЕОЧИЩЕННЫЙ; КАМЕДИ, СМОЛЫ И ПРОЧИЕ РАСТИТЕЛЬНЫЕ СОКИ И ЭКСТРАКТЫ</option>
								<option value="14">14-РАСТИТЕЛЬНЫЕ МАТЕРИАЛЫ ДЛЯ ИЗГОТОВЛЕНИЯ ПЛЕТЕНЫХ ИЗДЕЛИЙ; ПРОЧИЕ ПРОДУКТЫ РАСТИТЕЛЬНОГО ПРОИСХОЖДЕНИЯ, В ДРУГОМ МЕСТЕ НЕ ПОИМЕНОВАННЫЕ ИЛИ НЕ ВКЛЮЧЕННЫЕ</option>
								<option value="15">15-ЖИРЫ И МАСЛА ЖИВОТНОГО ИЛИ РАСТИТЕЛЬНОГО ПРОИСХОЖДЕНИЯ И ПРОДУКТЫ ИХ РАСЩЕПЛЕНИЯ; ГОТОВЫЕ ПИЩЕВЫЕ ЖИРЫ; ВОСКИ ЖИВОТНОГО ИЛИ РАСТИТЕЛЬНОГО ПРОИСХОЖДЕНИЯ</option>
								<option value="16">16-ГОТОВЫЕ ПРОДУКТЫ ИЗ МЯСА, РЫБЫ ИЛИ РАКООБРАЗНЫХ, МОЛЛЮСКОВ ИЛИ ПРОЧИХ ВОДНЫХ БЕСПОЗВОНОЧНЫХ</option>
								<option value="17">17-САХАР И КОНДИТЕРСКИЕ ИЗДЕЛИЯ ИЗ САХАРА</option>
								<option value="18">18-КАКАО И ПРОДУКТЫ ИЗ НЕГО</option>
								<option value="19">19-ГОТОВЫЕ ПРОДУКТЫ ИЗ ЗЕРНА ЗЛАКОВ, МУКИ, КРАХМАЛА ИЛИ МОЛОКА; МУЧНЫЕ КОНДИТЕРСКИЕ ИЗДЕЛИЯ</option>
								<option value="20">20-ПРОДУКТЫ ПЕРЕРАБОТКИ ОВОЩЕЙ, ФРУКТОВ, ОРЕХОВ ИЛИ ПРОЧИХ ЧАСТЕЙ РАСТЕНИЙ</option>
								<option value="21">21-РАЗНЫЕ ПИЩЕВЫЕ ПРОДУКТЫ</option>
								<option value="22">22-АЛКОГОЛЬНЫЕ И БЕЗАЛКОГОЛЬНЫЕ НАПИТКИ И УКСУС</option>
								<option value="23">23-ОСТАТКИ И ОТХОДЫ ПИЩЕВОЙ ПРОМЫШЛЕННОСТИ; ГОТОВЫЕ КОРМА ДЛЯ ЖИВОТНЫХ</option>
								<option value="24">24-ТАБАК И ПРОМЫШЛЕННЫЕ ЗАМЕНИТЕЛИ ТАБАКА</option>
								<option value="25">25-СОЛЬ; СЕРА; ЗЕМЛИ И КАМЕНЬ; ШТУКАТУРНЫЕ МАТЕРИАЛЫ, ИЗВЕСТЬ И ЦЕМЕНТ</option>
								<option value="26">26-РУДЫ, ШЛАК И ЗОЛА</option>
								<option value="27">27-ТОПЛИВО МИНЕРАЛЬНОЕ, НЕФТЬ И ПРОДУКТЫ ИХ ПЕРЕГОНКИ; БИТУМИНОЗНЫЕ ВЕЩЕСТВА; ВОСКИ МИНЕРАЛЬНЫЕ</option>
								<option value="28">28-ПРОДУКТЫ НЕОРГАНИЧЕСКОЙ ХИМИИ; СОЕДИНЕНИЯ НЕОРГАНИЧЕСКИЕ ИЛИ ОРГАНИЧЕСКИЕ ДРАГОЦЕННЫХ МЕТАЛЛОВ, РЕДКОЗЕМЕЛЬНЫХ МЕТАЛЛОВ, РАДИОАКТИВНЫХ ЭЛЕМЕНТОВ ИЛИ ИЗОТОПОВ</option>
								<option value="29">29-ОРГАНИЧЕСКИЕ ХИМИЧЕСКИЕ СОЕДИНЕНИЯ</option>
								<option value="30">30-ФАРМАЦЕВТИЧЕСКАЯ ПРОДУКЦИЯ</option>
								<option value="31">31-УДОБРЕНИЯ</option>
								<option value="32">32-ЭКСТРАКТЫ ДУБИЛЬНЫЕ ИЛИ КРАСИЛЬНЫЕ; ТАННИНЫ И ИХ ПРОИЗВОДНЫЕ; КРАСИТЕЛИ, ПИГМЕНТЫ И ПРОЧИЕ КРАСЯЩИЕ ВЕЩЕСТВА; КРАСКИ И ЛАКИ; ШПАТЛЕВКИ И ПРОЧИЕ МАСТИКИ; ПОЛИГРАФИЧЕСКАЯ КРАСКА, ЧЕРНИЛА, ТУШЬ</option>
								<option value="33">33-ЭФИРНЫЕ МАСЛА И РЕЗИНОИДЫ; ПАРФЮМЕРНЫЕ, КОСМЕТИЧЕСКИЕ ИЛИ ТУАЛЕТНЫЕ СРЕДСТВА</option>
								<option value="34">34-МЫЛО, ПОВЕРХНОСТНО-АКТИВНЫЕ ОРГАНИЧЕСКИЕ ВЕЩЕСТВА, МОЮЩИЕ СРЕДСТВА, СМАЗОЧНЫЕ МАТЕРИАЛЫ, ИСКУССТВЕННЫЕ И ГОТОВЫЕ ВОСКИ, СОСТАВЫ ДЛЯ ЧИСТКИ ИЛИ ПОЛИРОВКИ, СВЕЧИ И АНАЛОГИЧНЫЕ ИЗДЕЛИЯ, ПАСТЫ ДЛЯ ЛЕПКИ, ПЛАСТИЛИН, "ЗУБОВРАЧЕБНЫЙ ВОСК" И ЗУБОВРАЧЕБНЫЕ СОСТАВЫ НА ОСНОВЕ ГИПСА</option>
								<option value="35">35-БЕЛКОВЫЕ ВЕЩЕСТВА; МОДИФИЦИРОВАННЫЕ КРАХМАЛЫ; КЛЕИ; ФЕРМЕНТЫ</option>
								<option value="36">36-ВЗРЫВЧАТЫЕ ВЕЩЕСТВА; ПИРОТЕХНИЧЕСКИЕ ИЗДЕЛИЯ; СПИЧКИ; ПИРОФОРНЫЕ СПЛАВЫ; НЕКОТОРЫЕ ГОРЮЧИЕ ВЕЩЕСТВА</option>
								<option value="37">37-ФОТО- И КИНОТОВАРЫ</option>
								<option value="38">38-ПРОЧИЕ ХИМИЧЕСКИЕ ПРОДУКТЫ</option>
								<option value="39">39-ПЛАСТМАССЫ И ИЗДЕЛИЯ ИЗ НИХ</option>
								<option value="40">40-КАУЧУК, РЕЗИНА И ИЗДЕЛИЯ ИЗ НИХ</option>
								<option value="41">41-НЕОБРАБОТАННЫЕ ШКУРЫ (КРОМЕ НАТУРАЛЬНОГО МЕХА) И ВЫДЕЛАННАЯ КОЖА</option>
								<option value="42">42-ИЗДЕЛИЯ ИЗ КОЖИ; ШОРНО-СЕДЕЛЬНЫЕ ИЗДЕЛИЯ И УПРЯЖЬ; ДОРОЖНЫЕ ПРИНАДЛЕЖНОСТИ, СУМКИ И АНАЛОГИЧНЫЕ ИМ ТОВАРЫ; ИЗДЕЛИЯ ИЗ ВНУТРЕННИХ ОРГАНОВ ЖИВОТНЫХ (КРОМЕ ШЕЛКООТДЕЛИТЕЛЬНЫХ ЖЕЛЕЗ ШЕЛКОПРЯДА)</option>
								<option value="43">43-НАТУРАЛЬНЫЙ И ИСКУССТВЕННЫЙ МЕХ; ИЗДЕЛИЯ ИЗ НЕГО</option>
								<option value="44">44-ДРЕВЕСИНА И ИЗДЕЛИЯ ИЗ НЕЕ; ДРЕВЕСНЫЙ УГОЛЬ</option>
								<option value="45">45-ПРОБКА И ИЗДЕЛИЯ ИЗ НЕЕ</option>
								<option value="46">46-ИЗДЕЛИЯ ИЗ СОЛОМЫ, АЛЬФЫ ИЛИ ПРОЧИХ МАТЕРИАЛОВ ДЛЯ ПЛЕТЕНИЯ; КОРЗИНОЧНЫЕ ИЗДЕЛИЯ И ПЛЕТЕНЫЕ ИЗДЕЛИЯ</option>
								<option value="47">47-МАССА ИЗ ДРЕВЕСИНЫ ИЛИ ИЗ ДРУГИХ ВОЛОКНИСТЫХ ЦЕЛЛЮЛОЗНЫХ МАТЕРИАЛОВ; РЕГЕНЕРИРУЕМЫЕ БУМАГА ИЛИ КАРТОН (МАКУЛАТУРА И ОТХОДЫ)</option>
								<option value="48">48-БУМАГА И КАРТОН; ИЗДЕЛИЯ ИЗ БУМАЖНОЙ МАССЫ, БУМАГИ ИЛИ КАРТОНА</option>
								<option value="49">49-ПЕЧАТНЫЕ КНИГИ, ГАЗЕТЫ, РЕПРОДУКЦИИ И ДРУГИЕ ИЗДЕЛИЯ ПОЛИГРАФИЧЕСКОЙ ПРОМЫШЛЕННОСТИ; РУКОПИСИ, МАШИНОПИСНЫЕ ТЕКСТЫ И ПЛАНЫ</option>
								<option value="50">50-ШЕЛК</option>
								<option value="51">51-ШЕРСТЬ, ТОНКИЙ ИЛИ ГРУБЫЙ ВОЛОС ЖИВОТНЫХ; ПРЯЖА И ТКАНЬ, ИЗ КОНСКОГО ВОЛОСА</option>
								<option value="52">52-ХЛОПОК</option>
								<option value="53">53-ПРОЧИЕ РАСТИТЕЛЬНЫЕ ТЕКСТИЛЬНЫЕ ВОЛОКНА; БУМАЖНАЯ ПРЯЖА И ТКАНИ ИЗ БУМАЖНОЙ ПРЯЖИ</option>
								<option value="54">54-ГРУППА 54 ХИМИЧЕСКИЕ НИТИ; ПЛОСКИЕ И АНАЛОГИЧНЫЕ НИТИ ИЗ ХИМИЧЕСКИХ ТЕКСТИЛЬНЫХ МАТЕРИАЛОВ</option>
								<option value="55">55-ХИМИЧЕСКИЕ ВОЛОКНА</option>
								<option value="56">56-ВАТА, ВОЙЛОК ИЛИ ФЕТР И НЕТКАНЫЕ МАТЕРИАЛЫ; СПЕЦИАЛЬНАЯ ПРЯЖА; БЕЧЕВКИ, ВЕРЕВКИ, КАНАТЫ И ТРОСЫ И ИЗДЕЛИЯ ИЗ НИХ</option>
								<option value="57">57-М2-КОВРЫ И ПРОЧИЕ ТЕКСТИЛЬНЫЕ НАПОЛЬНЫЕ ПОКРЫТИЯ</option>
								<option value="58">58-СПЕЦИАЛЬНЫЕ ТКАНИ; ТАФТИНГОВЫЕ ТЕКСТИЛЬНЫЕ МАТЕРИАЛЫ; КРУЖЕВА; ГОБЕЛЕНЫ; ОТДЕЛОЧНЫЕ МАТЕРИАЛЫ; ВЫШИВКИ</option>
								<option value="59">59-ТЕКСТИЛЬНЫЕ МАТЕРИАЛЫ, ПРОПИТАННЫЕ, С ПОКРЫТИЕМ ИЛИ ДУБЛИРОВАННЫЕ; ТЕКСТИЛЬНЫЕ ИЗДЕЛИЯ ТЕХНИЧЕСКОГО НАЗНАЧЕНИЯ</option>
								<option value="60">60-ТРИКОТАЖНЫЕ ПОЛОТНА МАШИННОГО ИЛИ РУЧНОГО ВЯЗАНИЯ</option>
								<option value="61">61-ПРЕДМЕТЫ ОДЕЖДЫ И ПРИНАДЛЕЖНОСТИ К ОДЕЖДЕ, ТРИКОТАЖНЫЕ МАШИННОГО ИЛИ РУЧНОГО ВЯЗАНИЯ</option>
								<option value="62">62-ПРЕДМЕТЫ ОДЕЖДЫ И ПРИНАДЛЕЖНОСТИ К ОДЕЖДЕ, КРОМЕ ТРИКОТАЖНЫХ МАШИННОГО ИЛИ РУЧНОГО ВЯЗАНИЯ</option>
								<option value="63">63-ПРОЧИЕ ГОТОВЫЕ ТЕКСТИЛЬНЫЕ ИЗДЕЛИЯ; НАБОРЫ; ОДЕЖДА И ТЕКСТИЛЬНЫЕ ИЗДЕЛИЯ, БЫВШИЕ В УПОТРЕБЛЕНИИ; ТРЯПЬЕ</option>
								<option value="64">64-ОБУВЬ, ГЕТРЫ И АНАЛОГИЧНЫЕ ИЗДЕЛИЯ; ИХ ДЕТАЛИ</option>
								<option value="65">65-ГОЛОВНЫЕ УБОРЫ И ИХ ЧАСТИ</option>
								<option value="66">66-ЗОНТЫ, СОЛНЦЕЗАЩИТНЫЕ ЗОНТЫ, ТРОСТИ, ТРОСТИ-СИДЕНЬЯ, ХЛЫСТЫ, КНУТЫ ДЛЯ ВЕРХОВОЙ ЕЗДЫ И ИХ ЧАСТИ</option>
								<option value="67">67-ОБРАБОТАННЫЕ ПЕРЬЯ И ПУХ И ИЗДЕЛИЯ ИЗ ПЕРЬЕВ ИЛИ ПУХА; ИСКУССТВЕННЫЕ ЦВЕТЫ; ИЗДЕЛИЯ ИЗ ЧЕЛОВЕЧЕСКОГО ВОЛОСА</option>
								<option value="68">68-ИЗДЕЛИЯ ИЗ КАМНЯ, ГИПСА, ЦЕМЕНТА, АСБЕСТА, СЛЮДЫ ИЛИ АНАЛОГИЧНЫХ МАТЕРИАЛОВ</option>
								<option value="69">69-КЕРАМИЧЕСКИЕ ИЗДЕЛИЯ</option>
								<option value="70">70-СТЕКЛО И ИЗДЕЛИЯ ИЗ НЕГО</option>
								<option value="71">71-ЖЕМЧУГ ПРИРОДНЫЙ ИЛИ КУЛЬТИВИРОВАННЫЙ, ДРАГОЦЕННЫЕ ИЛИ ПОЛУДРАГОЦЕННЫЕ КАМНИ, ДРАГОЦЕННЫЕ МЕТАЛЛЫ, МЕТАЛЛЫ, ПЛАКИРОВАННЫЕ ДРАГОЦЕННЫМИ МЕТАЛЛАМИ, И ИЗДЕЛИЯ ИЗ НИХ; БИЖУТЕРИЯ; МОНЕТЫ</option>
								<option value="72">72-ЧЕРНЫЕ МЕТАЛЛЫ</option>
								<option value="73">73-ИЗДЕЛИЯ ИЗ ЧЕРНЫХ МЕТАЛЛОВ</option>
								<option value="74">74-МЕДЬ И ИЗДЕЛИЯ ИЗ НЕЕ</option>
								<option value="75">75-НИКЕЛЬ И ИЗДЕЛИЯ ИЗ НЕГО</option>
								<option value="76">76-АЛЮМИНИЙ И ИЗДЕЛИЯ ИЗ НЕГО</option>
								
								<option value="78">78-СВИНЕЦ И ИЗДЕЛИЯ ИЗ НЕГО</option>
								<option value="79">79-ЦИНК И ИЗДЕЛИЯ ИЗ НЕГО</option>
								<option value="80">80-ОЛОВО И ИЗДЕЛИЯ ИЗ НЕГО</option>
								<option value="81">81-ПРОЧИЕ НЕДРАГОЦЕННЫЕ МЕТАЛЛЫ; МЕТАЛЛОКЕРАМИКА; ИЗДЕЛИЯ ИЗ НИХ</option>
								<option value="82">82-ИНСТРУМЕНТЫ, ПРИСПОСОБЛЕНИЯ, НОЖЕВЫЕ ИЗДЕЛИЯ, ЛОЖКИ И ВИЛКИ ИЗ НЕДРАГОЦЕННЫХ МЕТАЛЛОВ; ИХ ЧАСТИ ИЗ НЕДРАГОЦЕННЫХ МЕТАЛЛОВ</option>
								<option value="83">83-ПРОЧИЕ ИЗДЕЛИЯ ИЗ НЕДРАГОЦЕННЫХ МЕТАЛЛОВ</option>
								<option value="84">84-РЕАКТОРЫ ЯДЕРНЫЕ, КОТЛЫ, ОБОРУДОВАНИЕ И МЕХАНИЧЕСКИЕ УСТРОЙСТВА; ИХ ЧАСТИ</option>
								<option value="85">85-ЭЛЕКТРИЧЕСКИЕ МАШИНЫ И ОБОРУДОВАНИЕ, ИХ ЧАСТИ; ЗВУКОЗАПИСЫВАЮЩАЯ И ЗВУКОВОСПРОИЗВОДЯЩАЯ АППАРАТУРА, АППАРАТУРА ДЛЯ ЗАПИСИ И ВОСПРОИЗВЕДЕНИЯ ТЕЛЕВИЗИОННОГО ИЗОБРАЖЕНИЯ И ЗВУКА, ИХ ЧАСТИ И ПРИНАДЛЕЖНОСТИ</option>
								<option value="86">86-ЖЕЛЕЗНОДОРОЖНЫЕ ЛОКОМОТИВЫ ИЛИ МОТОРНЫЕ ВАГОНЫ ТРАМВАЯ, ПОДВИЖНОЙ СОСТАВ И ИХ ЧАСТИ; ПУТЕВОЕ ОБОРУДОВАНИЕ И УСТРОЙСТВА ДЛЯ ЖЕЛЕЗНЫХ ДОРОГ ИЛИ ТРАМВАЙНЫХ ПУТЕЙ И ИХ ЧАСТИ; МЕХАНИЧЕСКОЕ (ВКЛЮЧАЯ ЭЛЕКТРОМЕХАНИЧЕСКОЕ) СИГНАЛЬНОЕ ОБОРУДОВАНИЕ ВСЕХ ВИДОВ</option>
								<option value="87">87-СРЕДСТВА НАЗЕМНОГО ТРАНСПОРТА, КРОМЕ ЖЕЛЕЗНОДОРОЖНОГО ИЛИ ТРАМВАЙНОГО ПОДВИЖНОГО СОСТАВА, И ИХ ЧАСТИ И ПРИНАДЛЕЖНОСТИ</option>
								<option value="88">88-ЛЕТАТЕЛЬНЫЕ АППАРАТЫ, КОСМИЧЕСКИЕ АППАРАТЫ, И ИХ ЧАСТИ</option>
								<option value="89">89-ШТ-СУДА, ЛОДКИ И ПЛАВУЧИЕ КОНСТРУКЦИИ</option>
								<option value="90">90-ИНСТРУМЕНТЫ И АППАРАТЫ ОПТИЧЕСКИЕ, ФОТОГРАФИЧЕСКИЕ, КИНЕМАТОГРАФИЧЕСКИЕ, ИЗМЕРИТЕЛЬНЫЕ, КОНТРОЛЬНЫЕ, ПРЕЦИЗИОННЫЕ, МЕДИЦИНСКИЕ ИЛИ ХИРУРГИЧЕСКИЕ; ИХ ЧАСТИ И ПРИНАДЛЕЖНОСТИ</option>
								<option value="91">91-ЧАСЫ ВСЕХ ВИДОВ И ИХ ЧАСТИ</option>
								<option value="92">92-ИНСТРУМЕНТЫ МУЗЫКАЛЬНЫЕ; ИХ ЧАСТИ И ПРИНАДЛЕЖНОСТИ</option>
								<option value="93">93-ОРУЖИЕ И БОЕПРИПАСЫ; ИХ ЧАСТИ И ПРИНАДЛЕЖНОСТИ</option>
								<option value="94">94-МЕБЕЛЬ; ПОСТЕЛЬНЫЕ ПРИНАДЛЕЖНОСТИ, МАТРАЦЫ, ОСНОВЫ МАТРАЦНЫЕ, ДИВАННЫЕ ПОДУШКИ И АНАЛОГИЧНЫЕ НАБИВНЫЕ ПРИНАДЛЕЖНОСТИ МЕБЕЛИ; ЛАМПЫ И ОСВЕТИТЕЛЬНОЕ ОБОРУДОВАНИЕ, В ДРУГОМ МЕСТЕ НЕ ПОИМЕНОВАННЫЕ ИЛИ НЕ ВКЛЮЧЕННЫЕ; СВЕТОВЫЕ ВЫВЕСКИ, СВЕТОВЫЕ ТАБЛИЧКИ С ИМЕНЕМ ИЛИ НАЗВАНИЕМ, ИЛИ АДРЕСОМ И АНАЛОГИЧНЫЕ ИЗДЕЛИЯ; СБОРНЫЕ СТРОИТЕЛЬНЫЕ КОНСТРУКЦИИ</option>
								<option value="95">95-ИГРУШКИ, ИГРЫ И СПОРТИВНЫЙ ИНВЕНТАРЬ; ИХ ЧАСТИ И ПРИНАДЛЕЖНОСТИ</option>
								<option value="96">96-РАЗНЫЕ ГОТОВЫЕ ИЗДЕЛИЯ</option>
								<option value="97">97-ПРОИЗВЕДЕНИЯ ИСКУССТВА, ПРЕДМЕТЫ КОЛЛЕКЦИОНИРОВАНИЯ И АНТИКВАРИАТ</option>
								<option value="XX">XX-ПРОЧИЕ ТОВАРЫ</option>					
						</select>
						<div class="dan_flex_row result_container" id="result_tnved"></div>						
					</details>
				</div>
				<div class="dan_flex_row">				
					<div class="flex_50"><div>Выбрать дату</div></div>
					<div class="flex_50 dan_flex_row flex_end">
					
						<div class="dan_flex_row dan_flex_center filters_row">				
							<div class="flex_50">
								<label for="start">Дата начала</label>							
							</div>
							<div class="flex_50">
								<input class="select" type="month" id="start" name="start" min="2021-01" value="2021-01">									
							</div>
						</div>
						<div class="dan_flex_row dan_flex_center filters_row">	
							<div class="flex_50">							
								<label for="end">Дата завершения</label>
							</div>
							<div class="flex_50">							
								<input class="select" type="month" id="end" name="end" max="2021-12" value="2021-12">				
							</div>
						</div>	
					</div>	
				</div>
			</div>
			<div class="flex_50">				
				<div class="filters_row">				
					<details><summary>Выберите страну</summary>					
							<select id="select_country" class="stat_select" size="10" name="country[]" value="">
								<option value="AB">Абхазия</option>
								<option value="AU">Австралия</option>
								<option value="AT">Австрия</option>
								<option value="AZ">Азербайджан</option>
								<option value="AL">Албания</option>
								<option value="DZ">Алжир</option>
								<option value="AS">Американское Самоа</option>
								<option value="AI">Ангилья</option>
								<option value="AO">Ангола</option>
								<option value="AD">Андорра</option>
								<option value="AQ">Антарктида</option>
								<option value="AG">Антигуа и Барбуда</option>
								<option value="AR">Аргентина</option>
								<option value="AM">Армения</option>
								<option value="AW">Аруба</option>
								<option value="AF">Афганистан</option>
								<option value="BS">Багамы</option>
								<option value="BD">Бангладеш</option>
								<option value="BB">Барбадос</option>
								<option value="BH">Бахрейн</option>
								<option value="BY">Беларусь</option>
								<option value="BZ">Белиз</option>
								<option value="BE">Бельгия</option>
								<option value="BJ">Бенин</option>
								<option value="BM">Бермуды</option>
								<option value="BG">Болгария</option>
								<option value="BO">Боливия, Многонациональное Государство</option>
								<option value="BQ">Бонайре, Саба и Синт-Эстатиус</option>
								<option value="BA">Босния и Герцеговина</option>
								<option value="BW">Ботсвана</option>
								<option value="BR">Бразилия</option>
								<option value="IO">Британская территория в Индийском океане</option>
								<option value="BN">Бруней-Даруссалам</option>
								<option value="BF">Буркина-Фасо</option>
								<option value="BI">Бурунди</option>
								<option value="BT">Бутан</option>
								<option value="VU">Вануату</option>
								<option value="HU">Венгрия</option>
								<option value="VE">Венесуэла Боливарианская Республика</option>
								<option value="VG">Виргинские острова, Британские</option>
								<option value="VI">Виргинские острова, США</option>
								<option value="VN">Вьетнам</option>
								<option value="GA">Габон</option>
								<option value="HT">Гаити</option>
								<option value="GY">Гайана</option>
								<option value="GM">Гамбия</option>
								<option value="GH">Гана</option>
								<option value="GP">Гваделупа</option>
								<option value="GT">Гватемала</option>
								<option value="GN">Гвинея</option>
								<option value="GW">Гвинея-Бисау</option>
								<option value="DE">Германия</option>
								<option value="GG">Гернси</option>
								<option value="GI">Гибралтар</option>
								<option value="HN">Гондурас</option>
								<option value="HK">Гонконг</option>
								<option value="GD">Гренада</option>
								<option value="GL">Гренландия</option>
								<option value="GR">Греция</option>
								<option value="GE">Грузия</option>
								<option value="GU">Гуам</option>
								<option value="DK">Дания</option>
								<option value="JE">Джерси</option>
								<option value="DJ">Джибути</option>
								<option value="DM">Доминика</option>
								<option value="DO">Доминиканская Республика</option>
								<option value="EG">Египет</option>
								<option value="ZM">Замбия</option>
								<option value="EH">Западная Сахара</option>
								<option value="ZW">Зимбабве</option>
								<option value="IL">Израиль</option>
								<option value="IN">Индия</option>
								<option value="ID">Индонезия</option>
								<option value="JO">Иордания</option>
								<option value="IQ">Ирак</option>
								<option value="IR">Иран, Исламская Республика</option>
								<option value="IE">Ирландия</option>
								<option value="IS">Исландия</option>
								<option value="ES">Испания</option>
								<option value="IT">Италия</option>
								<option value="YE">Йемен</option>
								<option value="CV">Кабо-Верде</option>
								<option value="KZ">Казахстан</option>
								<option value="KH">Камбоджа</option>
								<option value="CM">Камерун</option>
								<option value="CA">Канада</option>
								<option value="QA">Катар</option>
								<option value="KE">Кения</option>
								<option value="CY">Кипр</option>
								<option value="KG">Киргизия</option>
								<option value="KI">Кирибати</option>
								<option value="CN">Китай</option>
								<option value="CC">Кокосовые (Килинг) острова</option>
								<option value="CO">Колумбия</option>
								<option value="KM">Коморы</option>
								<option value="CG">Конго</option>
								<option value="CD">Конго, Демократическая Республика</option>
								<option value="KP">Корея, Народно-Демократическая Республика</option>
								<option value="KR">Корея, Республика</option>
								<option value="CR">Коста-Рика</option>
								<option value="CI">Кот д'Ивуар</option>
								<option value="CU">Куба</option>
								<option value="KW">Кувейт</option>
								<option value="CW">Кюрасао</option>
								<option value="LA">Лаос</option>
								<option value="LV">Латвия</option>
								<option value="LS">Лесото</option>
								<option value="LB">Ливан</option>
								<option value="LY">Ливийская Арабская Джамахирия</option>
								<option value="LR">Либерия</option>
								<option value="LI">Лихтенштейн</option>
								<option value="LT">Литва</option>
								<option value="LU">Люксембург</option>
								<option value="MU">Маврикий</option>
								<option value="MR">Мавритания</option>
								<option value="MG">Мадагаскар</option>
								<option value="YT">Майотта</option>
								<option value="MO">Макао</option>
								<option value="MW">Малави</option>
								<option value="MY">Малайзия</option>
								<option value="ML">Мали</option>
								<option value="UM">Малые Тихоокеанские отдаленные острова Соединенных Штатов</option>
								<option value="MV">Мальдивы</option>
								<option value="MT">Мальта</option>
								<option value="MA">Марокко</option>
								<option value="MQ">Мартиника</option>
								<option value="MH">Маршалловы острова</option>
								<option value="MX">Мексика</option>
								<option value="FM">Микронезия, Федеративные Штаты</option>
								<option value="MZ">Мозамбик</option>
								<option value="MD">Молдова, Республика</option>
								<option value="MC">Монако</option>
								<option value="MN">Монголия</option>
								<option value="MS">Монтсеррат</option>
								<option value="MM">Мьянма</option>
								<option value="NA">Намибия</option>
								<option value="NR">Науру</option>
								<option value="NP">Непал</option>
								<option value="NE">Нигер</option>
								<option value="NG">Нигерия</option>
								<option value="NL">Нидерланды</option>
								<option value="NI">Никарагуа</option>
								<option value="NU">Ниуэ</option>
								<option value="NZ">Новая Зеландия</option>
								<option value="NC">Новая Каледония</option>
								<option value="NO">Норвегия</option>
								<option value="AE">Объединенные Арабские Эмираты</option>
								<option value="OM">Оман</option>
								<option value="BV">Остров Буве</option>
								<option value="IM">Остров Мэн</option>
								<option value="NF">Остров Норфолк</option>
								<option value="CX">Остров Рождества</option>
								<option value="HM">Остров Херд и острова Макдональд</option>
								<option value="KY">Острова Кайман</option>
								<option value="CK">Острова Кука</option>
								<option value="TC">Острова Теркс и Кайкос</option>
								<option value="PK">Пакистан</option>
								<option value="PW">Палау</option>
								<option value="PS">Палестинская территория, оккупированная</option>
								<option value="PA">Панама</option>
								<option value="VA">Папский Престол (Государство — город Ватикан)">
								<option value="PG">Папуа-Новая Гвинея</option>
								<option value="PY">Парагвай</option>
								<option value="PE">Перу</option>
								<option value="PN">Питкерн</option>
								<option value="PL">Польша</option>
								<option value="PT">Португалия</option>
								<option value="PR">Пуэрто-Рико</option>
								<option value="MK">Республика Македония</option>
								<option value="RE">Реюньон</option>
								<option value="RU">Россия</option>
								<option value="RW">Руанда</option>
								<option value="RO">Румыния</option>
								<option value="WS">Самоа</option>
								<option value="SM">Сан-Марино</option>
								<option value="ST">Сан-Томе и Принсипи</option>
								<option value="SA">Саудовская Аравия</option>
								<option value="SH">Святая Елена, Остров вознесения, Тристан-да-Кунья</option>
								<option value="MP">Северные Марианские острова</option>
								<option value="BL">Сен-Бартельми</option>
								<option value="MF">Сен-Мартен</option>
								<option value="SN">Сенегал</option>
								<option value="VC">Сент-Винсент и Гренадины</option>
								<option value="KN">Сент-Китс и Невис</option>
								<option value="LC">Сент-Люсия</option>
								<option value="PM">Сент-Пьер и Микелон</option>
								<option value="RS">Сербия</option>
								<option value="SC">Сейшелы</option>
								<option value="SG">Сингапур</option>
								<option value="SX">Синт-Мартен</option>
								<option value="SY">Сирийская Арабская Республика</option>
								<option value="SK">Словакия</option>
								<option value="SI">Словения</option>
								<option value="GB">Соединенное Королевство</option>
								<option value="US">Соединенные Штаты</option>
								<option value="SB">Соломоновы острова</option>
								<option value="SO">Сомали</option>
								<option value="SD">Судан</option>
								<option value="SR">Суринам</option>
								<option value="SL">Сьерра-Леоне</option>
								<option value="TJ">Таджикистан</option>
								<option value="TH">Таиланд</option>
								<option value="TW">Тайвань (Китай)">
								<option value="TZ">Танзания, Объединенная Республика</option>
								<option value="TL">Тимор-Лесте</option>
								<option value="TG">Того</option>
								<option value="TK">Токелау</option>
								<option value="TO">Тонга</option>
								<option value="TT">Тринидад и Тобаго</option>
								<option value="TV">Тувалу</option>
								<option value="TN">Тунис</option>
								<option value="TM">Туркмения</option>
								<option value="TR">Турция</option>
								<option value="UG">Уганда</option>
								<option value="UZ">Узбекистан</option>
								<option value="UA">Украина</option>
								<option value="WF">Уоллис и Футуна</option>
								<option value="UY">Уругвай</option>
								<option value="FO">Фарерские острова</option>
								<option value="FJ">Фиджи</option>
								<option value="PH">Филиппины</option>
								<option value="FI">Финляндия</option>
								<option value="FK">Фолклендские острова (Мальвинские)">
								<option value="FR">Франция</option>
								<option value="GF">Французская Гвиана</option>
								<option value="PF">Французская Полинезия</option>
								<option value="TF">Французские Южные территории</option>
								<option value="HR">Хорватия</option>
								<option value="CF">Центрально-Африканская Республика</option>
								<option value="TD">Чад</option>
								<option value="ME">Черногория</option>
								<option value="CZ">Чешская Республика</option>
								<option value="CL">Чили</option>
								<option value="CH">Швейцария</option>
								<option value="SE">Швеция</option>
								<option value="SJ">Шпицберген и Ян Майен</option>
								<option value="LK">Шри-Ланка</option>
								<option value="EC">Эквадор</option>
								<option value="GQ">Экваториальная Гвинея</option>
								<option value="AX">Эландские острова</option>
								<option value="SV">Эль-Сальвадор</option>
								<option value="ER">Эритрея</option>
								<option value="SZ">Эсватини</option>
								<option value="EE">Эстония</option>
								<option value="ET">Эфиопия</option>
								<option value="ZA">Южная Африка</option>
								<option value="GS">Южная Джорджия и Южные Сандвичевы острова</option>
								<option value="OS">Южная Осетия</option>
								<option value="SS">Южный Судан</option>
								<option value="JM">Ямайка</option>
								<option value="JP">Япония</option>
							</select>							
							<div class="dan_flex_row result_container" id="result_country"></div>
					</details>			
				</div>
				<div class="filters_row">				
					<details><summary>Выберите регион</summary>					
							<select id="select_region" class="stat_select" size="10" name="region[]" value="">
								{region_options_html}
							</select>
							<div class="dan_flex_row result_container" id="result_region"></div>
					</details>
				</div>				

				<div id="send_result_button" class="dan_button_red">Применить</div>
			</div>	
			</div>          
			
		<div id="answer_content"></div>		

	'''
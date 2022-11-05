# from Users import Users

def mainpage(CORE):
    CORE.debug('PATH: /analisis/mainpage.py')

    CORE.addHeadFile('/templates/general/css/DAN.css')
    CORE.addHeadFile('/templates/general/js/DAN.js')
    CORE.addHeadFile('/templates/contextmenu/css/contextmenu.css')
    CORE.addHeadFile('/templates/contextmenu/js/contextmenu.js')
    CORE.addHeadFile('/templates/analisis/css/mainpage.css')
    CORE.addHeadFile('/templates/analisis/js/mainpage.js')

    # USER = Users(CORE)
    # users = USER.getUsersList()


    CORE.content = f'''
        <h1>Статистика</h1>
        <div class="stat_filters dan_flex_row">
			<div class="flex_50">
				<h2>Настроить фильтры</h2>
				<div class="dan_flex_row filters_row">				
					<div class="flex_50"><div>Направление перемещения</div></div>
					<div class="flex_50 flex_row" style="gap:10px;">
						<div class="pt10 pbc10 flex_row nowrap flex_start">
							<span><input class="dan_input" type="radio" id="input_import" name="travel_direction" value="Импорт" checked><label for="input_import">Импорт</label></span>
						</div>
						<div class="pt10 pbc10 flex_row nowrap flex_start">
							<span><input class="dan_input" type="radio" id="input_import_export" name="travel_direction" value="Импорт и экспорт"><label for="input_import_export">Импорт и экспорт</label></span>
						</div>
						<div class="pt10 pbc10 flex_row nowrap flex_start"><span><input class="dan_input" type="radio" id="input_export" name="travel_direction" value="Экспорт"><label for="input_export">Экспорт</label></span>
						</div>
					</div>	
				</div>
				<div class="filters_row">				
					<details>
                        <summary>Выберите Страну</summary>					
							<select id="select_country" size="10" name="country[]" value="">
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
                    </details>
                </div>		
				<div class="dan_flex_row filters_row">				
					<div class="flex_50"><div>Отображение веса</div></div>
					<div class="flex_50 flex_row" style="gap:10px;">
						<div class="pt10 pbc10 flex_row nowrap flex_start">
							<span><input class="dan_input" type="radio" id="input_kg" name="weight" value="кг" checked><label for="input_kg">кг</label></span>
						</div>
						<div class="pt10 pbc10 flex_row nowrap flex_start">
							<span><input class="dan_input" type="radio" id="input_t" name="weight" value="т"><label for="input_t">тонна</label></span>
						</div>
					</div>
				</div>
				<div><br><br><input id="result_hidden_travel_direction" type="text" value=""></div>
				<div><br><input id="result_hidden_country" type="hidden" value=""></div>
			</div>
          <div class="flex_50">
			<div><h2>Страна</h2></div>
				<div class="dan_flex_row result_container" id="result_country"></div>
		  </div>
          <div id="send_result_button" class="dan_button_red">Отправить</div>
        </div>
        <table class="admin_table dan_even_odd">
            <tr>
                <th style="width:50px">№</th>
                <th style="width:50px"></th>
                <th>Имя.</th>
                <th style="width:150px">Телефон</th>
                <th style="width:150px">Последний визит</th>
                <th style="width:150px">Регистрация</th>
                <th style="width:100px">Статус</th>
            </tr>
        </table>
  </div>
    '''
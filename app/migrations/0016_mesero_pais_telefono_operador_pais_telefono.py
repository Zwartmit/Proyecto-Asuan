# Generated by Django 5.0.6 on 2024-06-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_cliente_pais_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesero',
            name='pais_telefono',
            field=models.CharField(choices=[('Afganistán (+93)', 'Afganistán (+93)'), ('Albania (+355)', 'Albania (+355)'), ('Alemania (+49)', 'Alemania (+49)'), ('Andorra (+376)', 'Andorra (+376)'), ('Angola (+244)', 'Angola (+244)'), ('Anguila (+1 264)', 'Anguila (+1 264)'), ('Antártida (+672)', 'Antártida (+672)'), ('Antigua y Barbuda (+1 268)', 'Antigua y Barbuda (+1 268)'), ('Arabia Saudita (+966)', 'Arabia Saudita (+966)'), ('Argelia (+213)', 'Argelia (+213)'), ('Argentina (+54)', 'Argentina (+54)'), ('Armenia (+374)', 'Armenia (+374)'), ('Aruba (+297)', 'Aruba (+297)'), ('Australia (+61)', 'Australia (+61)'), ('Austria (+43)', 'Austria (+43)'), ('Azerbaiyán (+994)', 'Azerbaiyán (+994)'), ('Bahamas (+1 242)', 'Bahamas (+1 242)'), ('Bangladés (+880)', 'Bangladés (+880)'), ('Barbados (+1 246)', 'Barbados (+1 246)'), ('Baréin (+973)', 'Baréin (+973)'), ('Bélgica (+32)', 'Bélgica (+32)'), ('Belice (+501)', 'Belice (+501)'), ('Benín (+229)', 'Benín (+229)'), ('Bermudas (+1 441)', 'Bermudas (+1 441)'), ('Bielorrusia (+375)', 'Bielorrusia (+375)'), ('Bolivia (+591)', 'Bolivia (+591)'), ('Bosnia y Herzegovina (+387)', 'Bosnia y Herzegovina (+387)'), ('Botsuana (+267)', 'Botsuana (+267)'), ('Brasil (+55)', 'Brasil (+55)'), ('Brunéi (+673)', 'Brunéi (+673)'), ('Bulgaria (+359)', 'Bulgaria (+359)'), ('Burkina Faso (+226)', 'Burkina Faso (+226)'), ('Burundi (+257)', 'Burundi (+257)'), ('Bután (+975)', 'Bután (+975)'), ('Cabo Verde (+238)', 'Cabo Verde (+238)'), ('Camboya (+855)', 'Camboya (+855)'), ('Camerún (+237)', 'Camerún (+237)'), ('Canadá (+1)', 'Canadá (+1)'), ('Catar (+974)', 'Catar (+974)'), ('Chad (+235)', 'Chad (+235)'), ('Chile (+56)', 'Chile (+56)'), ('China (+86)', 'China (+86)'), ('Chipre (+357)', 'Chipre (+357)'), ('Colombia (+57)', 'Colombia (+57)'), ('Comoras (+269)', 'Comoras (+269)'), ('Congo (+242)', 'Congo (+242)'), ('Corea del Norte (+850)', 'Corea del Norte (+850)'), ('Corea del Sur (+82)', 'Corea del Sur (+82)'), ('Costa de Marfil (+225)', 'Costa de Marfil (+225)'), ('Costa Rica (+506)', 'Costa Rica (+506)'), ('Croacia (+385)', 'Croacia (+385)'), ('Cuba (+53)', 'Cuba (+53)'), ('Dinamarca (+45)', 'Dinamarca (+45)'), ('Dominica (+1 767)', 'Dominica (+1 767)'), ('Ecuador (+593)', 'Ecuador (+593)'), ('Egipto (+20)', 'Egipto (+20)'), ('El Salvador (+503)', 'El Salvador (+503)'), ('Emiratos Árabes Unidos (+971)', 'Emiratos Árabes Unidos (+971)'), ('Eritrea (+291)', 'Eritrea (+291)'), ('Eslovaquia (+421)', 'Eslovaquia (+421)'), ('Eslovenia (+386)', 'Eslovenia (+386)'), ('España (+34)', 'España (+34)'), ('Estados Unidos (+1)', 'Estados Unidos (+1)'), ('Estonia (+372)', 'Estonia (+372)'), ('Etiopía (+251)', 'Etiopía (+251)'), ('Fiji (+679)', 'Fiji (+679)'), ('Filipinas (+63)', 'Filipinas (+63)'), ('Finlandia (+358)', 'Finlandia (+358)'), ('Francia (+33)', 'Francia (+33)'), ('Gabón (+241)', 'Gabón (+241)'), ('Gambia (+220)', 'Gambia (+220)'), ('Georgia (+995)', 'Georgia (+995)'), ('Ghana (+233)', 'Ghana (+233)'), ('Gibraltar (+350)', 'Gibraltar (+350)'), ('Granada (+1 473)', 'Granada (+1 473)'), ('Grecia (+30)', 'Grecia (+30)'), ('Groenlandia (+299)', 'Groenlandia (+299)'), ('Guadalupe (+590)', 'Guadalupe (+590)'), ('Guam (+1 671)', 'Guam (+1 671)'), ('Guatemala (+502)', 'Guatemala (+502)'), ('Guayana Francesa (+594)', 'Guayana Francesa (+594)'), ('Guernsey (+44 1481)', 'Guernsey (+44 1481)'), ('Guinea (+224)', 'Guinea (+224)'), ('Guinea Ecuatorial (+240)', 'Guinea Ecuatorial (+240)'), ('Guinea-Bisáu (+245)', 'Guinea-Bisáu (+245)'), ('Guyana (+592)', 'Guyana (+592)'), ('Haití (+509)', 'Haití (+509)'), ('Honduras (+504)', 'Honduras (+504)'), ('Hong Kong (+852)', 'Hong Kong (+852)'), ('Hungría (+36)', 'Hungría (+36)'), ('India (+91)', 'India (+91)'), ('Indonesia (+62)', 'Indonesia (+62)'), ('Irak (+964)', 'Irak (+964)'), ('Irán (+98)', 'Irán (+98)'), ('Irlanda (+353)', 'Irlanda (+353)'), ('Isla Bouvet (+47)', 'Isla Bouvet (+47)'), ('Isla de Man (+44 1624)', 'Isla de Man (+44 1624)'), ('Isla Navidad (+61)', 'Isla Navidad (+61)'), ('Isla Norfolk (+672)', 'Isla Norfolk (+672)'), ('Islandia (+354)', 'Islandia (+354)'), ('Islas Åland (+358)', 'Islas Åland (+358)'), ('Islas Caimán (+1 345)', 'Islas Caimán (+1 345)'), ('Islas Cocos (+61)', 'Islas Cocos (+61)'), ('Islas Cook (+682)', 'Islas Cook (+682)'), ('Islas Feroe (+298)', 'Islas Feroe (+298)'), ('Islas Georgias del Sur y Sandwich del Sur (+500)', 'Islas Georgias del Sur y Sandwich del Sur (+500)'), ('Islas Heard y McDonald (+672)', 'Islas Heard y McDonald (+672)'), ('Islas Malvinas (+500)', 'Islas Malvinas (+500)'), ('Islas Marianas del Norte (+1 670)', 'Islas Marianas del Norte (+1 670)'), ('Islas Marshall (+692)', 'Islas Marshall (+692)'), ('Islas menores alejadas de los Estados Unidos (+1)', 'Islas menores alejadas de los Estados Unidos (+1)'), ('Islas Salomón (+677)', 'Islas Salomón (+677)'), ('Islas Turcas y Caicos (+1 649)', 'Islas Turcas y Caicos (+1 649)'), ('Islas Vírgenes Británicas (+1 284)', 'Islas Vírgenes Británicas (+1 284)'), ('Islas Vírgenes de los Estados Unidos (+1 340)', 'Islas Vírgenes de los Estados Unidos (+1 340)'), ('Israel (+972)', 'Israel (+972)'), ('Italia (+39)', 'Italia (+39)'), ('Jamaica (+1 876)', 'Jamaica (+1 876)'), ('Japón (+81)', 'Japón (+81)'), ('Jersey (+44 1534)', 'Jersey (+44 1534)'), ('Jordania (+962)', 'Jordania (+962)'), ('Kazajistán (+7)', 'Kazajistán (+7)'), ('Kenia (+254)', 'Kenia (+254)'), ('Kirguistán (+996)', 'Kirguistán (+996)'), ('Kiribati (+686)', 'Kiribati (+686)'), ('Kuwait (+965)', 'Kuwait (+965)'), ('Laos (+856)', 'Laos (+856)'), ('Lesoto (+266)', 'Lesoto (+266)'), ('Letonia (+371)', 'Letonia (+371)'), ('Líbano (+961)', 'Líbano (+961)'), ('Liberia (+231)', 'Liberia (+231)'), ('Libia (+218)', 'Libia (+218)'), ('Liechtenstein (+423)', 'Liechtenstein (+423)'), ('Lituania (+370)', 'Lituania (+370)'), ('Luxemburgo (+352)', 'Luxemburgo (+352)'), ('Macao (+853)', 'Macao (+853)'), ('Madagascar (+261)', 'Madagascar (+261)'), ('Malasia (+60)', 'Malasia (+60)'), ('Malaui (+265)', 'Malaui (+265)'), ('Maldivas (+960)', 'Maldivas (+960)'), ('Malí (+223)', 'Malí (+223)'), ('Malta (+356)', 'Malta (+356)'), ('Marruecos (+212)', 'Marruecos (+212)'), ('Martinica (+596)', 'Martinica (+596)'), ('Mauricio (+230)', 'Mauricio (+230)'), ('Mauritania (+222)', 'Mauritania (+222)'), ('Mayotte (+262)', 'Mayotte (+262)'), ('México (+52)', 'México (+52)'), ('Micronesia (+691)', 'Micronesia (+691)'), ('Moldavia (+373)', 'Moldavia (+373)'), ('Mónaco (+377)', 'Mónaco (+377)'), ('Mongolia (+976)', 'Mongolia (+976)'), ('Montenegro (+382)', 'Montenegro (+382)'), ('Montserrat (+1 664)', 'Montserrat (+1 664)'), ('Mozambique (+258)', 'Mozambique (+258)'), ('Myanmar (+95)', 'Myanmar (+95)'), ('Namibia (+264)', 'Namibia (+264)'), ('Nauru (+674)', 'Nauru (+674)'), ('Nepal (+977)', 'Nepal (+977)'), ('Nicaragua (+505)', 'Nicaragua (+505)'), ('Níger (+227)', 'Níger (+227)'), ('Nigeria (+234)', 'Nigeria (+234)'), ('Niue (+683)', 'Niue (+683)'), ('Noruega (+47)', 'Noruega (+47)'), ('Nueva Caledonia (+687)', 'Nueva Caledonia (+687)'), ('Nueva Zelanda (+64)', 'Nueva Zelanda (+64)'), ('Omán (+968)', 'Omán (+968)'), ('Países Bajos (+31)', 'Países Bajos (+31)'), ('Pakistán (+92)', 'Pakistán (+92)'), ('Palaos (+680)', 'Palaos (+680)'), ('Palestina (+970)', 'Palestina (+970)'), ('Panamá (+507)', 'Panamá (+507)'), ('Papúa Nueva Guinea (+675)', 'Papúa Nueva Guinea (+675)'), ('Paraguay (+595)', 'Paraguay (+595)'), ('Perú (+51)', 'Perú (+51)'), ('Polinesia Francesa (+689)', 'Polinesia Francesa (+689)'), ('Polonia (+48)', 'Polonia (+48)'), ('Portugal (+351)', 'Portugal (+351)'), ('Puerto Rico (+1 787)', 'Puerto Rico (+1 787)'), ('Reino Unido (+44)', 'Reino Unido (+44)'), ('República Centroafricana (+236)', 'República Centroafricana (+236)'), ('República Checa (+420)', 'República Checa (+420)'), ('República del Congo (+242)', 'República del Congo (+242)'), ('República Dominicana (+1 809)', 'República Dominicana (+1 809)'), ('Reunión (+262)', 'Reunión (+262)'), ('Ruanda (+250)', 'Ruanda (+250)'), ('Rumania (+40)', 'Rumania (+40)'), ('Rusia (+7)', 'Rusia (+7)'), ('Sáhara Occidental (+212)', 'Sáhara Occidental (+212)'), ('Samoa (+685)', 'Samoa (+685)'), ('Samoa Americana (+1 684)', 'Samoa Americana (+1 684)'), ('San Bartolomé (+590)', 'San Bartolomé (+590)'), ('San Cristóbal y Nieves (+1 869)', 'San Cristóbal y Nieves (+1 869)'), ('San Marino (+378)', 'San Marino (+378)'), ('San Martín (Francia) (+590)', 'San Martín (Francia) (+590)'), ('San Pedro y Miquelón (+508)', 'San Pedro y Miquelón (+508)'), ('San Vicente y las Granadinas (+1 784)', 'San Vicente y las Granadinas (+1 784)'), ('Santa Elena, Ascensión y Tristán de Acuña (+290)', 'Santa Elena, Ascensión y Tristán de Acuña (+290)'), ('Santa Lucía (+1 758)', 'Santa Lucía (+1 758)'), ('Santa Sede (Ciudad del Vaticano) (+379)', 'Santa Sede (Ciudad del Vaticano) (+379)'), ('Santo Tomé y Príncipe (+239)', 'Santo Tomé y Príncipe (+239)'), ('Senegal (+221)', 'Senegal (+221)'), ('Serbia (+381)', 'Serbia (+381)'), ('Seychelles (+248)', 'Seychelles (+248)'), ('Sierra Leona (+232)', 'Sierra Leona (+232)'), ('Singapur (+65)', 'Singapur (+65)'), ('Sint Maarten (+1 721)', 'Sint Maarten (+1 721)'), ('Siria (+963)', 'Siria (+963)'), ('Somalia (+252)', 'Somalia (+252)'), ('Sri Lanka (+94)', 'Sri Lanka (+94)'), ('Sudáfrica (+27)', 'Sudáfrica (+27)'), ('Sudán (+249)', 'Sudán (+249)'), ('Sudán del Sur (+211)', 'Sudán del Sur (+211)'), ('Suecia (+46)', 'Suecia (+46)'), ('Suiza (+41)', 'Suiza (+41)'), ('Surinam (+597)', 'Surinam (+597)'), ('Svalbard y Jan Mayen (+47)', 'Svalbard y Jan Mayen (+47)'), ('Swazilandia (+268)', 'Swazilandia (+268)'), ('Tailandia (+66)', 'Tailandia (+66)'), ('Taiwán (+886)', 'Taiwán (+886)'), ('Tanzania (+255)', 'Tanzania (+255)'), ('Tayikistán (+992)', 'Tayikistán (+992)'), ('Territorio Británico del Océano Índico (+246)', 'Territorio Británico del Océano Índico (+246)'), ('Territorios Australes Franceses (+262)', 'Territorios Australes Franceses (+262)'), ('Timor Oriental (+670)', 'Timor Oriental (+670)'), ('Togo (+228)', 'Togo (+228)'), ('Tokelau (+690)', 'Tokelau (+690)'), ('Tonga (+676)', 'Tonga (+676)'), ('Trinidad y Tobago (+1 868)', 'Trinidad y Tobago (+1 868)'), ('Túnez (+216)', 'Túnez (+216)'), ('Turkmenistán (+993)', 'Turkmenistán (+993)'), ('Turquía (+90)', 'Turquía (+90)'), ('Tuvalu (+688)', 'Tuvalu (+688)'), ('Ucrania (+380)', 'Ucrania (+380)'), ('Uganda (+256)', 'Uganda (+256)'), ('Uruguay (+598)', 'Uruguay (+598)'), ('Uzbekistán (+998)', 'Uzbekistán (+998)'), ('Vanuatu (+678)', 'Vanuatu (+678)'), ('Venezuela (+58)', 'Venezuela (+58)'), ('Vietnam (+84)', 'Vietnam (+84)'), ('Wallis y Futuna (+681)', 'Wallis y Futuna (+681)'), ('Yemen (+967)', 'Yemen (+967)'), ('Yibuti (+253)', 'Yibuti (+253)'), ('Zambia (+260)', 'Zambia (+260)'), ('Zimbabue (+263)', 'Zimbabue (+263)')], default='Colombia (+57)', max_length=50, verbose_name='Prefijo telefónico'),
        ),
        migrations.AddField(
            model_name='operador',
            name='pais_telefono',
            field=models.CharField(choices=[('Afganistán (+93)', 'Afganistán (+93)'), ('Albania (+355)', 'Albania (+355)'), ('Alemania (+49)', 'Alemania (+49)'), ('Andorra (+376)', 'Andorra (+376)'), ('Angola (+244)', 'Angola (+244)'), ('Anguila (+1 264)', 'Anguila (+1 264)'), ('Antártida (+672)', 'Antártida (+672)'), ('Antigua y Barbuda (+1 268)', 'Antigua y Barbuda (+1 268)'), ('Arabia Saudita (+966)', 'Arabia Saudita (+966)'), ('Argelia (+213)', 'Argelia (+213)'), ('Argentina (+54)', 'Argentina (+54)'), ('Armenia (+374)', 'Armenia (+374)'), ('Aruba (+297)', 'Aruba (+297)'), ('Australia (+61)', 'Australia (+61)'), ('Austria (+43)', 'Austria (+43)'), ('Azerbaiyán (+994)', 'Azerbaiyán (+994)'), ('Bahamas (+1 242)', 'Bahamas (+1 242)'), ('Bangladés (+880)', 'Bangladés (+880)'), ('Barbados (+1 246)', 'Barbados (+1 246)'), ('Baréin (+973)', 'Baréin (+973)'), ('Bélgica (+32)', 'Bélgica (+32)'), ('Belice (+501)', 'Belice (+501)'), ('Benín (+229)', 'Benín (+229)'), ('Bermudas (+1 441)', 'Bermudas (+1 441)'), ('Bielorrusia (+375)', 'Bielorrusia (+375)'), ('Bolivia (+591)', 'Bolivia (+591)'), ('Bosnia y Herzegovina (+387)', 'Bosnia y Herzegovina (+387)'), ('Botsuana (+267)', 'Botsuana (+267)'), ('Brasil (+55)', 'Brasil (+55)'), ('Brunéi (+673)', 'Brunéi (+673)'), ('Bulgaria (+359)', 'Bulgaria (+359)'), ('Burkina Faso (+226)', 'Burkina Faso (+226)'), ('Burundi (+257)', 'Burundi (+257)'), ('Bután (+975)', 'Bután (+975)'), ('Cabo Verde (+238)', 'Cabo Verde (+238)'), ('Camboya (+855)', 'Camboya (+855)'), ('Camerún (+237)', 'Camerún (+237)'), ('Canadá (+1)', 'Canadá (+1)'), ('Catar (+974)', 'Catar (+974)'), ('Chad (+235)', 'Chad (+235)'), ('Chile (+56)', 'Chile (+56)'), ('China (+86)', 'China (+86)'), ('Chipre (+357)', 'Chipre (+357)'), ('Colombia (+57)', 'Colombia (+57)'), ('Comoras (+269)', 'Comoras (+269)'), ('Congo (+242)', 'Congo (+242)'), ('Corea del Norte (+850)', 'Corea del Norte (+850)'), ('Corea del Sur (+82)', 'Corea del Sur (+82)'), ('Costa de Marfil (+225)', 'Costa de Marfil (+225)'), ('Costa Rica (+506)', 'Costa Rica (+506)'), ('Croacia (+385)', 'Croacia (+385)'), ('Cuba (+53)', 'Cuba (+53)'), ('Dinamarca (+45)', 'Dinamarca (+45)'), ('Dominica (+1 767)', 'Dominica (+1 767)'), ('Ecuador (+593)', 'Ecuador (+593)'), ('Egipto (+20)', 'Egipto (+20)'), ('El Salvador (+503)', 'El Salvador (+503)'), ('Emiratos Árabes Unidos (+971)', 'Emiratos Árabes Unidos (+971)'), ('Eritrea (+291)', 'Eritrea (+291)'), ('Eslovaquia (+421)', 'Eslovaquia (+421)'), ('Eslovenia (+386)', 'Eslovenia (+386)'), ('España (+34)', 'España (+34)'), ('Estados Unidos (+1)', 'Estados Unidos (+1)'), ('Estonia (+372)', 'Estonia (+372)'), ('Etiopía (+251)', 'Etiopía (+251)'), ('Fiji (+679)', 'Fiji (+679)'), ('Filipinas (+63)', 'Filipinas (+63)'), ('Finlandia (+358)', 'Finlandia (+358)'), ('Francia (+33)', 'Francia (+33)'), ('Gabón (+241)', 'Gabón (+241)'), ('Gambia (+220)', 'Gambia (+220)'), ('Georgia (+995)', 'Georgia (+995)'), ('Ghana (+233)', 'Ghana (+233)'), ('Gibraltar (+350)', 'Gibraltar (+350)'), ('Granada (+1 473)', 'Granada (+1 473)'), ('Grecia (+30)', 'Grecia (+30)'), ('Groenlandia (+299)', 'Groenlandia (+299)'), ('Guadalupe (+590)', 'Guadalupe (+590)'), ('Guam (+1 671)', 'Guam (+1 671)'), ('Guatemala (+502)', 'Guatemala (+502)'), ('Guayana Francesa (+594)', 'Guayana Francesa (+594)'), ('Guernsey (+44 1481)', 'Guernsey (+44 1481)'), ('Guinea (+224)', 'Guinea (+224)'), ('Guinea Ecuatorial (+240)', 'Guinea Ecuatorial (+240)'), ('Guinea-Bisáu (+245)', 'Guinea-Bisáu (+245)'), ('Guyana (+592)', 'Guyana (+592)'), ('Haití (+509)', 'Haití (+509)'), ('Honduras (+504)', 'Honduras (+504)'), ('Hong Kong (+852)', 'Hong Kong (+852)'), ('Hungría (+36)', 'Hungría (+36)'), ('India (+91)', 'India (+91)'), ('Indonesia (+62)', 'Indonesia (+62)'), ('Irak (+964)', 'Irak (+964)'), ('Irán (+98)', 'Irán (+98)'), ('Irlanda (+353)', 'Irlanda (+353)'), ('Isla Bouvet (+47)', 'Isla Bouvet (+47)'), ('Isla de Man (+44 1624)', 'Isla de Man (+44 1624)'), ('Isla Navidad (+61)', 'Isla Navidad (+61)'), ('Isla Norfolk (+672)', 'Isla Norfolk (+672)'), ('Islandia (+354)', 'Islandia (+354)'), ('Islas Åland (+358)', 'Islas Åland (+358)'), ('Islas Caimán (+1 345)', 'Islas Caimán (+1 345)'), ('Islas Cocos (+61)', 'Islas Cocos (+61)'), ('Islas Cook (+682)', 'Islas Cook (+682)'), ('Islas Feroe (+298)', 'Islas Feroe (+298)'), ('Islas Georgias del Sur y Sandwich del Sur (+500)', 'Islas Georgias del Sur y Sandwich del Sur (+500)'), ('Islas Heard y McDonald (+672)', 'Islas Heard y McDonald (+672)'), ('Islas Malvinas (+500)', 'Islas Malvinas (+500)'), ('Islas Marianas del Norte (+1 670)', 'Islas Marianas del Norte (+1 670)'), ('Islas Marshall (+692)', 'Islas Marshall (+692)'), ('Islas menores alejadas de los Estados Unidos (+1)', 'Islas menores alejadas de los Estados Unidos (+1)'), ('Islas Salomón (+677)', 'Islas Salomón (+677)'), ('Islas Turcas y Caicos (+1 649)', 'Islas Turcas y Caicos (+1 649)'), ('Islas Vírgenes Británicas (+1 284)', 'Islas Vírgenes Británicas (+1 284)'), ('Islas Vírgenes de los Estados Unidos (+1 340)', 'Islas Vírgenes de los Estados Unidos (+1 340)'), ('Israel (+972)', 'Israel (+972)'), ('Italia (+39)', 'Italia (+39)'), ('Jamaica (+1 876)', 'Jamaica (+1 876)'), ('Japón (+81)', 'Japón (+81)'), ('Jersey (+44 1534)', 'Jersey (+44 1534)'), ('Jordania (+962)', 'Jordania (+962)'), ('Kazajistán (+7)', 'Kazajistán (+7)'), ('Kenia (+254)', 'Kenia (+254)'), ('Kirguistán (+996)', 'Kirguistán (+996)'), ('Kiribati (+686)', 'Kiribati (+686)'), ('Kuwait (+965)', 'Kuwait (+965)'), ('Laos (+856)', 'Laos (+856)'), ('Lesoto (+266)', 'Lesoto (+266)'), ('Letonia (+371)', 'Letonia (+371)'), ('Líbano (+961)', 'Líbano (+961)'), ('Liberia (+231)', 'Liberia (+231)'), ('Libia (+218)', 'Libia (+218)'), ('Liechtenstein (+423)', 'Liechtenstein (+423)'), ('Lituania (+370)', 'Lituania (+370)'), ('Luxemburgo (+352)', 'Luxemburgo (+352)'), ('Macao (+853)', 'Macao (+853)'), ('Madagascar (+261)', 'Madagascar (+261)'), ('Malasia (+60)', 'Malasia (+60)'), ('Malaui (+265)', 'Malaui (+265)'), ('Maldivas (+960)', 'Maldivas (+960)'), ('Malí (+223)', 'Malí (+223)'), ('Malta (+356)', 'Malta (+356)'), ('Marruecos (+212)', 'Marruecos (+212)'), ('Martinica (+596)', 'Martinica (+596)'), ('Mauricio (+230)', 'Mauricio (+230)'), ('Mauritania (+222)', 'Mauritania (+222)'), ('Mayotte (+262)', 'Mayotte (+262)'), ('México (+52)', 'México (+52)'), ('Micronesia (+691)', 'Micronesia (+691)'), ('Moldavia (+373)', 'Moldavia (+373)'), ('Mónaco (+377)', 'Mónaco (+377)'), ('Mongolia (+976)', 'Mongolia (+976)'), ('Montenegro (+382)', 'Montenegro (+382)'), ('Montserrat (+1 664)', 'Montserrat (+1 664)'), ('Mozambique (+258)', 'Mozambique (+258)'), ('Myanmar (+95)', 'Myanmar (+95)'), ('Namibia (+264)', 'Namibia (+264)'), ('Nauru (+674)', 'Nauru (+674)'), ('Nepal (+977)', 'Nepal (+977)'), ('Nicaragua (+505)', 'Nicaragua (+505)'), ('Níger (+227)', 'Níger (+227)'), ('Nigeria (+234)', 'Nigeria (+234)'), ('Niue (+683)', 'Niue (+683)'), ('Noruega (+47)', 'Noruega (+47)'), ('Nueva Caledonia (+687)', 'Nueva Caledonia (+687)'), ('Nueva Zelanda (+64)', 'Nueva Zelanda (+64)'), ('Omán (+968)', 'Omán (+968)'), ('Países Bajos (+31)', 'Países Bajos (+31)'), ('Pakistán (+92)', 'Pakistán (+92)'), ('Palaos (+680)', 'Palaos (+680)'), ('Palestina (+970)', 'Palestina (+970)'), ('Panamá (+507)', 'Panamá (+507)'), ('Papúa Nueva Guinea (+675)', 'Papúa Nueva Guinea (+675)'), ('Paraguay (+595)', 'Paraguay (+595)'), ('Perú (+51)', 'Perú (+51)'), ('Polinesia Francesa (+689)', 'Polinesia Francesa (+689)'), ('Polonia (+48)', 'Polonia (+48)'), ('Portugal (+351)', 'Portugal (+351)'), ('Puerto Rico (+1 787)', 'Puerto Rico (+1 787)'), ('Reino Unido (+44)', 'Reino Unido (+44)'), ('República Centroafricana (+236)', 'República Centroafricana (+236)'), ('República Checa (+420)', 'República Checa (+420)'), ('República del Congo (+242)', 'República del Congo (+242)'), ('República Dominicana (+1 809)', 'República Dominicana (+1 809)'), ('Reunión (+262)', 'Reunión (+262)'), ('Ruanda (+250)', 'Ruanda (+250)'), ('Rumania (+40)', 'Rumania (+40)'), ('Rusia (+7)', 'Rusia (+7)'), ('Sáhara Occidental (+212)', 'Sáhara Occidental (+212)'), ('Samoa (+685)', 'Samoa (+685)'), ('Samoa Americana (+1 684)', 'Samoa Americana (+1 684)'), ('San Bartolomé (+590)', 'San Bartolomé (+590)'), ('San Cristóbal y Nieves (+1 869)', 'San Cristóbal y Nieves (+1 869)'), ('San Marino (+378)', 'San Marino (+378)'), ('San Martín (Francia) (+590)', 'San Martín (Francia) (+590)'), ('San Pedro y Miquelón (+508)', 'San Pedro y Miquelón (+508)'), ('San Vicente y las Granadinas (+1 784)', 'San Vicente y las Granadinas (+1 784)'), ('Santa Elena, Ascensión y Tristán de Acuña (+290)', 'Santa Elena, Ascensión y Tristán de Acuña (+290)'), ('Santa Lucía (+1 758)', 'Santa Lucía (+1 758)'), ('Santa Sede (Ciudad del Vaticano) (+379)', 'Santa Sede (Ciudad del Vaticano) (+379)'), ('Santo Tomé y Príncipe (+239)', 'Santo Tomé y Príncipe (+239)'), ('Senegal (+221)', 'Senegal (+221)'), ('Serbia (+381)', 'Serbia (+381)'), ('Seychelles (+248)', 'Seychelles (+248)'), ('Sierra Leona (+232)', 'Sierra Leona (+232)'), ('Singapur (+65)', 'Singapur (+65)'), ('Sint Maarten (+1 721)', 'Sint Maarten (+1 721)'), ('Siria (+963)', 'Siria (+963)'), ('Somalia (+252)', 'Somalia (+252)'), ('Sri Lanka (+94)', 'Sri Lanka (+94)'), ('Sudáfrica (+27)', 'Sudáfrica (+27)'), ('Sudán (+249)', 'Sudán (+249)'), ('Sudán del Sur (+211)', 'Sudán del Sur (+211)'), ('Suecia (+46)', 'Suecia (+46)'), ('Suiza (+41)', 'Suiza (+41)'), ('Surinam (+597)', 'Surinam (+597)'), ('Svalbard y Jan Mayen (+47)', 'Svalbard y Jan Mayen (+47)'), ('Swazilandia (+268)', 'Swazilandia (+268)'), ('Tailandia (+66)', 'Tailandia (+66)'), ('Taiwán (+886)', 'Taiwán (+886)'), ('Tanzania (+255)', 'Tanzania (+255)'), ('Tayikistán (+992)', 'Tayikistán (+992)'), ('Territorio Británico del Océano Índico (+246)', 'Territorio Británico del Océano Índico (+246)'), ('Territorios Australes Franceses (+262)', 'Territorios Australes Franceses (+262)'), ('Timor Oriental (+670)', 'Timor Oriental (+670)'), ('Togo (+228)', 'Togo (+228)'), ('Tokelau (+690)', 'Tokelau (+690)'), ('Tonga (+676)', 'Tonga (+676)'), ('Trinidad y Tobago (+1 868)', 'Trinidad y Tobago (+1 868)'), ('Túnez (+216)', 'Túnez (+216)'), ('Turkmenistán (+993)', 'Turkmenistán (+993)'), ('Turquía (+90)', 'Turquía (+90)'), ('Tuvalu (+688)', 'Tuvalu (+688)'), ('Ucrania (+380)', 'Ucrania (+380)'), ('Uganda (+256)', 'Uganda (+256)'), ('Uruguay (+598)', 'Uruguay (+598)'), ('Uzbekistán (+998)', 'Uzbekistán (+998)'), ('Vanuatu (+678)', 'Vanuatu (+678)'), ('Venezuela (+58)', 'Venezuela (+58)'), ('Vietnam (+84)', 'Vietnam (+84)'), ('Wallis y Futuna (+681)', 'Wallis y Futuna (+681)'), ('Yemen (+967)', 'Yemen (+967)'), ('Yibuti (+253)', 'Yibuti (+253)'), ('Zambia (+260)', 'Zambia (+260)'), ('Zimbabue (+263)', 'Zimbabue (+263)')], default='Colombia (+57)', max_length=50, verbose_name='Prefijo telefónico'),
        ),
    ]
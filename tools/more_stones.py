# -*- coding: utf-8 -*-
"""Stones added in seed v4, merged into build_seed.py's tables.

Names and stone groups were cross-checked against the public material lists of
stone-universe.com/materials (granite, marble, limestone, quartzite, onyx,
travertine, sandstone, slate, serpentine, porphyry) and the stone families and
quarry regions on stonelibrary.net. Only names, groups and origins are used;
no text or photos are copied from those sites. Photos still come from
Wikimedia Commons at runtime.

Same column layouts as build_seed.py / i18n_data.py.
"""

# id, fa, en, desc(fa), density, absorption, compressive, flexural, mohs, acid, standard, finishes, uses, wiki
TYPES = [
    ("porphyry", "پورفیری", "Porphyry",
     "سنگ آذرین با بلورهای درشت در زمینه‌ای ریزدانه، اغلب قرمز، بنفش یا قهوه‌ای. بسیار سخت و مقاوم است و به صورت کوبیک و تخته‌سنگ تیشه‌ای برای فرش خیابان و محوطه به کار می‌رود.",
     (2550, 2700), (0.2, 1.0), (150, 300), (15, 25), (6, 7), "none", "ASTM C615 (روش آزمون)",
     "spl,fla,san,hon", "pv,fa,fl,st", "Porphyry (geology)"),
    ("semiprecious", "سنگ نیمه‌قیمتی", "Semiprecious stone",
     "اسلب‌هایی که از قطعه‌های برش‌خوردهٔ عقیق، آمتیست، کوارتز و سنگ‌های مشابه با رزین ساخته می‌شوند. نیمه‌شفاف‌اند و برای دیوار نورپردازی‌شده، کانتر و میز لوکس به کار می‌روند. مشخصات به رزین و چیدمان قطعه‌ها بستگی دارد و اعداد تقریبی است.",
     (2400, 2650), (0.05, 0.3), (80, 200), (20, 40), (6, 7), "none", "— (اسلب کامپوزیت؛ مقادیر تقریبی)",
     "pol", "wl,ct,st", "Agate"),
]

# id | ar name | ru name | en desc | ar desc | ru desc
TYPES_TR = """
semiprecious|حجر شبه كريم|Полудрагоценный камень|Slabs made from cut pieces of agate, amethyst, quartz and similar stones set in resin. Translucent; used for backlit walls, counters and luxury tables. Properties depend on the resin and layout, so the figures are approximate.|ألواح مصنوعة من قطع مقطوعة من العقيق والجمشت والكوارتز وما شابهها مثبتة بالراتنج. شبه شفافة؛ للجدران المضاءة من الخلف والكاونترات والطاولات الفاخرة. تعتمد الخصائص على الراتنج وترتيب القطع، لذا الأرقام تقريبية.|Плиты из распиленных кусочков агата, аметиста, кварца и подобных камней на смоле. Полупрозрачные; для стен с подсветкой, стоек и роскошных столов. Свойства зависят от смолы и раскладки, поэтому цифры приблизительные.
porphyry|بورفير|Порфир|Igneous rock with large crystals set in a fine-grained matrix, often red, purple or brown. Very hard and durable; used as setts and split flags for streets and landscaping.|صخر ناري ببلورات كبيرة في أرضية دقيقة الحبيبات، غالباً أحمر أو بنفسجي أو بني. شديد الصلابة والمتانة؛ يُستخدم مكعبات وألواحاً مشقوقة للشوارع والمساحات الخارجية.|Магматическая порода с крупными кристаллами в мелкозернистой массе, часто красная, фиолетовая или коричневая. Очень твёрдая и прочная; идёт на брусчатку и колотые плиты для улиц и благоустройства.
"""

# fa | en | ar | ru
COUNTRIES = """
اوکراین|Ukraine|أوكرانيا|Украина
سوئد|Sweden|السويد|Швеция
سوئیس|Switzerland|سويسرا|Швейцария
مصر|Egypt|مصر|Египет
اسکاتلند|Scotland|اسكتلندا|Шотландия
آرژانتین|Argentina|الأرجنتين|Аргентина
ماداگاسکار|Madagascar|مدغشقر|Мадагаскар
"""

# fa | en | ar | ru
REGIONS = """
جزیرهٔ ناکسوس|Naxos Island|جزيرة ناكسوس|остров Наксос
جزیرهٔ اسکیروس|Skyros Island|جزيرة سكيروس|остров Скирос
کاوالا، مقدونیهٔ شرقی|Kavala, East Macedonia|كافالا، مقدونيا الشرقية|Кавала, Восточная Македония
سیه‌نا، توسکانی|Siena, Tuscany|سيينا، توسكانا|Сиена, Тоскана
آزیاگو، ونتو|Asiago, Veneto|أزياغو، فينيتو|Азиаго, Венето
ویچنزا، ونتو|Vicenza, Veneto|فيتشنزا، فينيتو|Виченца, Венето
لچه، پولیا|Lecce, Apulia|ليتشي، بوليا|Лечче, Апулия
ترانی، پولیا|Trani, Apulia|تراني، بوليا|Трани, Апулия
فلورانس، توسکانی|Florence, Tuscany|فلورنسا، توسكانا|Флоренция, Тоскана
پیه‌مونته|Piedmont|بيدمونت|Пьемонт
ترنتینو|Trentino|ترينتينو|Трентино
لاوانیا، لیگوریا|Lavagna, Liguria|لافانيا، ليغوريا|Лаванья, Лигурия
ماکائل، آلمریا|Macael, Almería|ماكائيل، ألميريا|Макаэль, Альмерия
پونته‌ودرا، گالیسیا|Pontevedra, Galicia|بونتيفيدرا، غاليسيا|Понтеведра, Галисия
بورگونی|Burgundy|بورغونيا|Бургундия
لورن (موز)|Lorraine (Meuse)|اللورين (ميز)|Лотарингия (Мёз)
سیدوبر، تارن|Sidobre, Tarn|سيدوبر، تارن|Сидобр, Тарн
بریتانی|Brittany|بريتاني|Бретань
لیریا|Leiria|ليريا|Лейрия
بورسا|Bursa|بورصة|Бурса
آنتالیا|Antalya|أنطاليا|Анталья
الازیغ|Elazığ|ألازيغ|Элязыг
موغلا|Muğla|موغلا|Мугла
مانیسا|Manisa|مانيسا|Маниса
سیواس|Sivas|سيواس|Сивас
دیاربکر|Diyarbakır|ديار بكر|Диярбакыр
حاجی‌آباد، استان مرکزی|Hajiabad, Markazi|حاجي آباد، المحافظة المركزية|Хаджиабад, Меркези
تکاب، آذربایجان غربی|Takab, West Azerbaijan|تكاب، أذربيجان الغربية|Текаб, Западный Азербайджан
خرمدره، زنجان|Khorramdarreh, Zanjan|خرمدره، زنجان|Хоррамдарре, Зенджан
هند|India|الهند|Индия
ژیتومیر|Zhytomyr|جيتومير|Житомир
اسکونه|Skåne|سكونه|Сконе
بوهوسلن|Bohuslän|بوهوسلان|Бохуслен
یمتلند|Jämtland|يمتلاند|Емтланд
اوپدال، تروندلاگ|Oppdal, Trøndelag|أوبدال، تروندلاغ|Оппдал, Трёнделаг
آلتا، فینمارک|Alta, Finnmark|ألتا، فينمارك|Альта, Финнмарк
اوتا، اوپلاند|Otta, Oppland|أوتا، أوبلاند|Отта, Оппланн
ایده‌فیورد|Iddefjord|إيدفيورد|Иддефьорд
کورو، پیرکانما|Kuru, Pirkanmaa|كورو، بيركانما|Куру, Пирканмаа
گراوبوندن|Graubünden|غراوبوندن|Граубюнден
داکوتای جنوبی|South Dakota|داكوتا الجنوبية|Южная Дакота
بتل، ورمونت|Bethel, Vermont|بيثيل، فيرمونت|Бетел, Вермонт
تگزاس|Texas|تكساس|Техас
کاتس‌وولد، گلاسترشر|Cotswolds, Gloucestershire|كوتسوولد، غلوسترشير|Котсуолд, Глостершир
کامبریا|Cumbria|كمبريا|Камбрия
دامفریز|Dumfries|دمفريز|Дамфрис
کوه‌های جلاله|Galala Mountains|جبال الجلالة|горы Галала
سینا|Sinai|سيناء|Синай
المنیا|Minya|المنيا|Минья
ریو گرانده دو سول|Rio Grande do Sul|ريو غراندي دو سول|Риу-Гранди-ду-Сул
ماداگاسکار|Madagascar|مدغشقر|Мадагаскар
چوبوت، پاتاگونیا|Chubut, Patagonia|تشوبوت، باتاغونيا|Чубут, Патагония
صحرای شرقی (جبل دخان)|Eastern Desert (Gebel Dokhan)|الصحراء الشرقية (جبل الدخان)|Восточная пустыня (Джебель-Духан)
لاکونیا، پلوپونز|Laconia, Peloponnese|لاكونيا، البيلوبونيز|Лакония, Пелопоннес
کیپ شمالی|Northern Cape|الكاب الشمالية|Северо-Капская провинция
"""

# id|fa|en|aliases|type|color|pattern|region(fa)|country(fa)|finishes|uses|description(fa)|wiki
STONES = """
white_naxos|مرمر سفید ناکسوس|White Naxos|Naxos marble, ناکسوس|marble|wh|grain|جزیرهٔ ناکسوس|یونان|||مرمر سفید درشت‌بلور و براق جزیرهٔ ناکسوس؛ از دوران باستان برای پیکره و معماری استخراج می‌شود.|
skyros|مرمر اسکیروس|Skyros|Skiros, Breccia Skyros|marble|ye|cloud|جزیرهٔ اسکیروس|یونان|||مرمر برشی با قطعه‌های زرد، کرم و قرمز در زمینهٔ تیره؛ سنگ تزیینی کلاسیک یونان.|
kavala_white|مرمر سفید کاوالا|Kavala White|Kavala marble|marble|wh|vein|کاوالا، مقدونیهٔ شرقی|یونان|||مرمر سفید با رگه‌های ظریف خاکستری از شمال یونان؛ برای کف و دیوار.|
ariston|آریستون|Ariston|Ariston white, Drama white|marble|wh|cloud|دراما|یونان|||مرمر سفید شیری با ابرهای ملایم خاکستری؛ از مرمرهای پرمصرف یونان.|
giallo_siena|جیالو سیه‌نا|Giallo Siena|Siena yellow, زرد سینا|marble|ye|vein|سیه‌نا، توسکانی|ایتالیا|||مرمر زرد طلایی با رگه‌های بنفش و قهوه‌ای؛ در کلیساهای تاریخی توسکانی دیده می‌شود.|
paonazzo|پاونازو|Paonazzo|Pavonazzo|marble|wh|vein|کارارا، توسکانی|ایتالیا|||مرمر سفید کارارا با رگه‌های درشت بنفش و قهوه‌ای؛ از گونه‌های کمیاب و گران.|
fior_di_pesco|فیور دی پسکو کارنیکو|Fior di Pesco Carnico|Fior di Pesco|marble|gy|vein|فریولی|ایتالیا|||مرمر خاکستری تا بنفش با رگه‌های سفید و صورتی که نامش «شکوفهٔ هلو» است.|
breccia_pernice|برشیا پرنیچه|Breccia Pernice|Pernice|marble|pk|cloud|ورونا، ونتو|ایتالیا|||سنگ برشی صورتی و قرمز با قطعه‌های گرد؛ برای کف و تزیینات کلاسیک.|
rosa_portogallo|رزا پرتغال|Rosa Portogallo|Rosa Estremoz, Rosa Aurora, صورتی پرتغال|marble|pk|vein|استرموز، آلنتژو|پرتغال|||مرمر صورتی ملایم با رگه‌های کرم و قرمز از استرموز.|
blanco_macael|سفید ماکائل|Blanco Macael|Macael white|marble|wh|vein|ماکائل، آلمریا|اسپانیا|||مرمر سفید با رگه‌های خاکستری از مهم‌ترین قطب سنگ اسپانیا؛ در کاخ الحمرا هم به کار رفته است.|
amarillo_triana|آماریلو تریانا|Amarillo Triana|Triana yellow|marble|ye|vein|ماکائل، آلمریا|اسپانیا|||مرمر زرد کرم با رگه‌های طلایی و قهوه‌ای.|
elazig_cherry|الازیغ گیلاسی|Elazig Cherry|Rosso Levante, Elazig Visne|marble|rd|vein|الازیغ|ترکیه|||مرمر قرمز آلبالویی با رگه‌های سفید و خاکستری؛ از مرمرهای رنگی مشهور ترکیه.|
milas_white|مرمر سفید میلاس|Milas White|Mugla white, Milas marble|marble|wh|vein|موغلا|ترکیه|||مرمر سفید تا خاکستری روشن از منطقهٔ میلاس؛ بخش بزرگی از صادرات مرمر ترکیه.|
milas_lilac|میلاس لیلاک|Milas Lilac|Lilac marble, Mugla lilac|marble|wh|vein|موغلا|ترکیه|||مرمر سفید با رگه‌های بنفش ملایم از منطقهٔ میلاس.|
akhisar_beige|بژ آخیسار|Akhisar Beige|Akhisar marble|marble|cr|cloud|مانیسا|ترکیه|||مرمر بژ کرم با زمینهٔ یکنواخت از منطقهٔ مانیسا.|
fantasy_brown|فانتزی براون|Fantasy Brown|Fantasy brown marble|dolomitic|bn|band|راجستان|هند|||مرمر دولومیتی با نوارهای موجی خاکستری، قهوه‌ای و کرم؛ سخت‌تر از مرمر معمولی و برای صفحهٔ کابینت محبوب.|
rainforest_brown|رین‌فارست|Rainforest Brown|Rainforest green, Bidasar|marble|bn|vein|راجستان|هند|||مرمر قهوه‌ای سبز با رگه‌هایی شبیه شاخه و برگ درخت.|
forest_green|فارست گرین|Forest Green|Indian green marble, Verde Guatemala India|serpentinite|gn|vein|اودایپور، راجستان|هند|||سنگ سبز تیره با رگه‌های روشن از اودایپور؛ در بازار با نام مرمر سبز هندی فروخته می‌شود.|
spider_green|اسپایدر گرین|Spider Green|Spider green marble|serpentinite|gn|vein|اودایپور، راجستان|هند|||سنگ سبز با شبکهٔ رگه‌های سفید و سبز روشن شبیه تار عنکبوت.|
trani|سنگ ترانی|Trani|Pietra di Trani, Biancone di Trani|limestone|cr|uni|ترانی، پولیا|ایتالیا|||سنگ آهک متراکم کرم تا عاجی از جنوب ایتالیا؛ کلیسای جامع ترانی با آن ساخته شده است.|
pietra_vicenza|سنگ ویچنزا|Pietra di Vicenza|Vicenza stone|limestone|cr|uni|ویچنزا، ونتو|ایتالیا|||سنگ آهک نرم و روشن که آثار پالادیو با آن ساخته شده‌اند؛ برای حجاری و نما.|
lecce_stone|سنگ لچه|Lecce Stone|Pietra Leccese|limestone|ye|uni|لچه، پولیا|ایتالیا|||سنگ آهک نرم زرد عسلی که حجاری‌های باروک لچه با آن ساخته شده است.|Lecce stone
rosa_perlino|رزا پرلینو|Rosa Perlino|Perlino rosato|limestone|pk|cloud|آزیاگو، ونتو|ایتالیا|||سنگ آهک متراکم صورتی با ابرهای روشن؛ در بازار به نام مرمر فروخته می‌شود.|
rosa_asiago|رزا آزیاگو|Rosa Asiago|Asiago|limestone|pk|uni|آزیاگو، ونتو|ایتالیا|||سنگ آهک صورتی کم‌رنگ و یکنواخت از فلات آزیاگو.|
solnhofen|سنگ سولنهوفن|Solnhofen|Solnhofen limestone, Jura Marble plates|limestone|cr|uni|باواریا|آلمان|||سنگ آهک ورقه‌ای بسیار ریزدانه که فسیل آرکئوپتریکس در آن یافت شد؛ برای کف و چاپ سنگی.|Solnhofen Limestone
comblanchien|کومبلانشین|Comblanchien|Pierre de Bourgogne|limestone|cr|uni|بورگونی|فرانسه|||سنگ آهک متراکم بژ صورتی که جلا می‌پذیرد؛ کف فرودگاه‌ها و ساختمان‌های عمومی فرانسه.|
massangis|ماسانژی|Massangis|Massangis roche|limestone|cr|pore|بورگونی|فرانسه|||سنگ آهک بژ با ذرات صدفی ریز؛ برای نما و کف در فرانسه رایج است.|
savonnieres|ساوونیر|Savonnières|Savonnieres|limestone|cr|pore|لورن (موز)|فرانسه|||سنگ آهک اولیتی سبک و متخلخل؛ برای حجاری و مرمت بناهای تاریخی.|
euville|اوویل|Euville|Pierre d'Euville|limestone|cr|pore|لورن (موز)|فرانسه|||سنگ آهک کرینوئیدی کرم با بافت بلورین؛ در پل‌ها و بناهای پاریس به کار رفته است.|
moca_creme|موکا کرم|Moca Creme|Moca Cream, Mocca Cream|limestone|cr|band|لیریا|پرتغال|||سنگ آهک کرم با نوارهای ریز موازی؛ از پرفروش‌ترین سنگ‌های پرتغال.|
bursa_beige|بژ بورسا|Bursa Beige|Bursa light beige|limestone|cr|uni|بورسا|ترکیه|||سنگ آهک بژ روشن و یکنواخت از شمال غرب ترکیه.|
limra|لیمرا|Limra|Limra limestone|limestone|cr|pore|آنتالیا|ترکیه|||سنگ آهک کرم روشن با حفره‌های ریز؛ برای نمای ساختمان‌های مدرن.|
nero_belgio|سیاه بلژیک|Nero Belgio|Belgian Black, Noir Belge|limestone|bk|uni|منطقهٔ والونی|بلژیک|||سنگ آهک سیاه یکدست و براق؛ از سیاه‌ترین سنگ‌های جهان برای تزیینات و قرنیز.|
lueders|لودرز|Lueders|Lueders limestone|limestone|cr|uni|تگزاس|آمریکا|||سنگ آهک کرم تا خاکستری لایه‌ای؛ برای سنگ‌چین، نما و کف محوطه.|
cotswold|سنگ کاتس‌وولد|Cotswold Stone|Cotswold limestone|limestone|ye|uni|کاتس‌وولد، گلاسترشر|انگلستان|||سنگ آهک اولیتی زرد عسلی که روستاهای تاریخی کاتس‌وولد با آن ساخته شده‌اند.|
galala|جلاله|Galala|Galala marble, Galala beige|limestone|cr|uni|کوه‌های جلاله|مصر|||سنگ آهک بژ کرم متراکم که با نام «مرمر جلاله» فروخته می‌شود؛ از پرمصرف‌ترین سنگ‌های خاورمیانه.|
sinai_pearl|سینا پرل|Sinai Pearl|Sinai beige|limestone|cr|cloud|سینا|مصر|||سنگ آهک بژ با فسیل‌های ریز و ابرهای روشن.|
sunny_menia|سانی منیا|Sunny Menia|Sunny, Menia|limestone|ye|uni|المنیا|مصر|||سنگ آهک زرد کرم روشن و ارزان؛ برای کف و نما در کشورهای عربی رایج است.|
pietra_serena|پیترا سرنا|Pietra Serena|Florentine sandstone|sandstone|gy|uni|فلورانس، توسکانی|ایتالیا|||ماسه‌سنگ خاکستری آبی که ستون‌ها و قاب‌های معماری رنسانس فلورانس با آن ساخته شده‌اند.|Pietra serena
locharbriggs|لوخاربریگز|Locharbriggs|Locharbriggs red sandstone|sandstone|rd|uni|دامفریز|اسکاتلند|||ماسه‌سنگ قرمز اسکاتلند که در ساختمان‌های ویکتوریایی بسیاری از شهرها دیده می‌شود.|
volga_blue|ولگا بلو|Volga Blue|Labradorite Volga Blue|granite|bl|grain|ژیتومیر|اوکراین|||لابرادوریت تیره با بلورهای درشت که زیر نور آبی می‌درخشند.|
vizag_blue|ویزاگ بلو|Vizag Blue|Vizag|granite|bl|grain|آندرا پرادش|هند|||گرانیت آبی تیره تا خاکستری با دانه‌های درشت.|
viscount_white|ویسکانت وایت|Viscount White|Viscont white|granite|wh|band|هند|هند|||گرانیت سفید با نوارهای موجی خاکستری و سیاه.|
silver_pearl|سیلور پرل|Silver Pearl|Silver pearl granite|granite|gy|grain|هند|هند|||گرانیت خاکستری نقره‌ای با دانه‌های درخشان.|
madura_gold|مادورا گلد|Madura Gold|Madurai gold|granite|ye|grain|تامیل نادو|هند|||گرانیت طلایی با دانه‌های قهوه‌ای و سیاه.|
kashmir_gold|کشمیر گلد|Kashmir Gold|Kashmir gold granite|granite|ye|grain|تامیل نادو|هند|||گرانیت کرم طلایی با نقطه‌های قرمز گارنت و دانه‌های تیره.|
andromeda_white|آندرومدا وایت|Andromeda White|Andromeda|granite|wh|grain|هند|هند|||گرانیت سفید با دانه‌های خاکستری و صورتی ملایم.|
serizzo|سریتزو آنتیگوریو|Serizzo Antigorio|Serizzo, Antigorio|granite|gy|band|پیه‌مونته|ایتالیا|||سنگ گنیسی خاکستری با نوارهای موازی تیره؛ برای کف، پله و پیاده‌رو در شمال ایتالیا.|
rosa_baveno|رزا باونو|Rosa Baveno|Baveno pink|granite|pk|grain|پیه‌مونته|ایتالیا|||گرانیت صورتی درشت‌دانه از کنار دریاچهٔ ماجوره.|
bianco_montorfano|بیانکو مونتورفانو|Bianco Montorfano|Montorfano white|granite|wh|grain|پیه‌مونته|ایتالیا|||گرانیت سفید با دانه‌های سیاه میکا؛ در بناهای میلان به کار رفته است.|
rosa_limbara|رزا لیمبارا|Rosa Limbara|Limbara pink, Rosa Sardo|granite|pk|grain|ساردینیا|ایتالیا|||گرانیت صورتی روشن با دانه‌های خاکستری از کوه لیمبارا.|
porfido_trentino|پورفیری ترنتینو|Porfido Trentino|Trentino porphyry, Porfido|porphyry|rd|grain|ترنتینو|ایتالیا|||پورفیری قرمز قهوه‌ای تا بنفش؛ مشهورترین سنگ کوبیک برای فرش خیابان و میدان.|
porfido_argentino|پورفیری آرژانتین|Argentine Porphyry|Porfido Argentino, Patagonian porphyry|porphyry|bn|grain|چوبوت، پاتاگونیا|آرژانتین|||پورفیری قهوه‌ای قرمز تا بنفش پاتاگونیا؛ برای کوبیک و فرش محوطه.|
porfido_rosso_antico|پورفیری قرمز مصری|Imperial Porphyry|Porfido Rosso Antico, Egyptian red porphyry|porphyry|pu|grain|صحرای شرقی (جبل دخان)|مصر|||پورفیری ارغوانی با بلورهای ریز سفید که امپراتوران روم برای ستون و پیکره به کار می‌بردند.|
porfido_verde_antico|پورفیری سبز یونانی|Green Porphyry|Porfido Verde Antico, Lapis Lacedaemonius|porphyry|gn|grain|لاکونیا، پلوپونز|یونان|||پورفیری سبز تیره با بلورهای سبز روشن؛ سنگ تزیینی کلاسیک روم و یونان.|
rosso_vanga|روسو وانگا|Rosso Vanga|Vanga Red|granite|rd|grain|اسکونه|سوئد|||گرانیت قرمز درشت‌دانه با بلورهای آبی کوارتز.|
bohus_red|بوهوس رد|Bohus Red|Bohus granite|granite|rd|grain|بوهوسلن|سوئد|||گرانیت قرمز سوئد برای نما، سنگ قبر و محوطه.|
iddefjord|ایده‌فیورد|Iddefjord|Iddefjord granite|granite|gy|grain|ایده‌فیورد|نروژ|||گرانیت خاکستری روشن یکنواخت برای فرش و جدول خیابان.|
emerald_pearl|امرالد پرل|Emerald Pearl|Larvikite Emerald Pearl|granite|gn|grain|لارویک|نروژ|||لارویکیت سبز تیره با بلورهای درخشان رنگین‌کمانی.|Larvikite
kuru_grey|کورو گری|Kuru Grey|Kuru granite|granite|gy|grain|کورو، پیرکانما|فنلاند|||گرانیت خاکستری ریزدانه و یکنواخت فنلاند.|
andeer|آندیر|Andeer|Andeer granite, Andeerer|granite|gn|band|گراوبوندن|سوئیس|||گنیس سبز خاکستری سوئیس با نوارهای ظریف؛ برای کف و پله.|
gris_mondariz|گری موندریز|Gris Mondariz|Mondariz grey|granite|gy|grain|پونته‌ودرا، گالیسیا|اسپانیا|||گرانیت خاکستری روشن گالیسیا؛ پرمصرف برای نما و کف.|
tarn_granite|گرانیت تارن|Tarn Granite|Sidobre granite|granite|gy|grain|سیدوبر، تارن|فرانسه|||گرانیت خاکستری آبی از مهم‌ترین قطب گرانیت فرانسه.|
lanhelin|لانلن|Lanhelin|Lanhelin granite|granite|gy|grain|بریتانی|فرانسه|||گرانیت آبی خاکستری بریتانی برای ساختمان و سنگ قبر.|
giallo_veneziano|جیالو ونزیانو|Giallo Veneziano|Venetian Gold|granite|ye|grain|اسپیریتو سانتو|برزیل|||گرانیت زرد طلایی با نقطه‌های قهوه‌ای و قرمز؛ برای صفحهٔ کابینت.|
g687|گرانیت G687|G687|Peach Red|granite|pk|grain|فوجیان|چین|||گرانیت صورتی هلویی ارزان برای کف و محوطه.|
g640|گرانیت G640|G640|Bianco Sardo China|granite|gy|grain|فوجیان|چین|||گرانیت خاکستری با دانه‌های سیاه درشت؛ پرمصرف برای محوطه.|
dakota_mahogany|داکوتا ماهاگونی|Dakota Mahogany|Dakota mahogany granite|granite|rd|grain|داکوتای جنوبی|آمریکا|||گرانیت قهوه‌ای قرمز با دانه‌های سیاه؛ برای بناهای یادبود.|
bethel_white|بتل وایت|Bethel White|Bethel granite|granite|wh|grain|بتل، ورمونت|آمریکا|||از سفیدترین گرانیت‌های جهان با دانه‌های ریز خاکستری.|
khorramdarreh|گرانیت خرمدره|Khorramdarreh Granite|خرمدره، Khorramdareh|granite|gy|grain|خرمدره، زنجان|ایران|||گرانیت خاکستری سفید با دانه‌های سیاه؛ پرمصرف برای کف و پله در ایران.|
oppdal|کوارتزیت اوپدال|Oppdal Quartzite|Oppdal, Oppdalquarzite|quartzite|gy|band|اوپدال، تروندلاگ|نروژ|||کوارتزیت خاکستری نقره‌ای ورقه‌ای با سطح شکاف طبیعی؛ برای کف و دیوار.|
offerdal|کوارتزیت اوفردال|Offerdal Quartzite|Offerdal|quartzite|gy|band|یمتلند|سوئد|||کوارتزیت خاکستری ورقه‌ای سوئد با سطح طبیعی.|
alta_quartzite|کوارتزیت آلتا|Alta Quartzite|Alta, Altaquarzite|quartzite|gy|band|آلتا، فینمارک|نروژ|||کوارتزیت خاکستری از شمال نروژ که به صورت ورقه‌های نازک جدا می‌شود؛ برای بام و کف.|
hajiabad|تراورتن حاجی‌آباد|Hajiabad Travertine|حاجی آباد، Haji Abad|travertine|cr|pore|حاجی‌آباد، استان مرکزی|ایران|||تراورتن سفید تا کرم روشن؛ از تراورتن‌های پرمصرف نما در ایران.|
takab|تراورتن تکاب|Takab Travertine|تکاب|travertine|cr|band|تکاب، آذربایجان غربی|ایران|||تراورتن کرم تا زرد با لایه‌بندی موجی از شمال غرب ایران.|
azarshahr_chocolate|تراورتن شکلاتی آذرشهر|Azarshahr Chocolate Travertine|شکلاتی آذرشهر، Chocolate travertine|travertine|bn|band|آذرشهر، آذربایجان شرقی|ایران|||تراورتن قهوه‌ای شکلاتی با نوارهای روشن و تیره.|
sivas_yellow|زرد سیواس|Sivas Yellow|Sivas travertine|travertine|ye|band|سیواس|ترکیه|||تراورتن زرد طلایی با نوارهای قهوه‌ای از مرکز ترکیه.|
honey_onyx|اونیکس عسلی|Persian Honey Onyx|Onyx Miele, Honey onyx|onyx|ye|band|ایران|ایران|||مرمر سنگ زرد عسلی تا نارنجی با نوارهای موجی؛ زیر نور پشت جلوهٔ گرمی دارد.|
otta_slate|اسلیت اوتا|Otta Slate|Otta, Otta Pillarguri|slate|gy|uni|اوتا، اوپلاند|نروژ|||سنگ فیلیت خاکستری تیره با دانه‌های ریز درخشان؛ بسیار مقاوم برای کف و نما.|
ardesia_genovese|اردزیای جنوا|Ardesia Genovese|Ardesia di Lavagna, Liguria slate|slate|bk|uni|لاوانیا، لیگوریا|ایتالیا|||اسلیت سیاه لیگوریا که از قدیم برای میز بیلیارد، تخته‌سیاه و بام استفاده می‌شود.|
deoli_green|اسلیت سبز دئولی|Deoli Green|Deoli slate|slate|gn|uni|راجستان|هند|||اسلیت سبز روشن هند برای کف و دیوار.|
burlington|اسلیت برلینگتون|Burlington Slate|Westmorland green slate|slate|gn|uni|کامبریا|انگلستان|||اسلیت سبز روشن تا زیتونی شمال انگلستان؛ برای بام، کف و نما.|
diyarbakir_basalt|بازالت دیاربکر|Diyarbakir Basalt|Diyarbakır black stone|basalt|bk|pore|دیاربکر|ترکیه|||بازالت سیاه متخلخل که دیوارهای تاریخی دیاربکر با آن ساخته شده‌اند.|
blue_agate|عقیق آبی|Blue Agate|Agata blu, Agate slab|semiprecious|bl|band|ریو گرانده دو سول|برزیل|||اسلب نیمه‌شفاف از برش‌های عقیق آبی با حلقه‌های رنگی؛ برای دیوار و کانتر نورپردازی‌شده.|Agate
amethyst|آمتیست|Amethyst|Ametista, Amethyst slab|semiprecious|pu|cloud|ریو گرانده دو سول|برزیل|||اسلب بنفش از قطعه‌های آمتیست؛ زیر نور پشت درخشش بنفش دارد.|Amethyst
rose_quartz|رز کوارتز|Rose Quartz|Quarzo rosa, کوارتز صورتی|semiprecious|pk|cloud|ماداگاسکار|ماداگاسکار|||اسلب صورتی نیمه‌شفاف از قطعه‌های کوارتز صورتی.|Rose quartz
tigers_eye|چشم ببر|Tiger's Eye|Tiger eye, Occhio di tigre|semiprecious|bn|band|کیپ شمالی|آفریقای جنوبی|||اسلب قهوه‌ای طلایی با درخشش ابریشمی از قطعه‌های سنگ چشم ببر.|Tiger's eye
petrified_wood|چوب سنگ‌شده|Petrified Wood|Legno fossile, فسیل چوب|semiprecious|bn|band|ماداگاسکار|ماداگاسکار|||اسلب از برش‌های چوب فسیل‌شده با حلقه‌های رشد درخت؛ برای میز و دیوار.|Petrified wood
"""

# id | ar name | ru name | en desc | ar desc | ru desc
STONES_TR = """
white_naxos|رخام ناكسوس الأبيض|Белый мрамор Наксос|Coarse-crystalled, lustrous white marble from Naxos, quarried since antiquity for sculpture and architecture.|رخام أبيض لامع كبير البلورات من جزيرة ناكسوس، يُستخرج منذ العصور القديمة للنحت والعمارة.|Крупнокристаллический блестящий белый мрамор с Наксоса; добывается с античности для скульптуры и архитектуры.
skyros|رخام سكيروس|Скирос|Brecciated marble with yellow, cream and red fragments in a darker matrix; a classic Greek decorative stone.|رخام بريشي بقطع صفراء وكريمية وحمراء في أرضية داكنة؛ حجر زخرفي يوناني كلاسيكي.|Брекчиевый мрамор с жёлтыми, кремовыми и красными обломками в тёмной массе; классический греческий декоративный камень.
kavala_white|رخام كافالا الأبيض|Белый мрамор Кавала|White marble with fine grey veins from northern Greece; for floors and walls.|رخام أبيض بعروق رمادية رفيعة من شمال اليونان؛ للأرضيات والجدران.|Белый мрамор с тонкими серыми прожилками из северной Греции; для полов и стен.
ariston|أريستون|Аристон|Milky white marble with soft grey clouds; one of Greece's most used marbles.|رخام أبيض حليبي بغيوم رمادية خفيفة؛ من أكثر أنواع الرخام اليوناني استخداماً.|Молочно-белый мрамор с мягкими серыми облаками; один из самых используемых греческих мраморов.
giallo_siena|جيالو سيينا|Джалло Сиена|Golden-yellow marble with purple and brown veins, seen in Tuscany's historic churches.|رخام أصفر ذهبي بعروق بنفسجية وبنية، يُرى في كنائس توسكانا التاريخية.|Золотисто-жёлтый мрамор с фиолетовыми и коричневыми прожилками, встречается в старинных церквях Тосканы.
paonazzo|باونازو|Паонаццо|Carrara white marble with bold purple and brown veins; rare and costly.|رخام كرارا أبيض بعروق بنفسجية وبنية عريضة؛ نادر ومكلف.|Белый каррарский мрамор с крупными фиолетовыми и коричневыми прожилками; редкий и дорогой.
fior_di_pesco|فيور دي بيسكو كارنيكو|Фьор ди Песко Карнико|Grey to purple marble with white and pink veins; its name means "peach blossom".|رخام رمادي إلى بنفسجي بعروق بيضاء ووردية؛ اسمه يعني «زهرة الخوخ».|Серо-фиолетовый мрамор с белыми и розовыми прожилками; название значит «цветок персика».
breccia_pernice|بريشيا بيرنيتشي|Брекча Перниче|Pink and red breccia with rounded fragments; for floors and classical ornament.|بريشيا وردية وحمراء بقطع مستديرة؛ للأرضيات والزخارف الكلاسيكية.|Розово-красная брекчия с округлыми обломками; для полов и классического декора.
rosa_portogallo|روزا البرتغال|Роза Португалия|Soft pink marble with cream and red veins from Estremoz.|رخام وردي ناعم بعروق كريمية وحمراء من إستريموز.|Нежно-розовый мрамор с кремовыми и красными прожилками из Эштремоша.
blanco_macael|ماكائيل الأبيض|Бланко Макаэль|White marble with grey veins from Spain's main stone centre; also used in the Alhambra.|رخام أبيض بعروق رمادية من أهم مراكز الحجر في إسبانيا؛ استُخدم أيضاً في قصر الحمراء.|Белый мрамор с серыми прожилками из главного каменного центра Испании; использовался и в Альгамбре.
amarillo_triana|أماريو تريانا|Амарильо Триана|Cream-yellow marble with golden and brown veins.|رخام أصفر كريمي بعروق ذهبية وبنية.|Кремово-жёлтый мрамор с золотистыми и коричневыми прожилками.
elazig_cherry|ألازيغ الكرزي|Элязыг Вишня|Cherry-red marble with white and grey veins; a well-known Turkish coloured marble.|رخام أحمر كرزي بعروق بيضاء ورمادية؛ من أشهر أنواع الرخام الملون التركي.|Вишнёво-красный мрамор с белыми и серыми прожилками; известный турецкий цветной мрамор.
milas_white|رخام ميلاس الأبيض|Белый мрамор Милас|White to light grey marble from the Milas area; a large share of Turkey's marble exports.|رخام أبيض إلى رمادي فاتح من منطقة ميلاس؛ جزء كبير من صادرات الرخام التركي.|Белый или светло-серый мрамор из района Милас; значительная часть турецкого экспорта мрамора.
milas_lilac|ميلاس ليلك|Милас Лилак|White marble with soft lilac veins from the Milas area.|رخام أبيض بعروق ليلكية ناعمة من منطقة ميلاس.|Белый мрамор с мягкими сиреневыми прожилками из района Милас.
akhisar_beige|بيج أكحصار|Акхисар Беж|Creamy beige marble with an even base from the Manisa area.|رخام بيج كريمي بأرضية متجانسة من منطقة مانيسا.|Кремово-бежевый мрамор с ровным фоном из района Маниса.
fantasy_brown|فانتازي براون|Фэнтези Браун|Dolomitic marble with wavy grey, brown and cream bands; harder than ordinary marble and popular for countertops.|رخام دولوميتي بأشرطة متموجة رمادية وبنية وكريمية؛ أقسى من الرخام العادي ومحبوب لأسطح المطابخ.|Доломитовый мрамор с волнистыми серыми, коричневыми и кремовыми полосами; твёрже обычного мрамора, популярен для столешниц.
rainforest_brown|رين فورست|Рейнфорест|Brown-green marble with veins like tree branches and leaves.|رخام بني مخضر بعروق تشبه أغصان الشجر وأوراقه.|Коричнево-зелёный мрамор с прожилками, похожими на ветви и листья.
forest_green|فورست غرين|Форест Грин|Dark green stone with light veins from Udaipur, sold as Indian green marble.|حجر أخضر داكن بعروق فاتحة من أودايبور، يُباع باسم الرخام الهندي الأخضر.|Тёмно-зелёный камень со светлыми прожилками из Удайпура; продаётся как индийский зелёный мрамор.
spider_green|سبايدر غرين|Спайдер Грин|Green stone with a web of white and pale green veins.|حجر أخضر بشبكة من العروق البيضاء والخضراء الفاتحة.|Зелёный камень с паутиной белых и светло-зелёных прожилок.
trani|حجر تراني|Трани|Dense cream to ivory limestone from southern Italy; Trani Cathedral is built of it.|حجر جيري كثيف كريمي إلى عاجي من جنوب إيطاليا؛ بُنيت منه كاتدرائية تراني.|Плотный кремово-слоновый известняк с юга Италии; из него построен собор в Трани.
pietra_vicenza|حجر فيتشنزا|Камень Виченцы|Soft, light limestone used in Palladio's buildings; for carving and facades.|حجر جيري فاتح لين استُخدم في مباني بالاديو؛ للنحت والواجهات.|Мягкий светлый известняк, из которого строил Палладио; для резьбы и фасадов.
lecce_stone|حجر ليتشي|Леччезе|Soft honey-yellow limestone of Lecce's Baroque carvings.|حجر جيري لين أصفر عسلي صُنعت منه منحوتات ليتشي الباروكية.|Мягкий медово-жёлтый известняк барочной резьбы Лечче.
rosa_perlino|روزا بيرلينو|Роза Перлино|Dense pink limestone with light clouds, traded as marble.|حجر جيري وردي كثيف بغيوم فاتحة، يُتداول باسم رخام.|Плотный розовый известняк со светлыми облаками; продаётся как мрамор.
rosa_asiago|روزا أزياغو|Роза Азиаго|Pale, even pink limestone from the Asiago plateau.|حجر جيري وردي باهت متجانس من هضبة أزياغو.|Бледно-розовый ровный известняк с плато Азиаго.
solnhofen|حجر سولنهوفن|Зольнхофен|Very fine-grained platy limestone where Archaeopteryx was found; for floors and lithography.|حجر جيري صفائحي دقيق جداً عُثر فيه على الأركيوبتركس؛ للأرضيات والطباعة الحجرية.|Очень тонкозернистый плитчатый известняк, где нашли археоптерикса; для полов и литографии.
comblanchien|كومبلانشيان|Комбланшьен|Dense pinkish-beige limestone that takes a polish; floors of French airports and public buildings.|حجر جيري كثيف بيج مائل للوردي يقبل التلميع؛ أرضيات مطارات ومبانٍ عامة في فرنسا.|Плотный розовато-бежевый известняк, хорошо полируется; полы французских аэропортов и общественных зданий.
massangis|ماسانجي|Массанжи|Beige limestone with tiny shell fragments; common for facades and floors in France.|حجر جيري بيج بشظايا صدفية صغيرة؛ شائع للواجهات والأرضيات في فرنسا.|Бежевый известняк с мелкими обломками раковин; распространён во Франции для фасадов и полов.
savonnieres|سافونيير|Савоньер|Light, porous oolitic limestone for carving and restoring historic buildings.|حجر جيري أوليتي خفيف ومسامي للنحت وترميم المباني التاريخية.|Лёгкий пористый оолитовый известняк для резьбы и реставрации исторических зданий.
euville|أوفيل|Эвиль|Cream crinoidal limestone with a crystalline texture, used in Paris bridges and monuments.|حجر جيري كرينويدي كريمي بملمس بلوري، استُخدم في جسور ومعالم باريس.|Кремовый криноидный известняк с кристаллической текстурой; использован в мостах и памятниках Парижа.
moca_creme|موكا كريم|Мока Крем|Cream limestone with fine parallel bands; one of Portugal's best-selling stones.|حجر جيري كريمي بأشرطة متوازية دقيقة؛ من أكثر الأحجار البرتغالية مبيعاً.|Кремовый известняк с тонкими параллельными полосами; один из самых продаваемых португальских камней.
bursa_beige|بيج بورصة|Бурса Беж|Light, even beige limestone from north-western Turkey.|حجر جيري بيج فاتح متجانس من شمال غرب تركيا.|Светлый ровный бежевый известняк с северо-запада Турции.
limra|ليمرا|Лимра|Light cream limestone with fine pores; for modern facades.|حجر جيري كريمي فاتح بمسام دقيقة؛ للواجهات الحديثة.|Светло-кремовый известняк с мелкими порами; для современных фасадов.
nero_belgio|الأسود البلجيكي|Неро Бельджо|Uniform glossy black limestone; one of the blackest stones in the world, for ornament and mouldings.|حجر جيري أسود لامع متجانس؛ من أشد الأحجار سواداً في العالم، للزخارف والأفاريز.|Однородный блестящий чёрный известняк; один из самых чёрных камней в мире, для декора и карнизов.
lueders|لودرز|Людерс|Layered cream to grey limestone; for walling, facades and landscaping.|حجر جيري طبقي كريمي إلى رمادي؛ للجدران والواجهات وتنسيق الحدائق.|Слоистый кремово-серый известняк; для кладки, фасадов и благоустройства.
cotswold|حجر كوتسوولد|Котсуолдский камень|Honey-yellow oolitic limestone of the historic Cotswold villages.|حجر جيري أوليتي أصفر عسلي بُنيت منه قرى كوتسوولد التاريخية.|Медово-жёлтый оолитовый известняк исторических деревень Котсуолда.
galala|جلالة|Галала|Dense cream-beige limestone sold as "Galala marble"; one of the most used stones in the Middle East.|حجر جيري كثيف بيج كريمي يُباع باسم «رخام الجلالة»؛ من أكثر الأحجار استخداماً في الشرق الأوسط.|Плотный кремово-бежевый известняк, продаётся как «мрамор Галала»; один из самых используемых камней Ближнего Востока.
sinai_pearl|سيناء بيرل|Синай Перл|Beige limestone with small fossils and light clouds.|حجر جيري بيج بأحافير صغيرة وغيوم فاتحة.|Бежевый известняк с мелкими окаменелостями и светлыми облаками.
sunny_menia|صني منيا|Санни Минья|Inexpensive light cream-yellow limestone, common for floors and facades in Arab countries.|حجر جيري أصفر كريمي فاتح رخيص، شائع للأرضيات والواجهات في الدول العربية.|Недорогой светлый кремово-жёлтый известняк; распространён для полов и фасадов в арабских странах.
pietra_serena|بييترا سيرينا|Пьетра Серена|Blue-grey sandstone of the columns and frames of Renaissance Florence.|حجر رملي رمادي مزرق صُنعت منه أعمدة وإطارات عمارة عصر النهضة في فلورنسا.|Сине-серый песчаник колонн и обрамлений ренессансной Флоренции.
locharbriggs|لوخاربريغز|Локарбриггс|Scottish red sandstone seen in Victorian buildings in many cities.|حجر رملي أحمر اسكتلندي يُرى في المباني الفيكتورية في مدن كثيرة.|Шотландский красный песчаник, встречается в викторианских зданиях многих городов.
volga_blue|فولغا بلو|Волга Блю|Dark labradorite with large crystals that flash blue in the light.|لابرادوريت داكن ببلورات كبيرة تلمع بالأزرق تحت الضوء.|Тёмный лабрадорит с крупными кристаллами, переливающимися синим на свету.
vizag_blue|فيزاغ بلو|Визаг Блю|Dark blue to grey granite with coarse grains.|غرانيت أزرق داكن إلى رمادي بحبيبات خشنة.|Тёмно-синий или серый крупнозернистый гранит.
viscount_white|فيسكونت وايت|Висконт Уайт|White granite with wavy grey and black bands.|غرانيت أبيض بأشرطة متموجة رمادية وسوداء.|Белый гранит с волнистыми серыми и чёрными полосами.
silver_pearl|سيلفر بيرل|Сильвер Перл|Silver-grey granite with sparkling grains.|غرانيت رمادي فضي بحبيبات لامعة.|Серебристо-серый гранит с блестящими зёрнами.
madura_gold|مادورا غولد|Мадура Голд|Golden granite with brown and black grains.|غرانيت ذهبي بحبيبات بنية وسوداء.|Золотистый гранит с коричневыми и чёрными зёрнами.
kashmir_gold|كشمير غولد|Кашмир Голд|Creamy gold granite with red garnet dots and dark grains.|غرانيت ذهبي كريمي بنقاط حمراء من العقيق وحبيبات داكنة.|Кремово-золотистый гранит с красными гранатами и тёмными зёрнами.
andromeda_white|أندروميدا وايت|Андромеда Уайт|White granite with grey and soft pink grains.|غرانيت أبيض بحبيبات رمادية ووردية خفيفة.|Белый гранит с серыми и нежно-розовыми зёрнами.
serizzo|سيريتسو أنتيغوريو|Серицо Антигорио|Grey gneiss with parallel dark bands; for floors, stairs and pavements in northern Italy.|نايس رمادي بأشرطة داكنة متوازية؛ للأرضيات والدرج والأرصفة في شمال إيطاليا.|Серый гнейс с параллельными тёмными полосами; для полов, лестниц и тротуаров на севере Италии.
rosa_baveno|روزا بافينو|Роза Бавено|Coarse-grained pink granite from the shores of Lake Maggiore.|غرانيت وردي خشن الحبيبات من ضفاف بحيرة ماجوري.|Крупнозернистый розовый гранит с берегов озера Маджоре.
bianco_montorfano|بيانكو مونتورفانو|Бьянко Монторфано|White granite with black mica grains, used in Milan's buildings.|غرانيت أبيض بحبيبات ميكا سوداء، استُخدم في مباني ميلانو.|Белый гранит с чёрными зёрнами слюды; использовался в зданиях Милана.
rosa_limbara|روزا ليمبارا|Роза Лимбара|Light pink granite with grey grains from Mount Limbara.|غرانيت وردي فاتح بحبيبات رمادية من جبل ليمبارا.|Светло-розовый гранит с серыми зёрнами с горы Лимбара.
porfido_trentino|بورفير ترينتينو|Порфир Трентино|Red-brown to purple porphyry; the best-known setts for streets and squares.|بورفير أحمر بني إلى بنفسجي؛ أشهر مكعبات رصف الشوارع والساحات.|Красно-коричневый или фиолетовый порфир; самая известная брусчатка для улиц и площадей.
porfido_argentino|بورفير أرجنتيني|Аргентинский порфир|Red-brown to purple Patagonian porphyry for setts and outdoor paving.|بورفير باتاغوني أحمر بني إلى بنفسجي لمكعبات الرصف والأرضيات الخارجية.|Красно-коричневый или фиолетовый патагонский порфир для брусчатки и мощения.
porfido_rosso_antico|بورفير إمبراطوري|Императорский порфир|Purple porphyry with small white crystals, used by Roman emperors for columns and statues.|بورفير أرجواني ببلورات بيضاء صغيرة، استخدمه أباطرة روما للأعمدة والتماثيل.|Пурпурный порфир с мелкими белыми кристаллами; римские императоры использовали его для колонн и статуй.
porfido_verde_antico|بورفير أخضر يوناني|Зелёный порфир|Dark green porphyry with pale green crystals; a classic Roman and Greek decorative stone.|بورفير أخضر داكن ببلورات خضراء فاتحة؛ حجر زخرفي روماني ويوناني كلاسيكي.|Тёмно-зелёный порфир со светло-зелёными кристаллами; классический римский и греческий декоративный камень.
rosso_vanga|روسو فانغا|Россо Ванга|Coarse red granite with blue quartz crystals.|غرانيت أحمر خشن ببلورات كوارتز زرقاء.|Крупнозернистый красный гранит с голубыми кристаллами кварца.
bohus_red|بوهوس الأحمر|Бохус Ред|Swedish red granite for facades, memorials and landscaping.|غرانيت سويدي أحمر للواجهات والنصب وتنسيق المساحات.|Шведский красный гранит для фасадов, памятников и благоустройства.
iddefjord|إيدفيورد|Иддефьорд|Even light grey granite for paving and kerbs.|غرانيت رمادي فاتح متجانس للرصف والأرصفة.|Ровный светло-серый гранит для мощения и бордюров.
emerald_pearl|إميرالد بيرل|Эмеральд Перл|Dark green larvikite with shimmering iridescent crystals.|لارفيكيت أخضر داكن ببلورات متلألئة قزحية.|Тёмно-зелёный ларвикит с переливающимися кристаллами.
kuru_grey|كورو غراي|Куру Грей|Fine-grained, even grey Finnish granite.|غرانيت فنلندي رمادي دقيق الحبيبات ومتجانس.|Мелкозернистый ровный серый финский гранит.
andeer|أنديير|Андеер|Swiss green-grey gneiss with fine bands; for floors and stairs.|نايس سويسري أخضر رمادي بأشرطة دقيقة؛ للأرضيات والدرج.|Швейцарский зеленовато-серый гнейс с тонкими полосами; для полов и лестниц.
gris_mondariz|غريس مونداريز|Грис Мондарис|Light grey Galician granite, widely used for facades and floors.|غرانيت رمادي فاتح من غاليسيا، واسع الاستخدام للواجهات والأرضيات.|Светло-серый галисийский гранит, широко используется для фасадов и полов.
tarn_granite|غرانيت تارن|Гранит Тарн|Blue-grey granite from France's main granite centre.|غرانيت رمادي مزرق من أهم مراكز الغرانيت في فرنسا.|Сине-серый гранит из главного гранитного центра Франции.
lanhelin|لانلان|Ланлен|Blue-grey Breton granite for building and memorials.|غرانيت رمادي مزرق من بريتاني للبناء والنصب.|Сине-серый бретонский гранит для строительства и памятников.
giallo_veneziano|جيالو فينيتسيانو|Джалло Венециано|Golden-yellow granite with brown and red dots; for countertops.|غرانيت أصفر ذهبي بنقاط بنية وحمراء؛ لأسطح المطابخ.|Золотисто-жёлтый гранит с коричневыми и красными точками; для столешниц.
g687|غرانيت G687|Гранит G687|Inexpensive peach-pink granite for floors and landscaping.|غرانيت وردي خوخي رخيص للأرضيات والمساحات الخارجية.|Недорогой персиково-розовый гранит для полов и благоустройства.
g640|غرانيت G640|Гранит G640|Grey granite with large black grains; widely used outdoors.|غرانيت رمادي بحبيبات سوداء كبيرة؛ واسع الاستخدام في الخارج.|Серый гранит с крупными чёрными зёрнами; широко применяется снаружи.
dakota_mahogany|داكوتا ماهوغاني|Дакота Махагони|Reddish-brown granite with black grains; for memorials.|غرانيت بني محمر بحبيبات سوداء؛ للنصب التذكارية.|Красновато-коричневый гранит с чёрными зёрнами; для памятников.
bethel_white|بيثيل وايت|Бетел Уайт|One of the whitest granites in the world, with fine grey grains.|من أكثر أنواع الغرانيت بياضاً في العالم، بحبيبات رمادية دقيقة.|Один из самых белых гранитов в мире, с мелкими серыми зёрнами.
khorramdarreh|غرانيت خرمدره|Гранит Хоррамдарре|Grey-white granite with black grains; widely used for floors and stairs in Iran.|غرانيت أبيض رمادي بحبيبات سوداء؛ واسع الاستخدام للأرضيات والدرج في إيران.|Серо-белый гранит с чёрными зёрнами; широко используется в Иране для полов и лестниц.
oppdal|كوارتزيت أوبدال|Кварцит Оппдал|Silver-grey platy quartzite with a natural cleft surface; for floors and walls.|كوارتزيت صفائحي رمادي فضي بسطح مشقوق طبيعي؛ للأرضيات والجدران.|Серебристо-серый плитчатый кварцит с природной колотой поверхностью; для полов и стен.
offerdal|كوارتزيت أوفردال|Кварцит Оффердал|Swedish grey platy quartzite with a natural surface.|كوارتزيت سويدي صفائحي رمادي بسطح طبيعي.|Шведский серый плитчатый кварцит с природной поверхностью.
alta_quartzite|كوارتزيت ألتا|Кварцит Альта|Grey quartzite from northern Norway that splits into thin slabs; for roofs and floors.|كوارتزيت رمادي من شمال النرويج ينشق إلى ألواح رقيقة؛ للأسطح والأرضيات.|Серый кварцит с севера Норвегии, колется на тонкие плиты; для кровли и полов.
hajiabad|ترافرتين حاجي آباد|Травертин Хаджиабад|White to light cream travertine; widely used on facades in Iran.|ترافرتين أبيض إلى كريمي فاتح؛ واسع الاستخدام في الواجهات في إيران.|Белый или светло-кремовый травертин; широко используется на фасадах в Иране.
takab|ترافرتين تكاب|Травертин Текаб|Cream to yellow travertine with wavy layering from north-west Iran.|ترافرتين كريمي إلى أصفر بطبقات متموجة من شمال غرب إيران.|Кремовый или жёлтый травертин с волнистыми слоями с северо-запада Ирана.
azarshahr_chocolate|ترافرتين آذرشهر الشوكولاتي|Шоколадный травертин Азаршахр|Chocolate-brown travertine with light and dark bands.|ترافرتين بني شوكولاتي بأشرطة فاتحة وداكنة.|Шоколадно-коричневый травертин со светлыми и тёмными полосами.
sivas_yellow|سيواس الأصفر|Сивас Еллоу|Golden-yellow travertine with brown bands from central Turkey.|ترافرتين أصفر ذهبي بأشرطة بنية من وسط تركيا.|Золотисто-жёлтый травертин с коричневыми полосами из центральной Турции.
honey_onyx|أونيكس إيراني عسلي|Иранский медовый оникс|Honey-yellow to orange onyx with wavy bands; glows warmly when backlit.|أونيكس أصفر عسلي إلى برتقالي بأشرطة متموجة؛ يتوهج بدفء عند الإضاءة الخلفية.|Медово-жёлтый или оранжевый оникс с волнистыми полосами; тепло светится при подсветке.
otta_slate|أردواز أوتا|Сланец Отта|Dark grey phyllite with fine sparkling grains; very durable for floors and facades.|فيليت رمادي داكن بحبيبات دقيقة لامعة؛ شديد المتانة للأرضيات والواجهات.|Тёмно-серый филлит с мелкими блёстками; очень прочен для полов и фасадов.
ardesia_genovese|أردواز جنوة|Генуэзский сланец|Black Ligurian slate long used for billiard tables, blackboards and roofs.|أردواز ليغوري أسود يُستخدم منذ القدم لطاولات البلياردو والسبورات والأسطح.|Чёрный лигурийский сланец, издавна идёт на бильярдные столы, доски и кровлю.
deoli_green|أردواز ديولي الأخضر|Деоли Грин|Light green Indian slate for floors and walls.|أردواز هندي أخضر فاتح للأرضيات والجدران.|Светло-зелёный индийский сланец для полов и стен.
burlington|أردواز برلنغتون|Сланец Берлингтон|Light green to olive slate from northern England; for roofs, floors and facades.|أردواز أخضر فاتح إلى زيتوني من شمال إنجلترا؛ للأسطح والأرضيات والواجهات.|Светло-зелёный или оливковый сланец с севера Англии; для кровли, полов и фасадов.
diyarbakir_basalt|بازلت ديار بكر|Базальт Диярбакыр|Porous black basalt of Diyarbakır's historic city walls.|بازلت أسود مسامي بُنيت منه أسوار ديار بكر التاريخية.|Пористый чёрный базальт исторических стен Диярбакыра.
blue_agate|عقيق أزرق|Голубой агат|Translucent slab of blue agate slices with coloured rings; for backlit walls and counters.|لوح شبه شفاف من شرائح العقيق الأزرق بحلقات ملونة؛ للجدران والكاونترات المضاءة.|Полупрозрачная плита из срезов голубого агата с цветными кольцами; для стен и стоек с подсветкой.
amethyst|جمشت|Аметист|Purple slab of amethyst pieces that glows violet when backlit.|لوح بنفسجي من قطع الجمشت يتوهج بالبنفسجي عند الإضاءة الخلفية.|Фиолетовая плита из кусочков аметиста; светится фиолетовым при подсветке.
rose_quartz|كوارتز وردي|Розовый кварц|Translucent pink slab of rose quartz pieces.|لوح وردي شبه شفاف من قطع الكوارتز الوردي.|Полупрозрачная розовая плита из кусочков розового кварца.
tigers_eye|عين النمر|Тигровый глаз|Golden-brown slab with a silky shimmer, made from tiger's eye pieces.|لوح بني ذهبي بلمعان حريري من قطع عين النمر.|Золотисто-коричневая плита с шелковистым отливом из кусочков тигрового глаза.
petrified_wood|خشب متحجر|Окаменелое дерево|Slab of petrified wood slices showing the tree's growth rings; for tables and walls.|لوح من شرائح الخشب المتحجر تظهر فيه حلقات نمو الشجرة؛ للطاولات والجدران.|Плита из срезов окаменелого дерева с годичными кольцами; для столов и стен.
"""

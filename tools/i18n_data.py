"""Arabic, English and Russian text for seed.json (Persian lives in build_seed.py).

Every table is "|"-separated. build_seed.py checks that every stone, type,
region and country has an entry, so a missing translation fails the build.
"""

LANGS = ("en", "ar", "ru")

# fa | en | ar | ru
COUNTRIES = """
ایران|Iran|إيران|Иран
ایتالیا|Italy|إيطاليا|Италия
ترکیه|Turkey|تركيا|Турция
اسپانیا|Spain|إسبانيا|Испания
یونان|Greece|اليونان|Греция
هند|India|الهند|Индия
پرتغال|Portugal|البرتغال|Португалия
برزیل|Brazil|البرازيل|Бразилия
چین|China|الصين|Китай
فنلاند|Finland|فنلندا|Финляндия
نروژ|Norway|النرويج|Норвегия
آفریقای جنوبی|South Africa|جنوب أفريقيا|ЮАР
زیمباوه|Zimbabwe|زيمبابوي|Зимбабве
مکزیک|Mexico|المكسيك|Мексика
پاکستان|Pakistan|باكستان|Пакистан
انگلستان|England|إنجلترا|Англия
بریتانیا (ولز)|United Kingdom (Wales)|المملكة المتحدة (ويلز)|Великобритания (Уэльс)
فلسطین|Palestine|فلسطين|Палестина
آمریکا|USA|الولايات المتحدة|США
فرانسه|France|فرنسا|Франция
جمهوری دومینیکن|Dominican Republic|جمهورية الدومينيكان|Доминиканская Республика
استرالیا|Australia|أستراليا|Австралия
مقدونیهٔ شمالی|North Macedonia|مقدونيا الشمالية|Северная Македония
آلمان|Germany|ألمانيا|Германия
بلغارستان|Bulgaria|بلغاريا|Болгария
بلژیک|Belgium|بلجيكا|Бельгия
پرو|Peru|بيرو|Перу
"""

# fa | en | ar | ru
REGIONS = """
آباده، فارس|Abadeh, Fars|آباده، فارس|Абаде, Фарс
آذرشهر، آذربایجان شرقی|Azarshahr, East Azerbaijan|آذرشهر، أذربيجان الشرقية|Азаршахр, Восточный Азербайджан
آفیون‌قره‌حصار|Afyonkarahisar|أفيون قره حصار|Афьонкарахисар
آلکوباسا|Alcobaça|ألكوباسا|Алкобаса
آلیکانته، والنسیا|Alicante, Valencia|أليكانتي، فالنسيا|Аликанте, Валенсия
آندرا پرادش|Andhra Pradesh|أندرا براديش|Андхра-Прадеш
ازنا، لرستان|Azna, Lorestan|أزنا، لرستان|Азна, Лурестан
استان اصفهان|Isfahan Province|محافظة أصفهان|провинция Исфахан
استان فوجیان|Fujian Province|مقاطعة فوجيان|провинция Фуцзянь
استان یزد|Yazd Province|محافظة يزد|провинция Йезд
استرموز، آلنتژو|Estremoz, Alentejo|إستريموش، ألنتيجو|Эштремош, Алентежу
اسپیریتو سانتو|Espírito Santo|إسبيريتو سانتو|Эспириту-Санту
اوباتوبا، سائوپائولو|Ubatuba, São Paulo|أوباتوبا، ساو باولو|Убатуба, Сан-Паулу
اوبر، آریژ|Aubert, Ariège|أوبير، آرييج|Обер, Арьеж
اودایپور، راجستان|Udaipur, Rajasthan|أودايبور، راجستان|Удайпур, Раджастхан
اورشلیم و کرانهٔ باختری|Jerusalem and the West Bank|القدس والضفة الغربية|Иерусалим и Западный берег
اوریسا|Odisha|أوديشا|Одиша
اونگول، آندرا پرادش|Ongole, Andhra Pradesh|أونغول، أندرا براديش|Онголе, Андхра-Прадеш
ایران|Iran|إيران|Иран
باهیا|Bahia|باهيا|Баия
باواریا|Bavaria|بافاريا|Бавария
باگنوریجو، لاتزیو|Bagnoregio, Lazio|بانيوريدجو، لاتسيو|Баньореджо, Лацио
بث، سامرست|Bath, Somerset|باث، سومرست|Бат, Сомерсет
بدفورد، ایندیانا|Bedford, Indiana|بيدفورد، إنديانا|Бедфорд, Индиана
برزیل|Brazil|البرازيل|Бразилия
برشا، لمباردی|Brescia, Lombardy|بريشيا، لومبارديا|Брешиа, Ломбардия
بلوچستان|Balochistan|بلوشستان|Белуджистан
بوردور|Burdur|بوردور|Бурдур
تاملا|Tammela|تاميلا|Таммела
تامیل نادو|Tamil Nadu|تاميل نادو|Тамилнад
تراپانی، سیسیل|Trapani, Sicily|تراباني، صقلية|Трапани, Сицилия
تسالی|Thessaly|ثيساليا|Фессалия
تلنگانه|Telangana|تيلانغانا|Телангана
توکالی، پوئبلا|Tecali, Puebla|تيكالي، بويبلا|Текали, Пуэбла
تیوولی، لاتزیو|Tivoli, Lazio|تيفولي، لاتسيو|Тиволи, Лацио
جزیرهٔ تاسوس|Thassos Island|جزيرة ثاسوس|остров Тасос
جزیرهٔ مرمره، بالیکسیر|Marmara Island, Balıkesir|جزيرة مرمرة، باليكسير|остров Мармара, Балыкесир
جزیرهٔ پورتلند، دورست|Isle of Portland, Dorset|جزيرة بورتلاند، دورست|остров Портленд, Дорсет
جوشقان، اصفهان|Jowshaqan, Isfahan|جوشقان، أصفهان|Джошакан, Исфахан
خرم‌آباد، لرستان|Khorramabad, Lorestan|خرم آباد، لرستان|Хорремабад, Лурестан
خونین|Junín|خونين|Хунин
دراما|Drama|دراما|Драма
دره آئوستا|Aosta Valley|وادي أوستا|Валле-д'Аоста
درهٔ اسلیت، ورمونت|Slate Valley, Vermont|وادي السليت، فيرمونت|Слейт-Вэлли, Вермонт
درود، لرستان|Dorud, Lorestan|درود، لرستان|Доруд, Лурестан
دلیجان، استان مرکزی|Delijan, Markazi|دليجان، المحافظة المركزية|Делиджан, Меркези
دنیزلی|Denizli|دنيزلي|Денизли
دهبید، فارس|Dehbid, Fars|دهبيد، فارس|Дехбид, Фарс
دولپور، راجستان|Dholpur, Rajasthan|دولبور، راجستان|Дхолпур, Раджастхан
راجستان|Rajasthan|راجستان|Раджастхан
روستنبورگ|Rustenburg|روستنبرغ|Растенбург
زاهدان، سیستان و بلوچستان|Zahedan, Sistan and Baluchestan|زاهدان، سيستان وبلوشستان|Захедан, Систан и Белуджистан
ساردینیا|Sardinia|سردينيا|Сардиния
سواحل جنوبی|Southern coast|الساحل الجنوبي|южное побережье
سیدنی، نیو ساوت ولز|Sydney, New South Wales|سيدني، نيو ساوث ويلز|Сидней, Новый Южный Уэльс
شانشی|Shanxi|شانشي|Шаньси
شیرکوه، یزد|Shirkuh, Yazd|شيركوه، يزد|Ширкух, Йезд
فاوسکه|Fauske|فاوسكه|Фауске
فریولی|Friuli|فريولي|Фриули
فوجیان|Fujian|فوجيان|Фуцзянь
لا ریوخا|La Rioja|لا ريوخا|Риоха
لارویک|Larvik|لارفيك|Ларвик
لازا، تیرول جنوبی|Laas, South Tyrol|لاس، تيرول الجنوبية|Лас, Южный Тироль
لاشتر، اصفهان|Lashtar, Isfahan|لاشتر، أصفهان|Лаштар, Исфахан
لانگدوک|Languedoc|لانغدوك|Лангедок
لوانتو، لیگوریا|Levanto, Liguria|ليفانتو، ليغوريا|Леванто, Лигурия
مارکینا، باسک|Markina, Basque Country|ماركينا، إقليم الباسك|Маркина, Страна Басков
محلات، استان مرکزی|Mahallat, Markazi|محلات، المحافظة المركزية|Махаллат, Меркези
ملایر، همدان|Malayer, Hamadan|ملاير، همدان|Малайер, Хамадан
منطقهٔ دنیزلی|Denizli region|منطقة دنيزلي|регион Денизли
منطقهٔ موتوکو|Mutoko area|منطقة موتوكو|район Мутоко
منطقهٔ والونی|Wallonia|منطقة والونيا|Валлония
مکرانا، راجستان|Makrana, Rajasthan|مكرانا، راجستان|Макрана, Раджастхан
میناس ژرایس|Minas Gerais|ميناس جيرايس|Минас-Жерайс
نطنز، اصفهان|Natanz, Isfahan|نطنز، أصفهان|Натанз, Исфахан
نهبندان، خراسان جنوبی|Nehbandan, South Khorasan|نهبندان، خراسان الجنوبية|Нехбендан, Южный Хорасан
نی‌ریز، فارس|Neyriz, Fars|نيريز، فارس|Нейриз, Фарс
هرسین، کرمانشاه|Harsin, Kermanshah|هرسين، كرمانشاه|Харсин, Керманшах
هونان|Hunan|هونان|Хунань
والدئوراس، گالیسیا|Valdeorras, Galicia|فالديوراس، غاليسيا|Вальдеоррас, Галисия
ورتسا|Vratsa|فراتسا|Враца
ورونا، ونتو|Verona, Veneto|فيرونا، فينيتو|Верона, Венето
پریلپ|Prilep|بريليب|Прилеп
پورتلند، کنتیکت|Portland, Connecticut|بورتلاند، كونيتيكت|Портленд, Коннектикут
پورتووِنِره، لیگوریا|Porto Venere, Liguria|بورتو فينيري، ليغوريا|Портовенере, Лигурия
پورینو، گالیسیا|O Porriño, Galicia|أو بورينيو، غاليسيا|О-Порриньо, Галисия
کاتانیا، سیسیل|Catania, Sicily|كاتانيا، صقلية|Катания, Сицилия
کارارا، توسکانی|Carrara, Tuscany|كارارا، توسكانا|Каррара, Тоскана
کارناتاکا|Karnataka|كارناتاكا|Карнатака
کاستیا|Castile|قشتالة|Кастилия
کان، نرماندی|Caen, Normandy|كان، نورماندي|Кан, Нормандия
کوه پنتلی، آتیکا|Mount Penteli, Attica|جبل بنتيلي، أتيكا|гора Пентеликон, Аттика
گوانگشی|Guangxi|قوانغشي|Гуанси
گوینت|Gwynedd|غوينيد|Гуинет
یلاروی|Ylämaa|يلاما|Юлямаа
یورکشایر|Yorkshire|يوركشاير|Йоркшир
"""

# Top-level categories, following the stone-type grouping used by stonecontact.com.
# id | fa | en | ar | ru | types in this category (comma separated)
CATEGORIES = """
marble|مرمر|Marble|رخام|Мрамор|marble,dolomitic,marmarite,serpentinite
granite|گرانیت|Granite|غرانيت|Гранит|granite,basalt
limestone|لایمستون (سنگ آهک)|Limestone|حجر جيري|Известняк|limestone
travertine|تراورتن|Travertine|ترافرتين|Травертин|travertine
sandstone|ماسه‌سنگ|Sandstone|حجر رملي|Песчаник|sandstone
quartzite|کوارتزیت|Quartzite|كوارتزيت|Кварцит|quartzite
onyx|اونیکس (مرمر سنگ)|Onyx|أونيكس|Оникс|onyx
slate|اسلیت|Slate|أردواز|Сланец|slate
"""

# id | ar name | ru name | en description | ar description | ru description
TYPES = """
granite|غرانيت|Гранит|Coarse-grained intrusive igneous rock of quartz, feldspar and mica. The trade also calls gabbro, diorite and norite "granite". Very hard and low-absorbing, suited to facades, busy floors, stairs and countertops.|صخر ناري جوفي خشن الحبيبات من الكوارتز والفلسبار والميكا. يسمي السوق الغابرو والديوريت والنوريت «غرانيت» أيضاً. شديد الصلابة قليل الامتصاص، مناسب للواجهات والأرضيات المزدحمة والدرج وأسطح المطابخ.|Крупнозернистая глубинная магматическая порода из кварца, полевого шпата и слюды. В торговле гранитом называют также габбро, диорит и норит. Очень твёрдый и мало впитывает воду; подходит для фасадов, полов с высокой нагрузкой, лестниц и столешниц.
marble|رخام|Мрамор|Metamorphic rock formed when limestone recrystallises. Interlocking calcite crystals give it its lustre and veining. Sensitive to acids and best used indoors.|صخر متحول ينشأ من إعادة تبلور الحجر الجيري. تمنحه بلورات الكالسيت المتشابكة لمعانه وعروقه. حساس للأحماض وأفضل استخدام له في الداخل.|Метаморфическая порода, образующаяся при перекристаллизации известняка. Сросшиеся кристаллы кальцита дают блеск и прожилки. Чувствителен к кислотам, лучше всего подходит для интерьеров.
dolomitic|رخام دولوميتي (تشيني وكريستال)|Доломитовый мрамор (чини и кристалл)|White crystalline dolomitic marble, called "chini" or "crystal" in the Iranian market. Slightly harder and less absorbent than calcite marble; with cold acid it fizzes only when powdered.|رخام دولوميتي أبيض بلوري يُسمى في السوق الإيرانية «تشيني» أو «كريستال». أصلب قليلاً وأقل امتصاصاً من الرخام الكالسيتي، ولا يفور مع الحمض البارد إلا مسحوقاً.|Белый кристаллический доломитовый мрамор, на иранском рынке его называют «чини» или «кристалл». Немного твёрже и плотнее кальцитового мрамора; с холодной кислотой вскипает только в порошке.
marmarite|حجر جيري متماسك (مرمريت)|Плотный известняк (мармарит)|Dense polishable limestone, sold as "marmarite" in Iran and often as "marble" internationally. Fossils and calcite veins are common.|حجر جيري كثيف قابل للصقل، يُباع في إيران باسم «مرمريت» وغالباً باسم «رخام» عالمياً. الأحافير وعروق الكالسيت شائعة فيه.|Плотный полируемый известняк, в Иране его продают как «мармарит», а на мировом рынке часто как «мрамор». Нередко содержит окаменелости и кальцитовые прожилки.
travertine|ترافرتين|Травертин|Limestone deposited by hot springs, with characteristic pores and wavy layering. Iran is one of the largest producers. Pores are usually filled with resin or cement.|حجر جيري يترسب من الينابيع الحارة، له مسام مميزة وطبقات متموجة. إيران من أكبر المنتجين. تُملأ المسام عادة بالراتنج أو الإسمنت.|Известняк, отложенный горячими источниками, с характерными порами и волнистой слоистостью. Иран — один из крупнейших производителей. Поры обычно заполняют смолой или цементом.
onyx|رخام أونيكس|Мраморный оникс|Banded, translucent calcite or aragonite deposited in caves and springs. Lets light through, so it is used for backlit walls and luxury details. Soft and brittle; recommended for interiors only.|كالسيت أو أراغونيت شفاف ومخطط يترسب في الكهوف والينابيع. ينفذ منه الضوء فيُستخدم للجدران المضاءة من الخلف والتفاصيل الفاخرة. طري وهش، يُنصح به للداخل فقط.|Полосчатый полупрозрачный кальцит или арагонит, отложенный в пещерах и источниках. Пропускает свет, поэтому используется для стен с подсветкой и роскошной отделки. Мягкий и хрупкий, только для интерьеров.
limestone|حجر جيري|Известняк|Sedimentary carbonate rock with moderate porosity that carves easily. Many of the world's historic buildings are made of it. Strength and absorption depend strongly on density.|صخر رسوبي كربوناتي متوسط المسامية سهل النحت. بُنيت منه كثير من المباني التاريخية في العالم. تعتمد مقاومته وامتصاصه كثيراً على كثافته.|Осадочная карбонатная порода средней пористости, легко обрабатывается. Из неё построены многие исторические здания мира. Прочность и водопоглощение сильно зависят от плотности.
sandstone|حجر رملي|Песчаник|Sedimentary rock of sand grains (mostly quartz) bound by natural cement. Rough and slip-resistant, good for landscaping and facades.|صخر رسوبي من حبيبات الرمل (غالباً كوارتز) ملتحمة بإسمنت طبيعي. سطحه خشن ومقاوم للانزلاق، مناسب للمساحات الخارجية والواجهات.|Осадочная порода из песчинок (в основном кварца), сцементированных природным цементом. Шероховатая и нескользкая, хороша для благоустройства и фасадов.
quartzite|كوارتزيت|Кварцит|Metamorphosed quartz sandstone; harder than granite while looking like marble. Very durable for countertops and busy floors.|حجر رملي كوارتزي متحول؛ أصلب من الغرانيت ويشبه الرخام في مظهره. شديد التحمل لأسطح المطابخ والأرضيات المزدحمة.|Метаморфизованный кварцевый песчаник: твёрже гранита, но выглядит как мрамор. Очень износостойкий для столешниц и полов.
slate|أردواز|Сланец|Fine-grained metamorphic rock that splits into thin flat sheets. Used for roofing, floors and natural-face walls.|صخر متحول دقيق الحبيبات ينفلق إلى صفائح رقيقة مستوية. يُستخدم لتغطية الأسطح والأرضيات والجدران ذات السطح الطبيعي.|Мелкозернистая метаморфическая порода, раскалывающаяся на тонкие ровные плиты. Используется для кровли, полов и стен с природной фактурой.
basalt|بازلت وأحجار بركانية|Базальт и вулканический камень|Dark, fine-grained extrusive igneous rock. Highly resistant to abrasion and frost; used for paving, kerbs and facades.|صخر ناري سطحي داكن دقيق الحبيبات. شديد المقاومة للتآكل والصقيع؛ يُستخدم للرصف والأرصفة والواجهات.|Тёмная мелкозернистая излившаяся порода. Очень устойчива к истиранию и морозу; применяется для мощения, бордюров и фасадов.
serpentinite|سربنتينيت (رخام أخضر)|Серпентинит (зелёный мрамор)|Green metamorphic rock of serpentine minerals, sold as "green marble" or "verde". Usually does not react with acid unless it has calcite veins.|صخر متحول أخضر من معادن السربنتين، يُباع باسم «الرخام الأخضر» أو «فيردي». لا يتفاعل عادة مع الحمض ما لم تكن فيه عروق كالسيت.|Зелёная метаморфическая порода из минералов серпентина, продаётся как «зелёный мрамор» или «верде». Обычно не реагирует с кислотой, если нет кальцитовых прожилок.
"""

# id | ar name | ru name | en description | ar description | ru description
STONES = """
mahallat_cream|ترافرتين محلات الكريمي|Травертин Махаллат кремовый|One of Iran's best-known travertines, with a light cream base and wavy layering; very common on residential facades.|من أشهر أنواع الترافرتين الإيراني، بأرضية كريمية فاتحة وطبقات متموجة؛ شائع جداً في واجهات المباني السكنية.|Один из самых известных иранских травертинов: светло-кремовый фон и волнистая слоистость; очень распространён на фасадах жилых домов.
atashkooh|ترافرتين آتشكوه|Травертин Аташкух|Cream to beige travertine with fine pores and a fairly even texture; used for floors and facades.|ترافرتين كريمي إلى بيج بمسام دقيقة وملمس متجانس نسبياً؛ للأرضيات والواجهات.|Кремовый или бежевый травертин с мелкими порами и довольно ровной текстурой; для полов и фасадов.
abbasabad|ترافرتين عباس آباد|Травертин Аббасабад|Light travertine with a milky to cream base; widely used on facades in Iran.|ترافرتين فاتح بأرضية حليبية إلى كريمية؛ واسع الاستخدام في الواجهات في إيران.|Светлый травертин молочно-кремового тона; широко применяется на фасадах в Иране.
azarshahr_red|ترافرتين آذرشهر الأحمر|Красный травертин Азаршахр|Red to orange travertine with coloured bands; a rare Iranian export variety.|ترافرتين أحمر إلى برتقالي بأشرطة ملونة؛ من الأنواع الإيرانية النادرة المصدَّرة.|Красный или оранжевый травертин с цветными полосами; редкий экспортный иранский сорт.
azarshahr_yellow|ترافرتين آذرشهر الليموني|Жёлтый травертин Азаршахр|Lemon-yellow travertine with wavy layering; gives facades and floors a warm look.|ترافرتين أصفر ليموني بطبقات متموجة؛ يضفي دفئاً على الواجهات والأرضيات.|Лимонно-жёлтый травертин с волнистыми слоями; придаёт фасадам и полам тёплый вид.
silver_travertine|ترافرتين فضي|Серебристый травертин|Grey to silver travertine with parallel veins; vein-cut it looks linear.|ترافرتين رمادي إلى فضي بعروق متوازية؛ يبدو خطياً عند القص الموازي للطبقات.|Серый или серебристый травертин с параллельными прожилками; при распиле по слоям выглядит линейным.
denizli_walnut|ترافرتين دنيزلي الجوزي|Травертин Денизли «ноче»|Walnut-brown travertine with warm colour variation; popular tumbled for floors and walls.|ترافرتين بني جوزي بتدرجات دافئة؛ شائع بتشطيب معتّق للأرضيات والجدران.|Травертин орехово-коричневого цвета с тёплыми переходами; популярен в галтованном виде для полов и стен.
denizli_light|ترافرتين دنيزلي الفاتح|Травертин Денизли светлый|Classic light cream travertine; one of the best sellers on the world market.|ترافرتين كريمي فاتح كلاسيكي؛ من الأكثر مبيعاً في السوق العالمية.|Классический светло-кремовый травертин; один из самых продаваемых в мире.
travertino_romano|ترافرتين روماني|Травертин Романо|Rome's historic travertine; the Colosseum and St Peter's Square are built of it.|الترافرتين التاريخي لروما؛ بُني منه الكولوسيوم وساحة القديس بطرس.|Исторический травертин Рима: из него построены Колизей и площадь Святого Петра.
carrara|رخام كارارا|Мрамор Каррара|White to light grey marble with fine grey veins; the world's most famous marble, quarried since Roman times.|رخام أبيض إلى رمادي فاتح بعروق رمادية رفيعة؛ أشهر رخام في العالم، يُستخرج منذ العصر الروماني.|Белый или светло-серый мрамор с тонкими серыми прожилками; самый известный мрамор мира, добывается со времён Рима.
statuario|ستاتواريو|Статуарио|Pure white marble with bold grey veins; the classic sculptors' stone and one of the most expensive marbles.|رخام أبيض نقي بعروق رمادية بارزة؛ حجر النحاتين الكلاسيكي ومن أغلى أنواع الرخام.|Чисто-белый мрамор с выразительными серыми прожилками; классический скульптурный камень и один из самых дорогих.
calacatta|كالاكاتا|Калакатта|White marble with broad gold to grey veins; a symbol of luxury interiors.|رخام أبيض بعروق عريضة ذهبية إلى رمادية؛ رمز للديكورات الفاخرة.|Белый мрамор с широкими золотистыми или серыми прожилками; символ роскошных интерьеров.
arabescato|أرابيسكاتو|Арабескато|White marble with dense, irregular grey veining.|رخام أبيض بعروق رمادية كثيفة غير منتظمة.|Белый мрамор с густыми неровными серыми прожилками.
bardiglio|بارديليو|Бардильо|Bluish-grey marble with darker veins from the Carrara quarries.|رخام رمادي مائل للزرقة بعروق أغمق من محاجر كارارا.|Голубовато-серый мрамор с более тёмными прожилками из карьеров Каррары.
pentelic|رخام بنتيلي|Пентелийский мрамор|Fine-grained white marble with a faint golden tint; the stone of the Parthenon.|رخام أبيض دقيق الحبيبات بمسحة ذهبية خفيفة؛ حجر البارثينون.|Мелкозернистый белый мрамор с лёгким золотистым оттенком; камень Парфенона.
volakas|فولاكاس|Волакас|White marble with pale grey veins; a common alternative to Italian marbles.|رخام أبيض بعروق رمادية باهتة؛ بديل شائع للرخام الإيطالي.|Белый мрамор с бледно-серыми прожилками; распространённая альтернатива итальянским.
makrana|رخام مكرانا|Мрамор Макрана|White marble used to build the Taj Mahal.|رخام أبيض بُني منه تاج محل.|Белый мрамор, из которого построен Тадж-Махал.
afyon_white|أبيض أفيون|Белый Афьон|Milky white marble with an even texture.|رخام أبيض حليبي بملمس متجانس.|Молочно-белый мрамор с ровной текстурой.
marmara_white|رخام جزيرة مرمرة|Мрамор острова Мармара|White marble with parallel grey bands; the Sea of Marmara is named after these quarries.|رخام أبيض بأشرطة رمادية متوازية؛ سُمّي بحر مرمرة باسم هذه المحاجر.|Белый мрамор с параллельными серыми полосами; Мраморное море названо по этим карьерам.
estremoz|رخام إستريموش|Мрамор Эштремош|Pink to cream marble with soft clouding from Portugal's old quarries.|رخام وردي إلى كريمي بغيوم ناعمة من محاجر البرتغال القديمة.|Розовый или кремовый мрамор с мягкими облаками из старых карьеров Португалии.
nero_marquina|نيرو ماركينا|Неро Маркина|Black stone with bright white veins; one of the most popular black stones in interior design.|حجر أسود بعروق بيضاء لامعة؛ من أكثر الأحجار السوداء رواجاً في التصميم الداخلي.|Чёрный камень с яркими белыми прожилками; один из самых популярных чёрных камней в интерьере.
nero_portoro|نيرو بورتورو|Неро Порторо|Black stone with golden veins; rare and expensive.|حجر أسود بعروق ذهبية؛ نادر وغالي الثمن.|Чёрный камень с золотыми прожилками; редкий и дорогой.
azna_chini|تشيني أزنا|Чини Азна|Brilliant white crystalline dolomitic marble; one of Iran's best-known chini stones.|رخام دولوميتي أبيض بلوري شديد اللمعان؛ من أشهر أحجار التشيني الإيرانية.|Сверкающий белый кристаллический доломитовый мрамор; один из самых известных иранских «чини».
neyriz_chini|تشيني نيريز|Чини Нейриз|White chini stone with very soft grey clouds; for interior floors and walls.|حجر تشيني أبيض بغيوم رمادية خفيفة جداً؛ للأرضيات والجدران الداخلية.|Белый «чини» с очень мягкими серыми облаками; для полов и стен в помещениях.
dorud_chini|كريستال درود|Кристалл Доруд|White chini with fine grey veins.|تشيني أبيض بعروق رمادية رفيعة.|Белый «чини» с тонкими серыми прожилками.
thassos|أبيض ثاسوس|Белый Тасос|One of the whitest stones in the world, with sparkling crystals; a very pure dolomitic marble.|من أنصع الأحجار بياضاً في العالم ببلورات لامعة؛ رخام دولوميتي نقي جداً.|Один из самых белых камней в мире, с искрящимися кристаллами; очень чистый доломитовый мрамор.
sivec|سيفيتس|Сивец|Fine-grained white dolomitic marble similar to Thassos.|رخام دولوميتي أبيض دقيق الحبيبات يشبه ثاسوس.|Мелкозернистый белый доломитовый мрамор, похожий на тасос.
dehbid|مرمريت دهبيد|Мармарит Дехбид|Cream to beige marmarite with light brown clouds; widely used for floors in Iran.|مرمريت كريمي إلى بيج بغيوم بنية فاتحة؛ واسع الاستخدام في الأرضيات بإيران.|Кремово-бежевый мармарит со светло-коричневыми облаками; широко используется для полов в Иране.
harsin|مرمريت هرسين|Мармарит Харсин|Even cream marmarite with little waste; very common for flooring.|مرمريت كريمي متجانس قليل الهدر؛ شائع جداً للأرضيات.|Ровный кремовый мармарит с малыми отходами; очень популярен для полов.
gohareh|مرمريت كوهره|Мармарит Гохаре|White to milky marmarite with soft clouds.|مرمريت أبيض إلى حليبي بغيوم ناعمة.|Белый или молочный мармарит с мягкими облаками.
jowshaqan|مرمريت جوشقان|Мармарит Джошакан|Light cream marmarite used for floors and stairs.|مرمريت كريمي فاتح للأرضيات والدرج.|Светло-кремовый мармарит для полов и лестниц.
lashtar|مرمريت لاشتر|Мармарит Лаштар|Cream marmarite with a fine, even texture.|مرمريت كريمي بملمس دقيق ومتجانس.|Кремовый мармарит с мелкой ровной текстурой.
abadeh|مرمريت آباده|Мармарит Абаде|Light marmarite with cream clouds from an old quarry in southern Iran.|مرمريت فاتح بغيوم كريمية من محجر قديم في جنوب إيران.|Светлый мармарит с кремовыми облаками из старого карьера на юге Ирана.
crema_marfil|كريما مارفيل|Крема Марфил|Ivory-cream stone with fine veins; one of the world's best-selling stones.|حجر كريمي عاجي بعروق رفيعة؛ من أكثر الأحجار مبيعاً في العالم.|Камень цвета слоновой кости с тонкими прожилками; один из самых продаваемых в мире.
emperador|إمبرادور داكن|Эмперадор тёмный|Dark brown stone with a network of light calcite veins.|حجر بني داكن بشبكة من عروق الكالسيت الفاتحة.|Тёмно-коричневый камень с сетью светлых кальцитовых прожилок.
rojo_alicante|أحمر أليكانتي|Рохо Аликанте|Brick-red stone with white veins.|حجر أحمر طوبي بعروق بيضاء.|Кирпично-красный камень с белыми прожилками.
botticino|بوتيتشينو|Боттичино|Cream stone with clouds and tiny fossils; the Victor Emmanuel II monument in Rome is built of it.|حجر كريمي بغيوم وأحافير دقيقة؛ بُني منه نصب فيكتور عمانوئيل الثاني في روما.|Кремовый камень с облаками и мелкими окаменелостями; из него построен памятник Виктору Эммануилу II в Риме.
rosso_verona|أحمر فيرونا|Россо Верона|Red limestone with ammonite fossils; abundant in Verona's historic buildings.|حجر جيري أحمر بأحافير الأمونيت؛ كثير في مباني فيرونا التاريخية.|Красный известняк с аммонитами; широко встречается в исторических зданиях Вероны.
burdur_beige|بيج بوردور|Бурдур беж|Even beige stone sold internationally as marble.|حجر بيج متجانس يُباع عالمياً كرخام.|Ровный бежевый камень, продаётся на мировом рынке как мрамор.
yazd_onyx|أونيكس يزد|Оникс Йезд|Honey-yellow to white onyx with wavy bands; translucent and suited to backlit walls.|أونيكس أصفر عسلي إلى أبيض بأشرطة متموجة؛ شفاف ومناسب للجدران المضاءة من الخلف.|Медово-жёлтый или белый оникс с волнистыми полосами; полупрозрачный, подходит для стен с подсветкой.
persian_white_onyx|أونيكس إيراني أبيض|Иранский белый оникс|White onyx with cream bands; lets a lot of light through.|أونيكس أبيض بأشرطة كريمية؛ ينفذ منه الكثير من الضوء.|Белый оникс с кремовыми полосами; хорошо пропускает свет.
persian_pink_onyx|أونيكس إيراني وردي|Иранский розовый оникс|Pink onyx with white and cream bands; for luxury spaces and lighting.|أونيكس وردي بأشرطة بيضاء وكريمية؛ للمساحات الفاخرة والإضاءة.|Розовый оникс с белыми и кремовыми полосами; для роскошных интерьеров и подсветки.
green_onyx_pakistan|أونيكس باكستاني أخضر|Пакистанский зелёный оникс|Light green onyx with brown veins; for decorative objects and walls.|أونيكس أخضر فاتح بعروق بنية؛ للتحف والجدران.|Светло-зелёный оникс с коричневыми прожилками; для декора и стен.
mexican_onyx|أونيكس مكسيكي|Мексиканский оникс|Honey to green onyx with translucent bands.|أونيكس عسلي إلى أخضر بأشرطة شفافة.|Медовый или зеленоватый оникс с прозрачными полосами.
natanz_granite|غرانيت نطنز|Гранит Натанз|Light grey granite with black speckles (salt and pepper); one of Iran's most used granites for floors and stairs.|غرانيت رمادي فاتح بنقاط سوداء (ملح وفلفل)؛ من أكثر أنواع الغرانيت الإيراني استخداماً للأرضيات والدرج.|Светло-серый гранит с чёрными вкраплениями («соль с перцем»); один из самых используемых иранских гранитов для полов и лестниц.
zahedan_granite|غرانيت زاهدان|Гранит Захедан|Medium-grained grey granite for facades and paving.|غرانيت رمادي متوسط الحبيبات للواجهات والرصف.|Среднезернистый серый гранит для фасадов и мощения.
shirkuh_red|غرانيت يزد الأحمر (شيركوه)|Красный гранит Йезд (Ширкух)|Pink to red granite with large feldspar crystals.|غرانيت وردي إلى أحمر ببلورات فلسبار كبيرة.|Розовый или красный гранит с крупными кристаллами полевого шпата.
malayer_granite|غرانيت ملاير|Гранит Малайер|Light grey to white granite for stairs and floors.|غرانيت رمادي فاتح إلى أبيض للدرج والأرضيات.|Светло-серый или белый гранит для лестниц и полов.
nehbandan_granite|غرانيت نهبندان|Гранит Нехбендан|Grey granite from eastern Iran for paving and facades.|غرانيت رمادي من شرق إيران للرصف والواجهات.|Серый гранит с востока Ирана для мощения и фасадов.
absolute_black|أبسولوت بلاك|Абсолют Блэк|Completely black, uniform "granite" (actually gabbro); for countertops and memorials.|«غرانيت» أسود تماماً ومتجانس (غابرو في الحقيقة)؛ لأسطح المطابخ والنصب التذكارية.|Полностью чёрный однородный «гранит» (на самом деле габбро); для столешниц и памятников.
black_galaxy|بلاك غالاكسي|Блэк Гэлакси|Black stone with sparkling golden flecks (bronzite) that look like a starry sky.|حجر أسود بنقاط ذهبية لامعة (برونزيت) تشبه السماء المرصعة بالنجوم.|Чёрный камень с золотистыми блёстками (бронзит), похожий на звёздное небо.
kashmir_white|كشمير وايت|Кашмир Уайт|White granite with red garnet and grey specks.|غرانيت أبيض بنقاط حمراء من العقيق ورمادية.|Белый гранит с красными гранатами и серыми вкраплениями.
tan_brown|تان براون|Тан Браун|Dark brown granite with black grains; common for kitchen countertops.|غرانيت بني داكن بحبيبات سوداء؛ شائع لأسطح المطابخ.|Тёмно-коричневый гранит с чёрными зёрнами; популярен для кухонных столешниц.
baltic_brown|بالتيك براون|Балтик Браун|Rapakivi granite with large round brown feldspar crystals.|غرانيت راباكيفي ببلورات فلسبار بنية مستديرة كبيرة.|Гранит рапакиви с крупными округлыми коричневыми кристаллами полевого шпата.
blue_pearl|بلو بيرل (لارفيكيت)|Блю Перл (ларвикит)|Igneous stone with feldspar crystals that flash blue (labradorescence).|حجر ناري ببلورات فلسبار تتلألأ بالأزرق (لابرادوريسنس).|Магматический камень с кристаллами полевого шпата, переливающимися синим (лабрадоресценция).
giallo_ornamental|جيالو أورنامنتال|Джалло Орнаментал|Golden-yellow granite with brown and black specks.|غرانيت أصفر ذهبي بنقاط بنية وسوداء.|Золотисто-жёлтый гранит с коричневыми и чёрными вкраплениями.
ubatuba|أوباتوبا|Убатуба|Dark green to black granite with golden grains.|غرانيت أخضر داكن إلى أسود بحبيبات ذهبية.|Тёмно-зелёный или чёрный гранит с золотистыми зёрнами.
rosa_porrino|روزا بورينيو|Роза Порриньо|Pink granite with grey grains; for facades and landscaping.|غرانيت وردي بحبيبات رمادية؛ للواجهات والمساحات الخارجية.|Розовый гранит с серыми зёрнами; для фасадов и благоустройства.
bianco_sardo|بيانكو ساردو|Бьянко Сардо|Light grey granite with black specks.|غرانيت رمادي فاتح بنقاط سوداء.|Светло-серый гранит с чёрными вкраплениями.
impala_black|إمبالا بلاك|Импала Блэк|Dark grey to black norite; very durable for facades.|نوريت رمادي داكن إلى أسود؛ شديد التحمل للواجهات.|Тёмно-серый или чёрный норит; очень долговечен для фасадов.
zimbabwe_black|زيمبابوي بلاك|Зимбабве Блэк|Uniform black gabbro with a very high polish.|غابرو أسود متجانس بلمعان عالٍ جداً.|Однородное чёрное габбро с очень высокой полировкой.
shanxi_black|شانشي بلاك|Шаньси Блэк|Fine-grained, uniform black granite.|غرانيت أسود دقيق الحبيبات ومتجانس.|Мелкозернистый однородный чёрный гранит.
g603|غرانيت G603|Гранит G603|Inexpensive, widely used light grey granite for paving.|غرانيت رمادي فاتح رخيص وواسع الاستخدام للرصف.|Недорогой и широко используемый светло-серый гранит для мощения.
g654|غرانيت G654|Гранит G654|Dark grey granite for paving, stairs and kerbs.|غرانيت رمادي داكن للرصف والدرج والأرصفة.|Тёмно-серый гранит для мощения, лестниц и бордюров.
taj_mahal|كوارتزيت تاج محل|Кварцит Тадж-Махал|Light cream quartzite with soft golden veins; looks like marble with granite's strength.|كوارتزيت كريمي فاتح بعروق ذهبية ناعمة؛ مظهر الرخام بصلابة الغرانيت.|Светло-кремовый кварцит с мягкими золотистыми прожилками: вид мрамора, прочность гранита.
mont_blanc|كوارتزيت مون بلان|Кварцит Монблан|White and grey quartzite with parallel veins.|كوارتزيت أبيض ورمادي بعروق متوازية.|Бело-серый кварцит с параллельными прожилками.
azul_macaubas|أزول ماكاوباس|Азул Макаубас|Sky-blue quartzite; very rare.|كوارتزيت أزرق سماوي؛ نادر جداً.|Небесно-голубой кварцит; очень редкий.
fusion_quartzite|كوارتزيت فيوجن|Кварцит Фьюжн|Multicoloured quartzite mixing blue, green and orange.|كوارتزيت متعدد الألوان يمزج الأزرق والأخضر والبرتقالي.|Многоцветный кварцит с сочетанием синего, зелёного и оранжевого.
portland_stone|حجر بورتلاند|Портлендский камень|White to cream limestone; St Paul's Cathedral and many London buildings are built of it.|حجر جيري أبيض إلى كريمي؛ بُنيت منه كاتدرائية القديس بولس وكثير من مباني لندن.|Белый или кремовый известняк; из него построены собор Святого Павла и многие здания Лондона.
bath_stone|حجر باث|Батский камень|Honey-coloured oolitic limestone from which the historic city of Bath is built.|حجر جيري بطروخي بلون العسل بُنيت منه مدينة باث التاريخية.|Оолитовый известняк медового цвета, из которого построен исторический город Бат.
jerusalem_stone|حجر القدس|Иерусалимский камень|Golden-cream limestone and dolomite used in the region since antiquity.|حجر جيري ودولوميت كريمي ذهبي يُستخدم في المنطقة منذ القدم.|Золотисто-кремовый известняк и доломит, используемые в регионе с древности.
indiana_limestone|حجر إنديانا الجيري|Индианский известняк|Cream limestone used to clad the Empire State Building and the Pentagon.|حجر جيري كريمي كُسيت به ناطحة إمباير ستيت والبنتاغون.|Кремовый известняк, которым облицованы Эмпайр-стейт-билдинг и Пентагон.
caen_stone|حجر كان|Канский камень|Cream limestone used in cathedrals and parts of the Tower of London.|حجر جيري كريمي استُخدم في الكاتدرائيات وأجزاء من برج لندن.|Кремовый известняк, использованный в соборах и частях Тауэра.
moleanos|موليانوس|Моленуш|Beige limestone with fine parallel veins; common for facades and floors.|حجر جيري بيج بعروق متوازية رفيعة؛ شائع للواجهات والأرضيات.|Бежевый известняк с тонкими параллельными прожилками; популярен для фасадов и полов.
coralina|حجر مرجاني|Коралловый камень|Coral limestone with coral and shell fossils; for coastal spaces and pools.|حجر جيري مرجاني بأحافير المرجان والأصداف؛ للمساحات الساحلية والمسابح.|Коралловый известняк с окаменелыми кораллами и ракушками; для побережья и бассейнов.
rainbow_sandstone|حجر رملي قوس قزح|Песчаник «Радуга»|Sandstone with cream, pink and brown bands.|حجر رملي بأشرطة كريمية ووردية وبنية.|Песчаник с кремовыми, розовыми и коричневыми полосами.
dholpur|حجر دولبور الرملي|Песчаник Дхолпур|Pink to red sandstone used in New Delhi landmarks such as the Presidential Palace.|حجر رملي وردي إلى أحمر استُخدم في معالم نيودلهي مثل القصر الرئاسي.|Розовый или красный песчаник, использованный в зданиях Нью-Дели, например в президентском дворце.
hawkesbury|حجر سيدني الرملي|Сиднейский песчаник|Golden-yellow sandstone with iron-rich layers; the identity of Sydney's old architecture.|حجر رملي أصفر ذهبي بطبقات غنية بالحديد؛ هوية عمارة سيدني القديمة.|Золотисто-жёлтый песчаник с железистыми слоями; символ старой архитектуры Сиднея.
brownstone|براونستون|Браунстоун|Dark brown sandstone of New York's famous townhouses.|حجر رملي بني داكن بُنيت منه بيوت نيويورك الشهيرة.|Тёмно-коричневый песчаник знаменитых нью-йоркских домов.
yorkstone|حجر يورك|Йоркский камень|Grey to brown sandstone for pavement paving.|حجر رملي رمادي إلى بني لرصف الأرصفة.|Серый или коричневый песчаник для мощения тротуаров.
welsh_slate|أردواز ويلز|Валлийский сланец|Blue-grey slate, a UNESCO World Heritage site, roofing many cities around the world.|أردواز رمادي مزرق، موقع تراث عالمي لليونسكو، يغطي أسطح مدن كثيرة حول العالم.|Сине-серый сланец, объект Всемирного наследия ЮНЕСКО; им покрыты крыши многих городов мира.
spanish_slate|أردواز إسباني|Испанский сланец|Black slate from the world's largest producer, for roofing.|أردواز أسود من أكبر منتج في العالم لتغطية الأسطح.|Чёрный сланец от крупнейшего в мире производителя, для кровли.
brazilian_slate|أردواز برازيلي|Бразильский сланец|Grey to green slate for floors and walls.|أردواز رمادي إلى أخضر للأرضيات والجدران.|Серый или зелёный сланец для полов и стен.
vermont_slate|أردواز فيرمونت|Вермонтский сланец|Slate in purple, green and red.|أردواز بألوان البنفسجي والأخضر والأحمر.|Сланец фиолетового, зелёного и красного цветов.
basaltina|بازالتينا|Базальтина|Grey basalt with fine pores; for paving and facades.|بازلت رمادي بمسام دقيقة؛ للرصف والواجهات.|Серый базальт с мелкими порами; для мощения и фасадов.
etna_lava|حجر حمم إتنا|Лавовый камень Этны|Dark volcanic stone that paves the streets of Catania.|حجر بركاني داكن رُصفت به شوارع كاتانيا.|Тёмный вулканический камень, которым вымощены улицы Катании.
g684|بازلت G684|Базальт G684|Inexpensive black basalt for paving and kerbs.|بازلت أسود رخيص للرصف والأرصفة.|Недорогой чёрный базальт для мощения и бордюров.
verde_guatemala|فيردي غواتيمالا|Верде Гватемала|Dark green stone with white veins; despite the name, it is quarried in India.|حجر أخضر داكن بعروق بيضاء؛ رغم اسمه يُستخرج في الهند.|Тёмно-зелёный камень с белыми прожилками; несмотря на название, добывается в Индии.
verde_alpi|فيردي ألبي|Верде Альпи|Dark green serpentinite with white and light green veins.|سربنتينيت أخضر داكن بعروق بيضاء وخضراء فاتحة.|Тёмно-зелёный серпентинит с белыми и светло-зелёными прожилками.
verde_antico|فيردي أنتيكو|Верде Антико|Green serpentine breccia prized in Roman and Byzantine times.|بريشيا سربنتينية خضراء ثمينة في العصرين الروماني والبيزنطي.|Зелёная серпентиновая брекчия, ценившаяся в римское и византийское время.
rosso_levanto|روسو ليفانتو|Россо Леванто|Wine-red serpentine breccia with white and green veins.|بريشيا سربنتينية حمراء نبيذية بعروق بيضاء وخضراء.|Винно-красная серпентиновая брекчия с белыми и зелёными прожилками.
bianco_lasa|بيانكو لاسا|Бьянко Лаза|Crystalline white marble from the Alps, resistant to weathering.|رخام أبيض بلوري من جبال الألب مقاوم للعوامل الجوية.|Кристаллический белый мрамор из Альп, устойчивый к выветриванию.
calacatta_viola|كالاكاتا فيولا|Калакатта Виола|White marble with bold purple and burgundy veins; very popular in interior design.|رخام أبيض بعروق بنفسجية وخمرية عريضة؛ رائج جداً في التصميم الداخلي.|Белый мрамор с крупными фиолетовыми и бордовыми прожилками; очень популярен в интерьерах.
perlato_sicilia|بيرلاتو صقلية|Перлато Сицилия|Light cream stone with very fine fossils and an even base.|حجر كريمي فاتح بأحافير دقيقة جداً وأرضية متجانسة.|Светло-кремовый камень с очень мелкими окаменелостями и ровным фоном.
grigio_carnico|غريجو كارنيكو|Гриджо Карнико|Dark grey stone with interlaced white veins.|حجر رمادي داكن بعروق بيضاء متشابكة.|Тёмно-серый камень с переплетёнными белыми прожилками.
rosa_norvegia|روزا نورفيجيا|Роза Норвегия|Pink marble with green and grey veins.|رخام وردي بعروق خضراء ورمادية.|Розовый мрамор с зелёными и серыми прожилками.
rosso_francia|أحمر فرنسا|Россо Франция|Red stone with white and grey patches; used in the Palace of Versailles.|حجر أحمر ببقع بيضاء ورمادية؛ استُخدم في قصر فرساي.|Красный камень с белыми и серыми пятнами; использован в Версальском дворце.
grand_antique|غراند أنتيك|Гранд Антик|Black and white breccia with angular fragments; a historic European stone.|بريشيا سوداء وبيضاء بقطع زاوية؛ من الأحجار الأوروبية التاريخية.|Чёрно-белая брекчия с угловатыми обломками; исторический европейский камень.
light_emperador|إمبرادور فاتح|Эмперадор светлый|Lighter Emperador with a honey-brown base and white veins.|نسخة أفتح من الإمبرادور بأرضية بنية عسلية وعروق بيضاء.|Более светлый эмперадор с медово-коричневым фоном и белыми прожилками.
panda_white|باندا وايت|Панда Уайт|White marble with wide, bold black veins; a very graphic look.|رخام أبيض بعروق سوداء عريضة بارزة؛ مظهر تصميمي جداً.|Белый мрамор с широкими выразительными чёрными прожилками; очень графичный.
guangxi_white|أبيض قوانغشي|Гуанси Уайт|White marble with grey veins; a cheaper alternative to Carrara.|رخام أبيض بعروق رمادية؛ بديل أرخص لكارارا.|Белый мрамор с серыми прожилками; более дешёвая альтернатива каррарскому.
ming_green|مينغ غرين|Минг Грин|Light green marble with white and dark green clouds.|رخام أخضر فاتح بغيوم بيضاء وخضراء داكنة.|Светло-зелёный мрамор с белыми и тёмно-зелёными облаками.
ruivina|رويفينا|Руйвина|Grey marble with darker bands.|رخام رمادي بأشرطة أغمق.|Серый мрамор с более тёмными полосами.
black_pearl|بلاك بيرل|Блэк Перл|Black granite with fine silvery grains.|غرانيت أسود بحبيبات فضية دقيقة.|Чёрный гранит с мелкими серебристыми зёрнами.
steel_grey|ستيل غراي|Стил Грей|Uniform dark grey granite; widely used for floors and countertops.|غرانيت رمادي داكن متجانس؛ واسع الاستخدام للأرضيات والأسطح.|Однородный тёмно-серый гранит; широко используется для полов и столешниц.
paradiso|باراديزو|Парадизо|Gneissic granite with purple, grey and pink bands.|غرانيت نايسي بأشرطة بنفسجية ورمادية ووردية.|Гнейсовый гранит с фиолетовыми, серыми и розовыми полосами.
red_multicolor|أحمر متعدد الألوان|Ред Мультиколор|Red granite with black and grey waves and bands.|غرانيت أحمر بموجات وأشرطة سوداء ورمادية.|Красный гранит с чёрными и серыми волнами и полосами.
santa_cecilia|سانتا سيسيليا|Санта Сесилия|Golden-yellow granite with brown grains and red garnet specks.|غرانيت أصفر ذهبي بحبيبات بنية ونقاط حمراء من العقيق.|Золотисто-жёлтый гранит с коричневыми зёрнами и красными гранатами.
blue_bahia|أزول باهيا|Азул Баия|Sky-blue igneous stone with white veins; rare and expensive.|حجر ناري أزرق سماوي بعروق بيضاء؛ نادر وغالي.|Небесно-голубой магматический камень с белыми прожилками; редкий и дорогой.
labrador_antique|لابرادور أنتيك|Лабрадор Антик|Dark granite with large brown and golden crystals.|غرانيت داكن ببلورات بنية وذهبية كبيرة.|Тёмный гранит с крупными коричневыми и золотистыми кристаллами.
rosa_beta|روزا بيتا|Роза Бета|Light pink granite with grey and black grains.|غرانيت وردي فاتح بحبيبات رمادية وسوداء.|Светло-розовый гранит с серыми и чёрными зёрнами.
balmoral_red|بالمورال الأحمر|Балморал Ред|Fine-grained dark red granite for facades and memorials.|غرانيت أحمر داكن دقيق الحبيبات للواجهات والنصب.|Мелкозернистый тёмно-красный гранит для фасадов и памятников.
g664|غرانيت G664|Гранит G664|Inexpensive, widely used pinkish-brown granite.|غرانيت وردي مائل للبني رخيص وواسع الاستخدام.|Недорогой и распространённый розовато-коричневый гранит.
g682|غرانيت G682|Гранит G682|Rusty yellow granite for paving and facades.|غرانيت أصفر صدئي للرصف والواجهات.|Ржаво-жёлтый гранит для мощения и фасадов.
jura_beige|جورا بيج|Юра Беж|Beige limestone with ammonite and belemnite fossils; for floors and facades.|حجر جيري بيج بأحافير الأمونيت والبلمنيت؛ للأرضيات والواجهات.|Бежевый известняк с окаменелыми аммонитами и белемнитами; для полов и фасадов.
vratza|حجر فراتسا الجيري|Врачанский известняк|Light, even cream limestone for facades and floors.|حجر جيري كريمي فاتح متجانس للواجهات والأرضيات.|Светлый ровный кремовый известняк для фасадов и полов.
crema_europa|كريما أوروبا|Крема Европа|Cream limestone with fine parallel veins.|حجر جيري كريمي بعروق متوازية رفيعة.|Кремовый известняк с тонкими параллельными прожилками.
belgian_bluestone|الحجر الأزرق البلجيكي|Бельгийский голубой камень|Blue-grey limestone with small fossils; despite the name "Petit Granit", it is a limestone.|حجر جيري رمادي مزرق بأحافير صغيرة؛ رغم اسمه «بيتي غرانيت» فهو حجر جيري.|Сине-серый известняк с мелкими окаменелостями; несмотря на название «Пти Гранит», это известняк.
chinese_bluestone|الحجر الأزرق الصيني|Китайский голубой камень|Dark grey limestone for paving and pool surrounds.|حجر جيري رمادي داكن للرصف وحواف المسابح.|Тёмно-серый известняк для мощения и бортов бассейнов.
kandla_grey|كاندلا غراي|Кандла Грей|Uniform grey sandstone for paving and sidewalks.|حجر رملي رمادي متجانس للرصف والأرصفة.|Однородный серый песчаник для мощения и тротуаров.
raj_green|راج غرين|Радж Грин|Green sandstone with brown and cream layers.|حجر رملي أخضر بطبقات بنية وكريمية.|Зелёный песчаник с коричневыми и кремовыми слоями.
teakwood|حجر تيك وود الرملي|Песчаник Тиквуд|Sandstone with yellow and brown bands resembling wood grain.|حجر رملي بأشرطة صفراء وبنية تشبه نقوش الخشب.|Песчаник с жёлтыми и коричневыми полосами, напоминающими текстуру дерева.
modak|حجر موداك الرملي|Песчаник Модак|Pink to red sandstone with yellow bands.|حجر رملي وردي إلى أحمر بأشرطة صفراء.|Розовый или красный песчаник с жёлтыми полосами.
autumn_brown|أوتم براون|Отем Браун|Brown sandstone with autumn-coloured bands.|حجر رملي بني بأشرطة بألوان الخريف.|Коричневый песчаник с осенними полосами.
navona|ترافرتين نافونا|Травертин Навона|Cream travertine with fine pores from historic quarries near Rome.|ترافرتين كريمي بمسام دقيقة من محاجر تاريخية قرب روما.|Кремовый травертин с мелкими порами из исторических карьеров под Римом.
persian_walnut|ترافرتين إيراني جوزي|Иранский ореховый травертин|Walnut-brown travertine with coloured bands; an Iranian export travertine.|ترافرتين بني جوزي بأشرطة ملونة؛ من أنواع الترافرتين الإيراني المصدَّرة.|Орехово-коричневый травертин с цветными полосами; иранский экспортный травертин.
peru_travertine|ترافرتين بيرو|Перуанский травертин|Cream to golden travertine from the Andes.|ترافرتين كريمي إلى ذهبي من جبال الأنديز.|Кремовый или золотистый травертин из Анд.
white_macaubas|ماكاوباس الأبيض|Белый Макаубас|White quartzite with delicate grey bands; very hard and low-absorbing.|كوارتزيت أبيض بأشرطة رمادية رقيقة؛ شديد الصلابة قليل الامتصاص.|Белый кварцит с тонкими серыми полосами; очень твёрдый и мало впитывает воду.
patagonia|باتاغونيا|Патагония|Multicoloured quartzite with cream, brown and translucent patches; good for backlighting.|كوارتزيت متعدد الألوان بقطع كريمية وبنية وشفافة؛ مناسب للإضاءة الخلفية.|Многоцветный кварцит с кремовыми, коричневыми и прозрачными участками; хорош для подсветки.
cristallo|كريستالو|Кристалло|Translucent white quartzite with large crystals; for backlighting and luxury spaces.|كوارتزيت أبيض شفاف ببلورات كبيرة؛ للإضاءة الخلفية والمساحات الفاخرة.|Полупрозрачный белый кварцит с крупными кристаллами; для подсветки и роскошных интерьеров.
sea_pearl|سي بيرل|Си Перл|Grey quartzite with white and silver veins.|كوارتزيت رمادي بعروق بيضاء وفضية.|Серый кварцит с белыми и серебристыми прожилками.
perla_venata|بيرلا فيناتا|Перла Вената|White quartzite with marble-like grey veins.|كوارتزيت أبيض بعروق رمادية تشبه الرخام.|Белый кварцит с серыми прожилками, как у мрамора.
persian_red_onyx|أونيكس إيراني أحمر|Иранский красный оникс|Red and orange onyx with wavy bands; for backlit walls and tables.|أونيكس أحمر وبرتقالي بأشرطة متموجة؛ للجدران والطاولات المضاءة.|Красно-оранжевый оникс с волнистыми полосами; для стен и столов с подсветкой.
"""

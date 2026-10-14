#!/usr/bin/env python3
"""Builds app/src/main/assets/seed.json from the tables below.

Edit the TYPES / STONES tables and run:  python3 tools/build_seed.py
Bump SEED_VERSION whenever the data changes so installed apps re-import it.

Lab values belong to the stone *type* and are typical ranges taken from the
ASTM dimension-stone specifications (C615, C503, C1527, C568, C616, C629, C1526)
and general literature. They are representative, not quarry test results.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import i18n_data as T  # noqa: E402

SEED_VERSION = 3

# id: (fa, en, description, density kg/m3, water absorption %, compressive MPa,
#      flexural MPa, mohs, acid reaction, standard, default finishes, default uses, wiki)
TYPES = [
    ("granite", "گرانیت", "Granite",
     "سنگ آذرین درونی و درشت‌دانه از کوارتز، فلدسپار و میکا. در بازار سنگ، گابرو، دیوریت و نوریت را هم «گرانیت» می‌نامند. بسیار سخت و کم‌جذب است و برای نما، کف پرتردد، پله و صفحهٔ کابینت مناسب است.",
     (2560, 2750), (0.1, 0.4), (130, 250), (10, 20), (6, 7), "none", "ASTM C615",
     "pol,hon,fla,bus,lea,san", "fl,wl,fa,pv,ct,st", "Granite"),
    ("marble", "مرمر (ماربل)", "Marble",
     "سنگ دگرگونی حاصل از تبلور دوبارهٔ سنگ آهک. بلورهای کلسیت درهم‌قفل‌شده به آن جلای زیبا و رگه‌های مشخص می‌دهند. به اسید حساس است و برای فضای داخلی بهترین کارایی را دارد.",
     (2595, 2800), (0.1, 0.2), (70, 140), (7, 20), (3, 4), "strong", "ASTM C503",
     "pol,hon,tum,lea", "fl,wl,st,mo", "Marble"),
    ("dolomitic", "چینی و کریستال (مرمر دولومیتی)", "Dolomitic marble",
     "مرمر دولومیتی سفید و بلورین که در بازار ایران «چینی» یا «کریستال» نامیده می‌شود. از مرمر کلسیتی کمی سخت‌تر و کم‌جذب‌تر است و با اسید سرد فقط به صورت پودر می‌جوشد.",
     (2700, 2870), (0.1, 0.3), (80, 150), (8, 15), (3.5, 4), "weak", "ASTM C503",
     "pol,hon,tum", "fl,wl,st,mo", "Dolomite (rock)"),
    ("marmarite", "مرمریت (سنگ آهک متراکم)", "Compact limestone (commercial marble)",
     "سنگ آهک متراکمی که صیقل‌پذیر است و در بازار ایران «مرمریت» و در بازار جهانی گاهی «ماربل» نامیده می‌شود. فسیل‌ها و رگه‌های کلسیتی در آن رایج است.",
     (2500, 2700), (0.2, 1.0), (60, 130), (6, 12), (3, 4), "strong", "ASTM C568 (high density)",
     "pol,hon,tum,bus", "fl,wl,fa,st", "Limestone"),
    ("travertine", "تراورتن", "Travertine",
     "سنگ آهکی رسوبی که از چشمه‌های آب گرم تشکیل می‌شود و حفره‌ها و لایه‌بندی موجی مشخص دارد. ایران از بزرگ‌ترین تولیدکنندگان آن است. حفره‌ها معمولاً با رزین یا سیمان «فیلر» می‌شوند.",
     (2305, 2600), (0.5, 2.5), (52, 100), (6.9, 12), (3, 4), "strong", "ASTM C1527",
     "pol,hon,fil,tum,san,bus", "fl,wl,fa,pv,st", "Travertine"),
    ("onyx", "مرمر سنگ (اونیکس)", "Onyx marble",
     "کلسیت یا آراگونیت نواری و نیمه‌شفاف که در غارها و چشمه‌ها رسوب می‌کند. نور را از خود عبور می‌دهد و برای دیوارهای بک‌لایت و تزئینات لوکس استفاده می‌شود. نرم و شکننده است و فقط برای داخل ساختمان توصیه می‌شود.",
     (2600, 2750), (0.1, 0.5), (50, 100), (6, 12), (3, 3), "strong", "ASTM C503 (روش آزمون)",
     "pol,hon", "wl,bl,mo", "Onyx marble"),
    ("limestone", "سنگ آهک", "Limestone",
     "سنگ رسوبی کربناته با تخلخل متوسط که آسان تراشیده می‌شود. بسیاری از بناهای تاریخی جهان از آن ساخته شده‌اند. مقاومت و جذب آب آن به چگالی بستگی زیادی دارد.",
     (2160, 2560), (3.0, 7.5), (28, 55), (3.4, 7), (3, 3), "strong", "ASTM C568",
     "hon,san,bus,spl,tum", "wl,fa,pv,mo", "Limestone"),
    ("sandstone", "ماسه‌سنگ", "Sandstone",
     "سنگ رسوبی از دانه‌های ماسه (عمدتاً کوارتز) که با سیمان طبیعی به هم چسبیده‌اند. سطح زبر و ضدلغزش دارد و برای محوطه و نما مناسب است.",
     (2003, 2600), (2.0, 8.0), (27, 140), (2.4, 14), (6, 7), "none", "ASTM C616",
     "spl,hon,san,tum", "fa,pv,wl", "Sandstone"),
    ("quartzite", "کوارتزیت", "Quartzite",
     "ماسه‌سنگ کوارتزی دگرگون‌شده؛ از گرانیت هم سخت‌تر است و ظاهری شبیه مرمر دارد. برای صفحهٔ کابینت و کف پرتردد بسیار مقاوم است.",
     (2560, 2700), (0.1, 1.0), (140, 300), (13, 25), (7, 7), "none", "ASTM C616 (quartzite)",
     "pol,hon,lea", "fl,wl,ct,fa,st", "Quartzite"),
    ("slate", "اسلیت", "Slate",
     "سنگ دگرگونی ریزدانه که به ورقه‌های نازک و صاف شکافته می‌شود. برای پوشش بام، کف و دیوار با سطح طبیعی استفاده می‌شود.",
     (2700, 2800), (0.25, 0.45), (100, 200), (49, 62), (3, 4), "none", "ASTM C629",
     "spl,hon", "rf,fl,wl,pv", "Slate"),
    ("basalt", "بازالت و سنگ‌های آتشفشانی", "Basalt and volcanic stone",
     "سنگ آذرین بیرونی تیره و ریزدانه. بسیار مقاوم در برابر سایش و یخ‌زدگی است و برای کف‌پوش محوطه، جدول و نما به کار می‌رود.",
     (2700, 3000), (0.1, 1.0), (150, 300), (15, 25), (6, 6), "none", "ASTM C615 (روش آزمون)",
     "hon,fla,bus,san,spl", "pv,fa,fl,st", "Basalt"),
    ("serpentinite", "سرپانتینیت (مرمر سبز)", "Serpentinite (green marble)",
     "سنگ دگرگونی سبزرنگ از کانی‌های گروه سرپانتین که در بازار «مرمر سبز» یا «وردی» نامیده می‌شود. معمولاً با اسید واکنش نمی‌دهد مگر رگه‌های کلسیتی داشته باشد.",
     (2600, 2800), (0.1, 0.6), (80, 200), (8, 20), (3, 5), "none", "ASTM C1526",
     "pol,hon", "fl,wl,ct", "Serpentinite"),
]

# Pattern codes: vein (رگه‌دار), cloud (ابری), uni (یکنواخت), grain (دانه‌ای/خال‌دار),
#                pore (حفره‌دار), band (نواری/لایه‌ای)
# Color codes:   wh cr ye bn rd pk gn bl gy bk  (see Palette.kt)
# Columns: id | fa | en | aliases | type | color | pattern | region (fa) | country (fa) |
#          finishes override | uses override | description | wiki title (specific article, optional)
STONES = """
mahallat_cream|تراورتن کرم محلات|Mahallat Cream Travertine|محلات کرم، Persian cream travertine|travertine|cr|pore|محلات، استان مرکزی|ایران|||از شناخته‌شده‌ترین تراورتن‌های ایران با زمینهٔ کرم روشن و لایه‌بندی موجی؛ برای نمای ساختمان‌های مسکونی بسیار رایج است.|
atashkooh|تراورتن آتشکوه|Atashkooh Travertine|آتش‌کوه|travertine|cr|pore|دلیجان، استان مرکزی|ایران|||تراورتن کرم تا بژ با حفره‌های ریز و بافت نسبتاً یکنواخت؛ برای کف و نما استفاده می‌شود.|
abbasabad|تراورتن عباس‌آباد|Abbas Abad Travertine|عباس آباد|travertine|cr|pore|استان اصفهان|ایران|||تراورتن روشن با زمینهٔ شیری تا کرم؛ از تراورتن‌های پرمصرف نمای ساختمان در ایران.|
azarshahr_red|تراورتن قرمز آذرشهر|Azarshahr Red Travertine|قرمز آذرشهر، Persian red travertine|travertine|rd|band|آذرشهر، آذربایجان شرقی|ایران|||تراورتن قرمز تا نارنجی با نوارهای رنگی؛ از گونه‌های کمیاب و صادراتی ایران.|
azarshahr_yellow|تراورتن لیمویی آذرشهر|Azarshahr Yellow Travertine|لیمویی آذرشهر، Persian yellow travertine|travertine|ye|band|آذرشهر، آذربایجان شرقی|ایران|||تراورتن زرد لیمویی با لایه‌بندی موجی؛ برای نما و کف جلوهٔ گرمی ایجاد می‌کند.|
silver_travertine|تراورتن نقره‌ای|Silver Travertine|سیلور، Grey travertine|travertine|gy|band|منطقهٔ دنیزلی|ترکیه|||تراورتن خاکستری تا نقره‌ای با رگه‌های موازی؛ در برش موازی لایه‌ها ظاهر خطی پیدا می‌کند.|
denizli_walnut|تراورتن گردویی دنیزلی|Denizli Noce Travertine|نوچه، Walnut travertine, Noce|travertine|bn|pore|دنیزلی|ترکیه|||تراورتن قهوه‌ای گردویی با تنوع رنگ گرم؛ برای کف و دیوار به صورت آنتیک (تامبل) محبوب است.|
denizli_light|تراورتن لایت دنیزلی|Denizli Light Travertine|Classic travertine, Light travertine|travertine|cr|pore|دنیزلی|ترکیه|||تراورتن کرم روشن کلاسیک؛ از پرفروش‌ترین تراورتن‌های بازار جهانی.|
travertino_romano|تراورتن رومی|Travertino Romano|تراورتینو رومانو، Tivoli travertine|travertine|cr|pore|تیوولی، لاتزیو|ایتالیا|||تراورتن تاریخی رم که کولوسئوم و میدان سن‌پیتر با آن ساخته شده‌اند.|Travertine
carrara|مرمر کارارا|Bianco Carrara|کارارا سفید، Carrara white|marble|wh|vein|کارارا، توسکانی|ایتالیا|||مرمر سفید تا خاکستری روشن با رگه‌های ظریف خاکستری؛ مشهورترین مرمر جهان که از دوران روم استخراج می‌شود.|Carrara marble
statuario|استاتواریو|Statuario|استچواری، Statuary marble|marble|wh|vein|کارارا، توسکانی|ایتالیا|||مرمر سفید خالص با رگه‌های پررنگ خاکستری؛ سنگ مجسمه‌سازی کلاسیک و از گران‌ترین مرمرها.|
calacatta|کالاکاتا|Calacatta|کلکته، Calacatta Oro|marble|wh|vein|کارارا، توسکانی|ایتالیا|||مرمر سفید با رگه‌های درشت طلایی تا خاکستری؛ نماد فضاهای لوکس.|
arabescato|عربسکاتو|Arabescato|Arabescato Carrara|marble|wh|vein|کارارا، توسکانی|ایتالیا|||مرمر سفید با رگه‌های خاکستری درهم و نامنظم.|
bardiglio|باردیلیو|Bardiglio|Bardiglio Carrara|marble|gy|vein|کارارا، توسکانی|ایتالیا|||مرمر خاکستری آبی‌فام با رگه‌های تیره‌تر از معادن کارارا.|
pentelic|مرمر پنتلیک|Pentelic marble|پنتلیکون|marble|wh|uni|کوه پنتلی، آتیکا|یونان|||مرمر سفید ریزدانه با ته‌رنگ طلایی ملایم؛ سنگ ساخت پارتنون آتن.|Pentelic marble
volakas|ولاکاس|Volakas|Jazz white|marble|wh|vein|دراما|یونان|||مرمر سفید با رگه‌های خاکستری کم‌رنگ؛ جایگزین رایج مرمرهای ایتالیایی.|
makrana|مرمر مکرانا|Makrana marble|Makrana white|marble|wh|uni|مکرانا، راجستان|هند|||مرمر سفید که تاج‌محل با آن ساخته شده است.|Makrana marble
afyon_white|سفید آفیون|Afyon White|Afyon Beyaz|marble|wh|uni|آفیون‌قره‌حصار|ترکیه|||مرمر سفید شیری با بافت یکنواخت.|
marmara_white|مرمر جزیرهٔ مرمره|Marmara White|Marmara Equator|marble|wh|band|جزیرهٔ مرمره، بالیکسیر|ترکیه|||مرمر سفید با نوارهای خاکستری موازی؛ دریای مرمره نام خود را از این معادن گرفته است.|
estremoz|مرمر استرموز|Estremoz marble|Rosa Portogallo, Rosa Aurora|marble|pk|cloud|استرموز، آلنتژو|پرتغال|||مرمر صورتی تا کرم با ابرهای ملایم؛ از معادن قدیمی پرتغال.|Estremoz marble
nero_marquina|نرو مارکینا|Nero Marquina|مشکی مارکینا، Black Marquina|marble|bk|vein|مارکینا، باسک|اسپانیا|||سنگ مشکی با رگه‌های سفید درخشان؛ از محبوب‌ترین سنگ‌های مشکی در طراحی داخلی.|
nero_portoro|نرو پورتورو|Nero Portoro|Portoro|marble|bk|vein|پورتووِنِره، لیگوریا|ایتالیا|||سنگ مشکی با رگه‌های طلایی؛ کمیاب و گران‌قیمت.|
azna_chini|چینی ازنا|Azna Crystal White|چینی کریستال ازنا، Persian crystal white|dolomitic|wh|uni|ازنا، لرستان|ایران|||مرمر دولومیتی سفید و بلورین با درخشش بالا؛ از شناخته‌شده‌ترین سنگ‌های چینی ایران.|
neyriz_chini|چینی نی‌ریز|Neyriz White|چینی نیریز|dolomitic|wh|cloud|نی‌ریز، فارس|ایران|||سنگ چینی سفید با ابرهای خاکستری بسیار ملایم؛ برای کف و دیوار داخلی.|
dorud_chini|چینی درود|Dorud Crystal|کریستال درود|dolomitic|wh|vein|درود، لرستان|ایران|||چینی سفید با رگه‌های خاکستری ظریف.|
thassos|سفید تاسوس|Thassos White|Snow white, Thassos|dolomitic|wh|uni|جزیرهٔ تاسوس|یونان|||از سفیدترین سنگ‌های جهان با بلورهای درخشان؛ مرمر دولومیتی بسیار خالص.|
sivec|سیوِک|Sivec|Sivec white|dolomitic|wh|uni|پریلپ|مقدونیهٔ شمالی|||مرمر دولومیتی سفید ریزدانه شبیه تاسوس.|
dehbid|مرمریت دهبید|Dehbid Marble|دهبید کرم، Persian beige|marmarite|cr|cloud|دهبید، فارس|ایران|||مرمریت کرم تا بژ با ابرهای قهوه‌ای روشن؛ از مرمریت‌های پرکاربرد کف ساختمان در ایران.|
harsin|مرمریت هرسین|Harsin Marble|هرسین کرم|marmarite|cr|uni|هرسین، کرمانشاه|ایران|||مرمریت کرم یکنواخت با درصد ضایعات کم؛ برای کف‌سازی بسیار رایج است.|
gohareh|مرمریت گوهره|Gohareh Marble|گوهره خرم‌آباد|marmarite|wh|cloud|خرم‌آباد، لرستان|ایران|||مرمریت سفید تا شیری با ابرهای ملایم.|
kermanshah_limestone|لایمستون کرمانشاه|Kermanshah Limestone|لایمستون کرم کرمانشاه، Persian cream limestone, NexStone limestone|limestone|cr|uni|کرمانشاه، استان کرمانشاه|ایران|pol,hon,bus,san,spl|fa,fl,wl,pv|سنگ آهک رسوبی از کربنات کلسیم با زمینهٔ کرم تا بژ روشن و بافت یکنواخت. ظاهر آرام و فرآوری‌پذیری بالا آن را برای نمای ساختمان‌های فاخر، کف و دیوارپوش داخلی مناسب کرده است. به صورت کوپ، اسلب، تایل و برش در ابعاد سفارشی عرضه می‌شود.|
jowshaqan|مرمریت جوشقان|Jowshaqan Marble|جوشقان|marmarite|cr|cloud|جوشقان، اصفهان|ایران|||مرمریت کرم روشن؛ برای کف و پله استفاده می‌شود.|
lashtar|مرمریت لاشتر|Lashtar Marble|لاشتر|marmarite|cr|uni|لاشتر، اصفهان|ایران|||مرمریت کرم با بافت ریز و یکنواخت.|
abadeh|مرمریت آباده|Abadeh Marble|سنگ آباده|marmarite|cr|cloud|آباده، فارس|ایران|||مرمریت روشن با ابرهای کرم؛ از معادن قدیمی جنوب ایران.|
crema_marfil|کرم مارفیل|Crema Marfil|کرما مارفیل|marmarite|cr|vein|آلیکانته، والنسیا|اسپانیا|||سنگ کرم عاجی با رگه‌های ظریف؛ از پرفروش‌ترین سنگ‌های جهان.|
emperador|امپرادور|Emperador Dark|امپرادور تیره، Marron Imperial|marmarite|bn|vein|لا ریوخا|اسپانیا|||سنگ قهوه‌ای تیره با شبکه‌ای از رگه‌های کلسیتی روشن.|
rojo_alicante|قرمز آلیکانته|Rojo Alicante|Rosso Alicante|marmarite|rd|vein|آلیکانته، والنسیا|اسپانیا|||سنگ قرمز آجری با رگه‌های سفید.|
botticino|بوتیچینو|Botticino|Botticino Classico|marmarite|cr|cloud|برشا، لمباردی|ایتالیا|||سنگ کرم با ابرها و فسیل‌های ریز؛ بنای یادبود ویکتور امانوئل دوم در رم با آن ساخته شده است.|
rosso_verona|قرمز ورونا|Rosso Verona|Rosso Ammonitico|marmarite|rd|cloud|ورونا، ونتو|ایتالیا|||سنگ آهک قرمز با فسیل آمونیت؛ در بناهای تاریخی ورونا فراوان است.|Rosso Ammonitico Veronese
burdur_beige|بژ بوردور|Burdur Beige|Burdur Bej|marmarite|cr|uni|بوردور|ترکیه|||سنگ بژ یکنواخت که در بازار جهانی به عنوان ماربل عرضه می‌شود.|
yazd_onyx|مرمر سنگ یزد|Yazd Onyx|اونیکس یزد، Persian onyx|onyx|ye|band|استان یزد|ایران|||مرمر سنگ زرد عسلی تا سفید با نوارهای موجی؛ نیمه‌شفاف و مناسب دیوار بک‌لایت.|
persian_white_onyx|اونیکس سفید ایران|Persian White Onyx|اونیکس سفید|onyx|wh|band|ایران|ایران|||مرمر سنگ سفید با نوارهای کرم؛ عبور نور زیاد.|
persian_pink_onyx|اونیکس صورتی ایران|Persian Pink Onyx|اونیکس صورتی|onyx|pk|band|ایران|ایران|||مرمر سنگ صورتی با نوارهای سفید و کرم؛ برای فضاهای لوکس و نورپردازی.|
green_onyx_pakistan|اونیکس سبز پاکستان|Pakistan Green Onyx|Afghan green onyx|onyx|gn|band|بلوچستان|پاکستان|||مرمر سنگ سبز روشن با رگه‌های قهوه‌ای؛ برای اشیای تزئینی و دیوار.|
mexican_onyx|اونیکس مکزیک|Mexican Onyx|Honey onyx, Tecali|onyx|ye|band|توکالی، پوئبلا|مکزیک|||مرمر سنگ عسلی تا سبز با نوارهای شفاف.|
natanz_granite|گرانیت نطنز|Natanz Granite|نطنز|granite|gy|grain|نطنز، اصفهان|ایران|||گرانیت خاکستری روشن با خال‌های مشکی (نمک‌فلفلی)؛ از پرمصرف‌ترین گرانیت‌های ایران برای کف و پله.|
zahedan_granite|گرانیت زاهدان|Zahedan Granite|زاهدان|granite|gy|grain|زاهدان، سیستان و بلوچستان|ایران|||گرانیت خاکستری با دانه‌های متوسط؛ برای نما و کف محوطه.|
shirkuh_red|گرانیت قرمز یزد (شیرکوه)|Yazd Red Granite|قرمز یزد، شیرکوه|granite|pk|grain|شیرکوه، یزد|ایران|||گرانیت صورتی تا قرمز با فلدسپارهای درشت.|
malayer_granite|گرانیت ملایر|Malayer Granite|ملایر|granite|gy|grain|ملایر، همدان|ایران|||گرانیت خاکستری روشن تا سفید؛ برای پله و کف.|
nehbandan_granite|گرانیت نهبندان|Nehbandan Granite|نهبندان|granite|gy|grain|نهبندان، خراسان جنوبی|ایران|||گرانیت خاکستری از شرق ایران؛ برای کف‌پوش و نما.|
absolute_black|ابسولوت بلک|Absolute Black|مشکی مطلق، Black granite|granite|bk|uni|کارناتاکا|هند|||گرانیت (در واقع گابرو) کاملاً مشکی و یکنواخت؛ برای صفحهٔ کابینت و سنگ یادبود.|
black_galaxy|بلک گلکسی|Black Galaxy|گلکسی مشکی|granite|bk|grain|اونگول، آندرا پرادش|هند|||سنگ مشکی با ذرات طلایی درخشان (برونزیت) که شبیه آسمان پرستاره است.|
kashmir_white|کشمیر وایت|Kashmir White|کشمیر سفید|granite|wh|grain|تامیل نادو|هند|||گرانیت سفید با خال‌های قرمز گارنت و خاکستری.|
tan_brown|تن براون|Tan Brown|قهوه‌ای هندی|granite|bn|grain|تلنگانه|هند|||گرانیت قهوه‌ای تیره با دانه‌های مشکی؛ برای کابینت آشپزخانه رایج است.|
baltic_brown|بالتیک براون|Baltic Brown|بالتیک قهوه‌ای، Rapakivi|granite|bn|grain|یلاروی|فنلاند|||گرانیت راپاکیوی با دایره‌های درشت فلدسپار قهوه‌ای.|Rapakivi granite
blue_pearl|بلو پرل (لارویکیت)|Blue Pearl|Larvikite, Labrador blue|granite|bl|grain|لارویک|نروژ|||سنگ آذرین با بلورهای فلدسپار که درخشش آبی (لابرادورسانس) دارند.|Larvikite
giallo_ornamental|جیالو اورنامنتال|Giallo Ornamental|زرد برزیلی|granite|ye|grain|اسپیریتو سانتو|برزیل|||گرانیت زرد طلایی با خال‌های قهوه‌ای و مشکی.|
ubatuba|اوباتوبا|Verde Ubatuba|سبز اوباتوبا|granite|gn|grain|اوباتوبا، سائوپائولو|برزیل|||گرانیت سبز تیره تا مشکی با دانه‌های طلایی.|
rosa_porrino|رزا پورینو|Rosa Porriño|صورتی پورینو|granite|pk|grain|پورینو، گالیسیا|اسپانیا|||گرانیت صورتی با دانه‌های خاکستری؛ برای نما و محوطه.|
bianco_sardo|بیانکو ساردو|Bianco Sardo|سفید ساردینیا|granite|gy|grain|ساردینیا|ایتالیا|||گرانیت خاکستری روشن با خال‌های مشکی.|
impala_black|ایمپالا بلک|Impala Black|Rustenburg, Nero Impala|granite|bk|grain|روستنبورگ|آفریقای جنوبی|||نوریت خاکستری تیره تا مشکی؛ بسیار مقاوم برای نما.|
zimbabwe_black|زیمباوه بلک|Zimbabwe Black|Nero Assoluto Zimbabwe|granite|bk|uni|منطقهٔ موتوکو|زیمباوه|||گابرو مشکی یکدست با جلای بسیار بالا.|
shanxi_black|شانشی بلک|Shanxi Black|مشکی چینی|granite|bk|uni|شانشی|چین|||گرانیت مشکی ریزدانه و یکنواخت.|
g603|گرانیت G603|G603 Bianco Crystal|G603, Padang light|granite|gy|grain|فوجیان|چین|||گرانیت خاکستری روشن ارزان و پرمصرف برای کف‌پوش محوطه.|
g654|گرانیت G654|G654 Padang Dark|G654|granite|gy|grain|فوجیان|چین|||گرانیت خاکستری تیره برای کف‌پوش، پله و جدول.|
taj_mahal|کوارتزیت تاج‌محل|Taj Mahal Quartzite|تاج محل|quartzite|cr|vein|میناس ژرایس|برزیل|||کوارتزیت کرم روشن با رگه‌های طلایی ملایم؛ ظاهر مرمر با مقاومت گرانیت.|
mont_blanc|کوارتزیت مون‌بلان|Mont Blanc Quartzite|مونت بلانک|quartzite|wh|vein|میناس ژرایس|برزیل|||کوارتزیت سفید و خاکستری با رگه‌های موازی.|
azul_macaubas|آزول ماکائوباس|Azul Macaubas|کوارتزیت آبی|quartzite|bl|band|باهیا|برزیل|||کوارتزیت آبی آسمانی بسیار کمیاب.|
fusion_quartzite|کوارتزیت فیوژن|Fusion Quartzite|Fusion Wow|quartzite|bl|band|برزیل|برزیل|||کوارتزیت چندرنگ با ترکیب آبی، سبز و نارنجی.|
portland_stone|سنگ پورتلند|Portland Stone|Portland limestone|limestone|wh|uni|جزیرهٔ پورتلند، دورست|انگلستان|||سنگ آهک سفید تا کرم؛ کلیسای سنت پاول لندن و بسیاری از بناهای لندن با آن ساخته شده‌اند.|Portland stone
bath_stone|سنگ بث|Bath Stone|Bath limestone|limestone|cr|uni|بث، سامرست|انگلستان|||سنگ آهک اُاُلیتی عسلی‌رنگ که شهر تاریخی بث با آن ساخته شده است.|Bath stone
jerusalem_stone|سنگ اورشلیم|Jerusalem Stone|Jerusalem gold|limestone|cr|uni|اورشلیم و کرانهٔ باختری|فلسطین|||سنگ آهک و دولومیت کرم طلایی که از دوران باستان در این منطقه به کار رفته است.|Jerusalem stone
indiana_limestone|سنگ آهک ایندیانا|Indiana Limestone|Bedford stone|limestone|cr|uni|بدفورد، ایندیانا|آمریکا|||سنگ آهک کرم که ساختمان امپایر استیت و پنتاگون با آن نماسازی شده‌اند.|Indiana Limestone
caen_stone|سنگ کان|Caen Stone|Pierre de Caen|limestone|cr|uni|کان، نرماندی|فرانسه|||سنگ آهک کرم که در ساخت کلیساها و بخش‌هایی از برج لندن به کار رفته است.|Caen stone
moleanos|مولیانوس|Moleanos|Moca Creme|limestone|cr|band|آلکوباسا|پرتغال|||سنگ آهک بژ با رگه‌های ریز موازی؛ برای نما و کف رایج است.|
coralina|سنگ مرجانی|Coralina|Coral stone|limestone|cr|pore|سواحل جنوبی|جمهوری دومینیکن|||سنگ آهک مرجانی با فسیل‌های مرجان و صدف؛ برای فضاهای ساحلی و استخر.|Coral stone
rainbow_sandstone|ماسه‌سنگ رنگین‌کمانی|Rainbow Sandstone|Rainbow|sandstone|cr|band|راجستان|هند|||ماسه‌سنگ با نوارهای کرم، صورتی و قهوه‌ای.|
dholpur|ماسه‌سنگ دولپور|Dholpur Sandstone|Dholpur beige, Dholpur red|sandstone|pk|uni|دولپور، راجستان|هند|||ماسه‌سنگ صورتی تا قرمز؛ در بناهای دهلی نو مانند کاخ ریاست جمهوری به کار رفته است.|
hawkesbury|ماسه‌سنگ سیدنی|Sydney Sandstone|Hawkesbury sandstone|sandstone|ye|band|سیدنی، نیو ساوت ولز|استرالیا|||ماسه‌سنگ زرد طلایی با لایه‌های آهن‌دار؛ هویت معماری قدیمی سیدنی.|Hawkesbury sandstone
brownstone|براون‌استون|Brownstone|Portland brownstone|sandstone|bn|uni|پورتلند، کنتیکت|آمریکا|||ماسه‌سنگ قهوه‌ای تیره که خانه‌های مشهور نیویورک با آن ساخته شده‌اند.|Brownstone
yorkstone|سنگ یورک|Yorkstone|York stone|sandstone|bn|band|یورکشایر|انگلستان|||ماسه‌سنگ خاکستری تا قهوه‌ای برای کف‌پوش پیاده‌روها.|Yorkstone
welsh_slate|اسلیت ولز|Welsh Slate|Penrhyn slate|slate|bl|uni|گوینت|بریتانیا (ولز)|||اسلیت خاکستری مایل به آبی که میراث جهانی یونسکو است و بام‌های بسیاری از شهرهای جهان را پوشانده است.|Welsh slate
spanish_slate|اسلیت اسپانیا|Spanish Slate|Valdeorras slate|slate|bk|uni|والدئوراس، گالیسیا|اسپانیا|||اسلیت مشکی بزرگ‌ترین تولیدکنندهٔ جهان برای پوشش بام.|
brazilian_slate|اسلیت برزیل|Brazilian Slate|Minas Gerais slate|slate|gy|uni|میناس ژرایس|برزیل|||اسلیت خاکستری تا سبز برای کف و دیوار.|
vermont_slate|اسلیت ورمونت|Vermont Slate|Slate Valley|slate|pu|uni|درهٔ اسلیت، ورمونت|آمریکا|||اسلیت در رنگ‌های بنفش، سبز و قرمز.|
basaltina|بازالتینا|Basaltina|Basaltina Roma|basalt|gy|pore|باگنوریجو، لاتزیو|ایتالیا|||بازالت خاکستری با حفره‌های ریز؛ برای کف‌پوش و نما.|
etna_lava|سنگ گدازهٔ اتنا|Etna Lava Stone|Pietra lavica dell'Etna|basalt|bk|pore|کاتانیا، سیسیل|ایتالیا|||سنگ آتشفشانی تیره که خیابان‌های کاتانیا با آن فرش شده‌اند.|
g684|بازالت G684|G684 Black Basalt|Fuding black|basalt|bk|uni|فوجیان|چین|||بازالت مشکی ارزان برای کف‌پوش محوطه و جدول.|
verde_guatemala|وردی گواتمالا|Verde Guatemala|Indian green marble|serpentinite|gn|vein|اودایپور، راجستان|هند|||سنگ سبز تیره با رگه‌های سفید؛ با وجود نام، معدن آن در هند است.|
verde_alpi|وردی آلپی|Verde Alpi|Verde Aver|serpentinite|gn|vein|دره آئوستا|ایتالیا|||سرپانتینیت سبز تیره با رگه‌های سفید و سبز روشن.|
verde_antico|وردی آنتیکو|Verde Antico|Verde antique, Thessalian green|serpentinite|gn|vein|تسالی|یونان|||برش سرپانتینی سبز که در دوران روم و بیزانس ارزشمند بود.|Verde antique
rosso_levanto|رسو لوانتو|Rosso Levanto|Levanto red|serpentinite|rd|vein|لوانتو، لیگوریا|ایتالیا|||برش سرپانتینی قرمز شرابی با رگه‌های سفید و سبز.|
bianco_lasa|بیانکو لازا|Bianco Lasa|Lasa white, Lasa marble|marble|wh|uni|لازا، تیرول جنوبی|ایتالیا|||مرمر سفید بلورین و مقاوم در برابر هوازدگی از کوه‌های آلپ.|Lasa marble
calacatta_viola|کالاکاتا ویولا|Calacatta Viola|Viola marble|marble|wh|vein|کارارا، توسکانی|ایتالیا|||مرمر سفید با رگه‌های درشت بنفش و شرابی؛ از سنگ‌های پرطرفدار طراحی داخلی.|
perlato_sicilia|پرلاتو سیسیل|Perlato di Sicilia|Perlato Sicilia|marmarite|cr|uni|تراپانی، سیسیل|ایتالیا|||سنگ کرم روشن با فسیل‌های بسیار ریز و زمینهٔ یکدست.|
grigio_carnico|گریجو کارنیکو|Grigio Carnico|Carnic grey|marble|gy|vein|فریولی|ایتالیا|||سنگ خاکستری تیره با رگه‌های سفید درهم.|
rosa_norvegia|رزا نروژ|Rosa Norvegia|Norwegian Rose|marble|pk|vein|فاوسکه|نروژ|||مرمر صورتی با رگه‌های سبز و خاکستری.|
rosso_francia|قرمز فرانسه|Rosso Francia|Rouge Languedoc, Rouge de France|marmarite|rd|cloud|لانگدوک|فرانسه|||سنگ قرمز با لکه‌های سفید و خاکستری؛ در کاخ ورسای به کار رفته است.|
grand_antique|گرند آنتیک|Grand Antique|Grand Antique d'Aubert|marmarite|bk|vein|اوبر، آریژ|فرانسه|||برش مشکی و سفید با تکه‌های زاویه‌دار؛ از سنگ‌های تاریخی اروپا.|
light_emperador|امپرادور روشن|Light Emperador|Emperador Light|marmarite|bn|vein|لا ریوخا|اسپانیا|||نسخهٔ روشن‌تر امپرادور با زمینهٔ قهوه‌ای عسلی و رگه‌های سفید.|
panda_white|پاندا وایت|Panda White|Panda marble|marble|wh|vein|استان فوجیان|چین|||مرمر سفید با رگه‌های پهن و پررنگ مشکی؛ ظاهری بسیار گرافیکی دارد.|
guangxi_white|سفید گوانگشی|Guangxi White|China Carrara|marble|wh|vein|گوانگشی|چین|||مرمر سفید با رگه‌های خاکستری؛ جایگزین ارزان‌تر کارارا.|
ming_green|مینگ گرین|Ming Green|Verde Ming, Hunan green|marble|gn|cloud|هونان|چین|||مرمر سبز روشن با ابرهای سفید و سبز تیره.|
ruivina|رویوینا|Ruivina|Ruivina marble|marble|gy|band|استرموز، آلنتژو|پرتغال|||مرمر خاکستری با نوارهای تیره‌تر.|
black_pearl|بلک پرل|Black Pearl|Black Pearl granite|granite|bk|grain|آندرا پرادش|هند|||گرانیت مشکی با دانه‌های ریز نقره‌ای.|
steel_grey|استیل گری|Steel Grey|Steel grey granite|granite|gy|grain|آندرا پرادش|هند|||گرانیت خاکستری تیره و یکنواخت؛ پرکاربرد برای کف و کابینت.|
paradiso|پارادیزو|Paradiso|Paradiso Classic|granite|pu|band|تامیل نادو|هند|||گرانیت گنیسی با نوارهای بنفش، خاکستری و صورتی.|
red_multicolor|قرمز مولتی‌کالر|Red Multicolor|Multicolor red|granite|rd|band|اوریسا|هند|||گرانیت قرمز با موج‌ها و نوارهای مشکی و خاکستری.|
santa_cecilia|سانتا سسیلیا|Santa Cecilia|Santa Cecilia Gold|granite|ye|grain|اسپیریتو سانتو|برزیل|||گرانیت زرد طلایی با دانه‌های قهوه‌ای و خال‌های قرمز گارنت.|
blue_bahia|بلو باهیا|Azul Bahia|Blue Bahia|granite|bl|grain|باهیا|برزیل|||سنگ آذرین آبی آسمانی با رگه‌های سفید؛ کمیاب و گران‌قیمت.|
labrador_antique|لابرادور آنتیک|Labrador Antique|Antique Brown|granite|bk|grain|اسپیریتو سانتو|برزیل|||گرانیت تیره با بلورهای قهوه‌ای و طلایی درشت.|
rosa_beta|رزا بتا|Rosa Beta|Rosa Beta granite|granite|pk|grain|ساردینیا|ایتالیا|||گرانیت صورتی روشن با دانه‌های خاکستری و مشکی.|
balmoral_red|رسو بالمورال|Balmoral Red|Rosso Balmoral|granite|rd|grain|تاملا|فنلاند|||گرانیت قرمز تیره و ریزدانه؛ برای نما و سنگ یادبود.|
g664|گرانیت G664|G664 Luna Pearl|G664, Bainbrook brown|granite|pk|grain|فوجیان|چین|||گرانیت صورتی مایل به قهوه‌ای ارزان و پرمصرف.|
g682|گرانیت G682|G682 Rusty Yellow|G682, Rustic yellow|granite|ye|grain|فوجیان|چین|||گرانیت زرد زنگاری برای کف‌پوش محوطه و نما.|
jura_beige|ژورا بژ|Jura Beige|Jura Marble, Jura limestone|limestone|cr|cloud|باواریا|آلمان|||سنگ آهک بژ با فسیل‌های آمونیت و بلمنیت؛ برای کف و نما.|
vratza|ورتسا|Vratza Limestone|Vratza|limestone|cr|uni|ورتسا|بلغارستان|||سنگ آهک کرم روشن و یکنواخت؛ برای نما و کف.|
crema_europa|کرم اروپا|Crema Europa|Crema Europa limestone|limestone|cr|band|کاستیا|اسپانیا|||سنگ آهک کرم با رگه‌های ریز موازی.|
belgian_bluestone|سنگ آبی بلژیک|Belgian Bluestone|Petit Granit, Pierre bleue|limestone|gy|uni|منطقهٔ والونی|بلژیک|||سنگ آهک خاکستری آبی‌فام با فسیل‌های ریز؛ با وجود نام «پتی گرانیت»، سنگ آهک است.|
chinese_bluestone|سنگ آبی چین|Chinese Bluestone|Blue limestone|limestone|gy|uni|فوجیان|چین|||سنگ آهک خاکستری تیره برای کف‌پوش محوطه و استخر.|
kandla_grey|کاندلا گری|Kandla Grey|Kandla grey sandstone|sandstone|gy|uni|راجستان|هند|||ماسه‌سنگ خاکستری یکنواخت برای کف‌پوش محوطه و پیاده‌رو.|
raj_green|راج گرین|Raj Green|Raja green|sandstone|gn|band|راجستان|هند|||ماسه‌سنگ سبز با لایه‌های قهوه‌ای و کرم.|
teakwood|ماسه‌سنگ تیک‌وود|Teakwood Sandstone|Teak sandstone|sandstone|ye|band|راجستان|هند|||ماسه‌سنگ با نوارهای زرد و قهوه‌ای شبیه بافت چوب.|
modak|ماسه‌سنگ موداک|Modak Sandstone|Modak|sandstone|pk|band|راجستان|هند|||ماسه‌سنگ صورتی تا قرمز با نوارهای زرد.|
autumn_brown|اوتوم براون|Autumn Brown|Autumn brown sandstone|sandstone|bn|band|راجستان|هند|||ماسه‌سنگ قهوه‌ای با نوارهای پاییزی.|
navona|تراورتن ناوونا|Travertino Navona|Navona|travertine|cr|pore|تیوولی، لاتزیو|ایتالیا|||تراورتن کرم با حفره‌های ریز؛ از معادن تاریخی نزدیک رم.|
persian_walnut|تراورتن گردویی ایران|Persian Walnut Travertine|Iran walnut travertine|travertine|bn|band|ایران|ایران|||تراورتن قهوه‌ای گردویی با نوارهای رنگی؛ از تراورتن‌های صادراتی ایران.|
peru_travertine|تراورتن پرو|Peruvian Travertine|Peru travertine|travertine|cr|pore|خونین|پرو|||تراورتن کرم تا طلایی از رشته‌کوه آند.|
white_macaubas|ماکائوباس سفید|White Macaubas|Macaubas white|quartzite|wh|band|باهیا|برزیل|||کوارتزیت سفید با نوارهای ظریف خاکستری؛ بسیار سخت و کم‌جذب.|
patagonia|پاتاگونیا|Patagonia|Patagonia quartzite|quartzite|cr|cloud|برزیل|برزیل|||کوارتزیت چندرنگ با تکه‌های کرم، قهوه‌ای و شفاف؛ مناسب بک‌لایت.|
cristallo|کریستالو|Cristallo|Cristallo quartzite|quartzite|wh|cloud|برزیل|برزیل|||کوارتزیت سفید نیمه‌شفاف با بلورهای درشت؛ برای بک‌لایت و فضاهای لوکس.|
sea_pearl|سی پرل|Sea Pearl|Sea Pearl quartzite|quartzite|gy|vein|برزیل|برزیل|||کوارتزیت خاکستری با رگه‌های سفید و نقره‌ای.|
perla_venata|پرلا ونتا|Perla Venata|Perla Venata quartzite|quartzite|wh|vein|برزیل|برزیل|||کوارتزیت سفید با رگه‌های خاکستری شبیه مرمر.|
persian_red_onyx|اونیکس قرمز ایران|Persian Red Onyx|Red onyx|onyx|rd|band|ایران|ایران|||مرمر سنگ قرمز و نارنجی با نوارهای موجی؛ برای دیوار و میز نورپردازی‌شده.|
"""


def parse_range(r):
    return {"min": r[0], "max": r[1]}


# Lab values a producer published for one specific stone; shown instead of the
# type's typical ranges. Units: density kg/m3, absorption %, strengths MPa,
# abrasion mm (EN 14157 wide wheel), porosity %.
STONE_LAB = {
    "kermanshah_limestone": {
        "density": (2500, 2650), "absorption": (0.5, 3.0), "compressive": (60, 120),
        "flexural": (7, 12), "abrasion": (20, 24), "porosity": (1, 6),
        "standard": "EN 1936, EN 13755, EN 1926, EN 12372, EN 14157",
        "source": "NexStone (nexstone.ir)",
        "sourceUrl": "https://nexstone.ir/stones/limestone/",
        "imageUrl": "https://nexstone.ir/wp-content/themes/nexstone/assets/img/photos/limestone-polished-slab-1.jpg",
    },
}


def table(text, cols):
    rows = {}
    for line in text.strip().splitlines():
        parts = [c.strip() for c in line.split("|")]
        assert len(parts) == cols, (len(parts), line)
        assert parts[0] not in rows, parts[0]
        rows[parts[0]] = parts
    return rows


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    countries = table(T.COUNTRIES, 4)
    regions = table(T.REGIONS, 4)
    cats = table(T.CATEGORIES, 6)
    type_tr = table(T.TYPES, 6)
    stone_tr = table(T.STONES, 6)

    type_to_cat = {}
    categories = []
    for i, (cid, c) in enumerate(cats.items()):
        categories.append({"id": cid, "nameFa": c[1], "nameEn": c[2], "nameAr": c[3], "nameRu": c[4], "sortOrder": i})
        for t in c[5].split(","):
            type_to_cat[t.strip()] = cid

    types = []
    type_ids = set()
    for i, t in enumerate(TYPES):
        (tid, fa, en, desc, dens, absn, comp, flex, mohs, acid, std, fin, uses, wiki) = t
        type_ids.add(tid)
        tr = type_tr[tid]
        types.append({
            "id": tid, "categoryId": type_to_cat[tid],
            "nameFa": fa, "nameEn": en, "nameAr": tr[1], "nameRu": tr[2],
            "description": desc, "descEn": tr[3], "descAr": tr[4], "descRu": tr[5],
            "densityMin": dens[0], "densityMax": dens[1],
            "absorptionMin": absn[0], "absorptionMax": absn[1],
            "compressiveMin": comp[0], "compressiveMax": comp[1],
            "flexuralMin": flex[0], "flexuralMax": flex[1],
            "mohsMin": mohs[0], "mohsMax": mohs[1],
            "acid": acid, "standard": std, "finishes": fin, "uses": uses,
            "wikiTitle": wiki, "sortOrder": i,
        })
    type_defaults = {t["id"]: t for t in types}

    colors = {"wh", "cr", "ye", "bn", "rd", "pk", "gn", "bl", "gy", "bk", "pu"}
    patterns = {"vein", "cloud", "uni", "grain", "pore", "band"}
    stones, seen = [], set()
    for line in STONES.strip().splitlines():
        cols = line.split("|")
        assert len(cols) == 13, (len(cols), line)
        (sid, fa, en, aliases, tid, color, pattern, region, country,
         fin, uses, desc, wiki) = [c.strip() for c in cols]
        assert sid not in seen, sid
        assert tid in type_ids, line
        assert color in colors, line
        assert pattern in patterns, line
        assert sid in stone_tr, f"missing translation for stone {sid}"
        assert region in regions, f"missing translation for region {region}"
        assert country in countries, f"missing translation for country {country}"
        seen.add(sid)
        tr, rg, co = stone_tr[sid], regions[region], countries[country]
        stones.append({
            "id": sid, "nameFa": fa, "nameEn": en, "nameAr": tr[1], "nameRu": tr[2],
            "aliases": aliases,
            "typeId": tid, "color": color, "pattern": pattern,
            "region": region, "regionEn": rg[1], "regionAr": rg[2], "regionRu": rg[3],
            "country": country, "countryEn": co[1], "countryAr": co[2], "countryRu": co[3],
            "finishes": fin or type_defaults[tid]["finishes"],
            "uses": uses or type_defaults[tid]["uses"],
            "description": desc, "descEn": tr[3], "descAr": tr[4], "descRu": tr[5],
            "wikiTitle": wiki or None,
            "lab": STONE_LAB.get(sid),
        })
    assert set(STONE_LAB) <= seen, set(STONE_LAB) - seen
    extra = set(stone_tr) - seen
    assert not extra, f"translations for unknown stones: {extra}"

    out = root / "app/src/main/assets/seed.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"version": SEED_VERSION, "categories": categories, "types": types, "stones": stones},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out} ({len(categories)} categories, {len(types)} types, {len(stones)} stones)")


if __name__ == "__main__":
    main()

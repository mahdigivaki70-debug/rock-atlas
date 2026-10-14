# -*- coding: utf-8 -*-
"""Shorter trade-name entries (seed v6): name, group, colour, pattern and origin.

These come from general knowledge of the dimension-stone trade, not from any one
catalogue. They have no description of their own: the app shows the type's
description and lab ranges. Names in Arabic and Russian fall back to the trade
name, which is how these stones are sold in every market.

Line format:
    type | colour | pattern | country (fa) | region (fa, optional) | Name; Name; Name=Persian name
Names that already exist in the main tables are skipped.
"""

# New countries used here: fa | en | ar | ru
COUNTRIES = """
ایرلند|Ireland|أيرلندا|Ирландия
کانادا|Canada|كندا|Канада
اتریش|Austria|النمسا|Австрия
اسلوونی|Slovenia|سلوفينيا|Словения
لهستان|Poland|بولندا|Польша
جمهوری چک|Czech Republic|التشيك|Чехия
روسیه|Russia|روسيا|Россия
بولیوی|Bolivia|بوليفيا|Боливия
ویتنام|Vietnam|فيتنام|Вьетнам
اندونزی|Indonesia|إندونيسيا|Индонезия
آنگولا|Angola|أنغولا|Ангола
کرواسی|Croatia|كرواتيا|Хорватия
"""

TRADE = """
granite|bk|uni|هند||Jet Black; Rajasthan Black
granite|bk|vein|هند||Black Forest; Black Markino
granite|rd|grain|هند||Imperial Red; New Imperial Red; Ruby Red; Lakha Red; Jhansi Red; Sindoori Red
granite|pk|grain|هند||Chima Pink; Rosy Pink
granite|bn|grain|هند||Desert Brown; Coffee Brown; Sapphire Brown; Ivory Brown; Cat's Eye
granite|bn|band|هند||English Teak
granite|wh|grain|هند||Colonial White; Bianco Romano; Moon White; Galaxy White
granite|wh|band|هند||River White; Thunder White
granite|ye|grain|هند||Colonial Gold; Crystal Yellow
granite|ye|band|هند||Tiger Skin
granite|cr|grain|هند||Raw Silk
granite|cr|band|هند||Ivory Fantasy; Juparana Colombo
granite|gn|grain|هند||Kuppam Green; Seaweed Green; Hassan Green
granite|gy|grain|هند||Sira Grey
granite|bl|grain|هند||Lavender Blue
granite|pu|band|هند||Paradiso Bash
marble|wh|vein|هند||Ambaji White; Banswara White
marble|wh|uni|هند||Morwad White
marble|pk|vein|هند||Udaipur Pink
marmarite|cr|cloud|هند||Katni Beige
limestone|ye|uni|هند||Jaisalmer Yellow; Tandur Yellow
limestone|gn|uni|هند||Kota Stone
limestone|bn|uni|هند||Kota Brown
limestone|gy|uni|هند||Tandur Blue; Shahabad Stone
sandstone|ye|uni|هند||Lalitpur Yellow
sandstone|gy|uni|هند||Lalitpur Grey
sandstone|rd|uni|هند||Agra Red
sandstone|cr|band|هند||Mint Sandstone; Fossil Mint
sandstone|pk|uni|هند||Jodhpur Pink; Bansi Pink
sandstone|bk|uni|هند||Sagar Black
sandstone|cr|uni|هند||Camel Dust
slate|bk|uni|هند||Jak Black
slate|ye|band|هند||Kund Multicolour; California Gold
slate|gy|band|هند||Peacock Slate
granite|ye|grain|برزیل||Giallo Fiorito; New Venetian Gold; Ocre Itabira; Amarelo Ouro Brasil
granite|ye|band|برزیل||Golden Persa; Lapidus
granite|gn|grain|برزیل||Verde Butterfly; Costa Esmeralda
granite|rd|band|برزیل||Typhoon Bordeaux
granite|rd|grain|برزیل||Vermelho Brasília; Vermelho Capão Bonito
granite|pk|grain|برزیل||Rosa Iracema
granite|wh|band|برزیل||Delicatus; White Ice; Alaska White; Bianco Antico
granite|wh|grain|برزیل||Branco Dallas; Branco Siena; Branco Itaúnas
granite|gy|grain|برزیل||Cinza Andorinha; Cinza Corumbá
granite|bk|band|برزیل||Cosmic Black
granite|bk|uni|برزیل||Preto São Gabriel
quartzite|wh|vein|برزیل||Bianco Superiore; Cielo White; Matarazzo
quartzite|bl|vein|برزیل||Blue Roma
quartzite|gn|vein|برزیل||Alexandrita
quartzite|pk|band|برزیل||Dolce Vita
quartzite|gy|band|برزیل||Gaya
quartzite|bk|vein|برزیل||Belvedere
dolomitic|wh|vein|برزیل||Super White
marble|wh|vein|ایتالیا|کارارا، توسکانی|Calacatta Borghini; Calacatta Vagli; Calacatta Macchia Vecchia; Statuarietto; Bianco Venato; Bianco Gioia; Arabescato Corchia; Arabescato Vagli; Arabescato Cervaiole; Venatino; Pavonazzetto
marble|gy|cloud|ایتالیا|کارارا، توسکانی|Bardiglio Nuvolato
marble|gy|band|ایتالیا|کارارا، توسکانی|Zebrino
marble|gn|band|ایتالیا|کارارا، توسکانی|Cipollino Apuano; Cipollino Ondulato
marble|wh|vein|ایتالیا|لازا، تیرول جنوبی|Bianco Covelano
marble|pk|vein|ایتالیا|پیه‌مونته|Candoglia
marmarite|pu|cloud|ایتالیا|کارارا، توسکانی|Breccia Medicea
marmarite|pk|cloud|ایتالیا|کارارا، توسکانی|Breccia Capraia
marmarite|pk|cloud|ایتالیا|برشا، لمباردی|Breccia Aurora
marmarite|ye|cloud|ایتالیا|برشا، لمباردی|Breccia Oniciata
marmarite|pk|cloud|ایتالیا|ورونا، ونتو|Nembro Rosato
marmarite|ye|cloud|ایتالیا|ورونا، ونتو|Giallo Reale
marmarite|rd|cloud|ایتالیا|ورونا، ونتو|Rosso Magnaboschi
marmarite|cr|cloud|ایتالیا|تراپانی، سیسیل|Perlato Royal
limestone|gy|cloud|ایتالیا||Grigio Billiemi
limestone|cr|band|ایتالیا|ورونا، ونتو|Pietra di Prun
limestone|cr|uni|ایتالیا|ترانی، پولیا|Perlato Svevo
limestone|cr|pore|ایتالیا||Pietra di Matera
limestone|gy|cloud|ایتالیا||Ceppo di Gré
serpentinite|gn|vein|ایتالیا|دره آئوستا|Verde Issorie
granite|gy|band|ایتالیا|پیه‌مونته|Pietra di Luserna; Beola
granite|gy|grain|ایتالیا||Ghiandone
granite|wh|grain|ایتالیا||San Fedelino
sandstone|bn|uni|ایتالیا|فلورانس، توسکانی|Pietra Forte
basalt|gy|grain|ایتالیا||Peperino
travertine|cr|pore|ایتالیا|سیه‌نا، توسکانی|Travertino Toscano
slate|bk|uni|ایتالیا||Pietra del Cardoso
marmarite|cr|vein|اسپانیا||Crema Valencia
marmarite|pk|cloud|اسپانیا||Rosa Zarci; Rosa Valencia
marmarite|gy|vein|اسپانیا||Gris Pulpis
marmarite|rd|cloud|اسپانیا||Rojo Coralito
marble|wh|vein|اسپانیا|ماکائل، آلمریا|Blanco Tranco
limestone|cr|uni|اسپانیا||Caliza Capri; Piedra de Colmenar; Piedra Campaspero
sandstone|ye|uni|اسپانیا||Arenisca de Villamayor
granite|wh|grain|اسپانیا||Blanco Castilla; Blanco Perla
granite|gy|grain|اسپانیا||Gris Quintana; Gris Alba
granite|pk|grain|اسپانیا|پونته‌ودرا، گالیسیا|Rosa Mondariz
limestone|cr|uni|پرتغال||Vidraço de Ataíja; Semi Rijo
limestone|gy|uni|پرتغال||Ataíja Azul
limestone|cr|vein|پرتغال||Lioz
limestone|ye|uni|پرتغال||Amarelo Negrais
granite|gy|grain|پرتغال||Cinzento Alpalhão
marble|rd|uni|یونان|لاکونیا، پلوپونز|Rosso Antico
marble|wh|uni|ترکیه|آفیون‌قره‌حصار|Afyon Sugar
marble|wh|vein|ترکیه|آفیون‌قره‌حصار|Afyon Violet
marble|gy|vein|ترکیه|آفیون‌قره‌حصار|Afyon Grey
marble|pk|vein|ترکیه||Rosalia
marble|gn|vein|ترکیه||Usak Green
marmarite|bk|vein|ترکیه||Toros Black
marmarite|gy|vein|ترکیه||Tundra Grey
marmarite|cr|cloud|ترکیه||Bilecik Beige
limestone|cr|uni|ترکیه||Toros Beige; Ottoman Beige
limestone|cr|pore|ترکیه||Küfeki
travertine|cr|pore|ترکیه|دنیزلی|Ivory Travertine
travertine|ye|band|ترکیه|دنیزلی|Scabos
travertine|rd|band|ترکیه||Altıntaş Red Travertine
basalt|gy|grain|ترکیه||Ankara Andesite
marble|bk|vein|ایران|استان اصفهان|Persian Black Marquina=مرمر مشکی مارکینای ایران
marble|bn|vein|ایران||Persian Emperador=امپرادور ایرانی
travertine|cr|pore|ایران||Darreh Bokhari Travertine=تراورتن دره‌بخاری
granite|bk|grain|ایران||Tuyserkan Granite=گرانیت تویسرکان
granite|gy|grain|چین|فوجیان|G602; G623; G633; G614; G341
granite|pk|grain|چین|فوجیان|G635; G636; G663; G681
granite|wh|grain|چین||G439 Big Flower White; G355 Crystal White; G655
granite|ye|grain|چین||G350 Shandong Yellow; G696
granite|rd|grain|چین||G562 Maple Red; Tianshan Red
granite|bk|uni|چین||Mongolia Black
marble|wh|vein|چین||Oriental White
marble|gy|vein|چین||Silver Dragon
marble|gy|band|چین||Wooden Grey
serpentinite|gn|vein|چین||Dandong Green
slate|ye|band|چین||Rusty Slate
basalt|bk|pore|چین||Hainan Black Basalt
granite|gn|grain|فنلاند||Baltic Green
granite|rd|grain|فنلاند||Karelia Red; Carmen Red
granite|bk|grain|فنلاند|یلاروی|Spectrolite
granite|bl|grain|نروژ|لارویک|Marina Pearl
serpentinite|gn|band|سوئد||Kolmården Marble
limestone|rd|uni|سوئد||Öland Limestone
sandstone|gy|uni|سوئد||Gotland Sandstone
limestone|gy|cloud|آلمان|باواریا|Jura Grey
limestone|cr|cloud|آلمان|باواریا|Treuchtlinger Marmor
limestone|cr|pore|آلمان|باواریا|Kirchheimer Muschelkalk; Krensheimer Muschelkalk
limestone|gn|uni|آلمان||Anröchter Dolomit
sandstone|rd|uni|آلمان||Main Sandstone
sandstone|cr|uni|آلمان||Obernkirchener Sandstein; Elbsandstein
sandstone|gy|uni|آلمان||Ruhr Sandstone
granite|gy|grain|آلمان|باواریا|Kösseine Granite; Flossenbürger Granite
basalt|gy|pore|آلمان||Mayen Basalt Lava
basalt|ye|pore|آلمان||Weiberner Tuff
slate|bk|uni|آلمان||Moselschiefer
limestone|cr|uni|فرانسه||Pierre de Lens; Pierre de Chauvigny
limestone|cr|pore|فرانسه||Saint-Maximin
limestone|cr|uni|فرانسه|بورگونی|Anstrude
limestone|cr|cloud|فرانسه|بورگونی|Buxy
limestone|wh|pore|فرانسه||Tuffeau
limestone|ye|pore|فرانسه|لورن (موز)|Pierre de Jaumont
granite|pk|grain|فرانسه|بریتانی|Rose de la Clarté
granite|gy|grain|فرانسه|بریتانی|Granit de Louvigné
slate|bk|uni|فرانسه||Ardoise d'Angers
basalt|gy|pore|فرانسه||Pierre de Volvic
marble|gn|band|فرانسه||Campan Vert
marmarite|rd|cloud|فرانسه||Sarrancolin
marble|wh|uni|فرانسه||Saint-Béat
marmarite|rd|cloud|بلژیک|منطقهٔ والونی|Rouge Royal
marmarite|bk|vein|بلژیک|منطقهٔ والونی|Bleu Belge
marmarite|gy|cloud|بلژیک|منطقهٔ والونی|Sainte-Anne
limestone|gy|cloud|انگلستان||Purbeck Marble
limestone|cr|uni|انگلستان||Ancaster Stone; Clipsham Stone; Hopton Wood; Doulting Stone
limestone|cr|pore|انگلستان||Ketton Stone
limestone|bn|uni|انگلستان||Hornton Stone
limestone|ye|uni|انگلستان||Ham Hill Stone
sandstone|gy|uni|انگلستان||Forest of Dean Stone
granite|pk|grain|انگلستان|کامبریا|Shap Pink
granite|gy|grain|انگلستان||De Lank Granite
slate|gy|uni|انگلستان||Delabole Slate
granite|gy|grain|اسکاتلند||Kemnay Granite; Rubislaw Granite
sandstone|gy|uni|اسکاتلند||Caithness Flagstone
serpentinite|gn|vein|ایرلند||Connemara Marble
limestone|bk|uni|ایرلند||Kilkenny Blue Limestone
sandstone|gy|uni|ایرلند||Liscannor Stone
granite|gy|grain|آمریکا||Barre Gray; Rockport Granite; Woodbury Gray
granite|bk|uni|آمریکا||Mesabi Black; Academy Black
granite|pk|grain|آمریکا||Stony Creek Granite
granite|wh|grain|آمریکا||Sierra White
granite|rd|grain|آمریکا|داکوتای جنوبی|Carnelian Granite
marble|wh|vein|آمریکا||Georgia Marble; Danby Marble
marble|wh|uni|آمریکا||Colorado Yule Marble
marmarite|pk|cloud|آمریکا||Tennessee Marble
limestone|ye|uni|آمریکا||Kasota Stone
limestone|cr|uni|آمریکا|تگزاس|Cordova Cream
limestone|cr|pore|آمریکا||Texas Shellstone; Florida Keystone
sandstone|cr|band|آمریکا||Crab Orchard Stone
sandstone|bl|uni|آمریکا||Pennsylvania Bluestone
sandstone|rd|uni|آمریکا||Arizona Flagstone
slate|bk|uni|آمریکا||Buckingham Slate
granite|gy|grain|کانادا||Stanstead Gray
granite|bk|uni|کانادا||Cambrian Black
limestone|cr|cloud|کانادا||Tyndall Stone
limestone|gy|uni|کانادا||Eramosa Limestone
sandstone|cr|uni|کانادا||Wallace Sandstone
marble|cr|uni|مکزیک||Santo Tomás Marble
marmarite|bk|vein|مکزیک||Negro Monterrey
basalt|pk|pore|مکزیک||Cantera Rosa
basalt|bk|pore|مکزیک||Recinto
granite|rd|grain|آفریقای جنوبی||African Red
granite|bk|uni|آفریقای جنوبی||Belfast Black
granite|bk|uni|آنگولا||Angola Black
marmarite|cr|uni|مصر||Triesta
marmarite|ye|uni|مصر||Khatmia
granite|rd|grain|مصر||Red Aswan
granite|bk|uni|مصر||Black Aswan
granite|pk|grain|مصر||Rosa El Nasr
granite|gy|grain|مصر||Halayeb Granite; Gandola Granite
marble|wh|vein|پاکستان|بلوچستان|Ziarat White
marble|bk|vein|پاکستان||Black Gold
limestone|cr|uni|کرواسی||Pietra d'Istria; Brač Stone
marmarite|cr|cloud|اتریش||Untersberger Marble
marmarite|rd|cloud|اتریش||Adneter Marble
marble|wh|vein|اتریش||Krastaler Marble; Sölker Marble
limestone|cr|uni|اسلوونی||Lipica Stone
granite|gy|grain|لهستان||Strzegom Granite
sandstone|ye|uni|لهستان||Szydłowiec Sandstone
sandstone|cr|uni|جمهوری چک||Hořice Sandstone
marble|wh|uni|روسیه||Koelga Marble
marble|wh|band|روسیه||Ufaley Marble
granite|rd|grain|روسیه||Kashina Gora
granite|gy|grain|روسیه||Mansurovsky Granite
quartzite|rd|uni|روسیه||Shoksha Quartzite
granite|rd|grain|اوکراین||Kapustino Granite
granite|bk|grain|اوکراین|ژیتومیر|Golovinsky Labradorite
granite|gy|grain|اوکراین||Pokostovka Granite
semiprecious|bl|cloud|بولیوی||Azul Boliviano Sodalite
marble|wh|uni|ویتنام||Yen Bai White
basalt|gy|pore|ویتنام||Vietnam Bluestone
sandstone|cr|uni|اندونزی||Palimanan Sandstone
basalt|gy|uni|اندونزی||Indonesian Andesite
limestone|cr|pore|استرالیا||Mount Gambier Limestone
granite|gy|grain|استرالیا||Harcourt Granite
basalt|gy|uni|استرالیا||Victorian Bluestone
sandstone|cr|uni|استرالیا||Helidon Sandstone
"""

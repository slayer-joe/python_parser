from parsers.ivi import IVI
from parsers.gamemania import GameMania
from parsers.news import News

news_url = "https://ria.ru/location_Minsk"
gamemania_url = "https://www.igromania.ru/articles/"
ivi_url = "https://www.ivi.ru/collections/populyarnoe-sejchas-movies"

# ivi for example
with IVI(ivi_url) as ivi:
    # parse() - generate a list of parsing items
    ivi.parse() 
    # display_item() - shows callable element in formatted string
    print(ivi[0], ' - first item')
    for el in ivi.parse():
        ivi.display_item(el)
from requests import get
from json import loads
from terminaltables import AsciiTable
from datetime import date
from datetime import datetime

def main():
    today = date.today()
    
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    
    imgw = 'https://danepubliczne.imgw.pl/api/data/synop'
    r = get(imgw)
    data = loads(r.text)

    print("-----------------------------------")
    print("Lista dostępnych miast dla pogody:")
    print("-----------------------------------")
    for city in data:
        print(city['stacja'])
    print("================================")
    
    cities = input("Podaje nazwę miasta lub kilku: ")
    
    head = [
    ['Dane dla dnia: ', 'Dla godziny: ']
        ]

    head.append([today, time])
    #head.append([cities['data_pomiaru'], cities['godzina_pomiaru']])
    htable = AsciiTable(head)

    body = [
        ['Miasto', 'Temperatura', 'Cisnienie', 'Godzina pomiaru']
    ]

    for city in data:
        if city['stacja'] in cities:
            body.append([
                city['stacja'],
                city['temperatura'],
                city['cisnienie'],
                city['godzina_pomiaru']+':00'
            ])
    table = AsciiTable(body)
    print(htable.table)
    print(table.table)
    
if __name__ == '__main__':
    main() 
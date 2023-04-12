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
    
    cities = input("Podaje nazwę miasta lub kilku. Jeśli chcesz wyświetlić pogodą dla wszystkich miast wpisz 'all' : ")
    
    if cities == '':
        print("*** Nie podałeś miasta ***")
    elif cities == "all":
        head = [
        ['Dane dla dnia: ', 'Dla godziny: ']
            ]

        head.append([today, time])
        htable = AsciiTable(head)

        body = [
            ['Miasto', 'Temperatura', 'Cisnienie', 'Godzina pomiaru']
        ]

        for city in data:
            body.append([
                city['stacja'],
                city['temperatura'],
                city['cisnienie'],
                city['godzina_pomiaru']
            ])
        table = AsciiTable(body)
        print(htable.table)
        print(table.table)
    else:
        head = [
        ['Dane dla dnia: ', 'Dla godziny: ']
            ]

        head.append([today, time])
        htable = AsciiTable(head)

        body = [
            ['Miasto', 'Temperatura', 'Cisnienie', 'Godzina pomiaru']
        ]

        for city in data:
            if city['stacja'] in cities:
                body.append([
                    city['stacja'],
                    city['temperatura']+ ' °C',
                    city['cisnienie']+ ' hPa',
                    city['godzina_pomiaru']+':00'
                ])
        table = AsciiTable(body)
        print(htable.table)
        print(table.table)
    
if __name__ == '__main__':
    main() 
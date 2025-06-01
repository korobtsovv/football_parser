#!/usr/bin/env python3

'''UPL.UA parser'''

import requests
from bs4 import BeautifulSoup
import sys

teams = {
        # 'chornomorets'  : '27',
        # 'dnipro1'       : '1807',
        'dynamo'        : '7',
        # 'epicentr'      : '',
        # 'inhulets'      : '1417',
        'karpaty'       : '1864',
        'kolos'         : '1806',
        'kryvbas'       : '1478',
        # 'livyi bereh'   : '1847',
        'lnz'           : '1813',
        # 'lviv'          : '3',
        # 'metalist'      : '1812',
        'metalist1925'  : '1810',
        # 'minaj'         : '1808',
        'obolon'        : '1565',
        'olexandria'    : '19',
        'polissya'      : '1814',
        # 'poltava'       : '',
        'rukh'          : '1809',
        'shakhtar'      : '28',
        'veres'         : '1811',
        'vorskla'       : '5',
        'zorya'         : '11'
        }
for i in teams:
    print(i)
print()
try:
    while True:
        team = input('Enter team name: ')
        if team in teams.keys():
            url = 'https://upl.ua/en/clubs/view/' + teams[team] + '/34?status=1'
            break
        else:
            print('Please, enter correct team name!')
except KeyboardInterrupt:
    print(' Exit')
    sys.exit(1)
try:
    headers = {
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    players = soup.find_all('div', class_='info')
    for player in players:
        link = player.find('a', href=True)
        url = 'https://upl.ua' + link['href']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml').find('div', class_='info')
        numbers = soup.find_all('div', class_="col-sm-6")
        for num in numbers:
            index = numbers.index(num)
            if num.text == 'Number':
                number = numbers[index + 1]
        if number.text == '-':
            continue
        else:
                number = number.text
        pseudonym = soup.find('div', class_='pseudonym')
        if pseudonym.text.strip() == '':
            fn = soup.find('div', class_='name').text.split()
            fn = fn[1].upper()
            ln = soup.find('div', class_='name').text.split()
            ln = ln[0].upper()
        else:
            fn = ''
            ln = pseudonym.text.strip().upper()
        role = soup.find('div', class_='amplua').text.upper()
        if role != 'GOALKEEPER':
            print('{},{},{},{}'.format(number, fn, ln, role))
        else:
            print('{},{},{} (GK),{}'.format(number, fn, ln, role))
        # break
except KeyboardInterrupt:
    print(' Exit')
    sys.exit(1)
print()
input("Press ENTER to close program")

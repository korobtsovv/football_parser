#!/usr/bin/env python3

'''UPL.UA parser'''

import requests
from bs4 import BeautifulSoup

helper = """
1) veres
2) dnipro1
3) lviv
4) olexandria
5) vorskla
6) zorya
7) kryvbas
8) rukh
9) metalist
10) inhulets
11) metalist1925
12) chornomorets
13) dynamo
14) kolos
15) minaj
16) shakhtar
"""

print(helper)
print()

teams = {'1': '1811',
         '2': '1807',
         '3': '3',
         '4': '19',
         '5': '5',
         '6': '11',
         '7': '1478',
         '8': '1809',
         '9': '1812',
         '10': '1417',
         '11': '1810',
         '12': '27',
         '13': '7',
         '14': '1806',
         '15': '1808',
         '16': '28'}

team = input('SELECT TEAM: ')
if team in teams.keys():
    url = 'https://upl.ua/en/clubs/view/' + teams[team] + '/32?status=0'
else:
    print('Wrong team code!')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

players = soup.find_all('div', class_='info')
# print(players)
print()

for player in players:
    # print(player)
    number = player.find('div', class_='number')
    if number:
        first_name = player.find('div', class_=False)
        last_name = player.find('span', class_='last-name')
        role = player.find('div', class_='role')
        print('{},{},{},{}'.format(number.text, first_name.text.split()[0].upper(), last_name.text.upper(), role.text.upper()))

print()
input("Press ENTER to close program")

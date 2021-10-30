#!/usr/bin/env python3

'''UPL.UA parser'''

import requests
from bs4 import BeautifulSoup

helper = """veres, dnipro1, lviv, olexandria,
vorskla, zorya, mariupol, rukh, 
desna, inhulets, metalist1925, chornomorets,
dynamo, kolos, minaj, shakhtar"""

print(helper)
print()

teams = {'veres': '1811',
         'dnipro1': '1807',
         'lviv': '3',
         'olexandria': '19',
         'vorskla': '5',
         'zorya': '11',
         'mariupol': '1803',
         'rukh': '1809',
         'desna': '6',
         'inhulets': '1417',
         'metalist1925': '1810',
         'chornomorets': '27',
         'dynamo': '7',
         'kolos': '1806',
         'minaj': '1808',
         'shakhtar': '28'}

team = input('SELECT TEAM: ')
if team in teams.keys():
    url = 'https://upl.ua/en/clubs/view/' + teams[team] + '/31?status=1'
else:
    print('Wrong team code!')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

players = soup.find_all('div', class_='info')
# print(players)
print()

for player in players:
    number = player.find('div', class_='number')
    if number:
        first_name = player.find('div', class_=False)
        last_name = player.find('span', class_='last-name')
        role = player.find('div', class_='role')
        if (role != None and role.text == 'Goalkeeper'):
            print('{},{},{} (GK)'.format(number.text, first_name.text.split()[0].upper(), last_name.text.upper()))
        else:
            print('{},{},{}'.format(number.text, first_name.text.split()[0].upper(), last_name.text.upper()))

print()
input("Press ENTER to close program")

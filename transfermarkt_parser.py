#!/usr/bin/env python3
'''transfermarkt.com parser'''

import requests
from bs4 import BeautifulSoup
import re

info = '''transfermarkt.com parser
Find football team and insert link from browser here...
'''

print(info)

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
url = input('ENTER URL: ')
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

regex = re.compile('^(odd|even)$')
players = soup.find_all('tr', {"class": regex})
print()

for player in players:
    # print(player)
    number = player.find('div', class_='rn_nummer')
    num = number.text
    if num[0].isdigit():
        name = player.find('td', class_='hauptlink')
        # print(name)
        first_name = name.text.split()[:-1]
        last_name = name.text.split()[-1]
        role = player.find('td', class_='zentriert rueckennummer bg_Torwart')
        if role != None:
            print('{},{},{} (GK)'.format(num, ' '.join(first_name).upper(), last_name.upper()))
        else:
            print('{},{},{}'.format(num, ' '.join(first_name).upper(), last_name.upper()))

print()
input("Press ENTER to close program")

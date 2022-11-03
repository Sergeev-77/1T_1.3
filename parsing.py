import json
from random import randint
from time import sleep

import requests as req
import tqdm
from bs4 import BeautifulSoup

'''
Парсим вакансии с hh.ru по запросу "python разработчик":
Название вакансии - title
Требуемый опыт работы - work experience
Заработную плату - salary
Регион - region
'''

headers = {
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }

data = []

for page in range(0, 15):
    url = f'https://hh.ru/search/vacancy?text=python+разработчик&page={page}'
    resp = req.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    items = soup.find_all(class_='serp-item__title')
    for item in tqdm.tqdm(items[0:-1]):
        item_descr = dict()
        item_descr['title'] = item.text
        url = item['href']
        resp = req.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        salary = soup.find(attrs={'data-qa': 'vacancy-salary'})
        work_exp = soup.find(attrs={'data-qa': 'vacancy-experience'})
        region = soup.find(attrs={'data-qa': 'vacancy-view-raw-address'})
        location = soup.find(attrs={'data-qa': 'vacancy-view-location'})
        item_descr['work experience'] = work_exp.text if work_exp else ''
        item_descr['salary'] = salary.text.replace(u'\xa0', u' ') if salary else ''
        item_descr['region'] = region.text.split(',')[0] if region else location.text.split(',')[0]
        data.append(item_descr)
        sleep(randint(2, 7))
    sleep(7)

with open('data.json', 'w', encoding='utf8') as file:
    json.dump({'data': data}, file, ensure_ascii=False)

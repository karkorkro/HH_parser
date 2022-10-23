import requests
import pprint
from json import dump

DOMAIN = 'https://api.hh.ru/'
url_vac = f'{DOMAIN}vacancies'

for i in range(8):
    params = {
        'text': 'python developer',
        'page': i+1
    }
    vacancies = requests.get(url_vac, params=params).json()
    items = vacancies['items']

    skills = []
    for i, v in enumerate(items):
        single_vac_url = items[i]['url']
        single_vac_data = requests.get(single_vac_url, params=params).json()
        single_vac_skills = single_vac_data['key_skills']
        single_vac_skills = [i['name'].lower() for i in single_vac_skills]
        skills.extend(single_vac_skills)


skills_stats = [{'name': i, 'count': skills.count(i), 'percent': skills.count(i)*len(skills)/100}
                 for i in set(skills)]
skills_stats.sort(key=lambda d: d['count'])
pprint.pprint(skills_stats)

with open('vacancies_info.json', mode='w') as f:
    dump([skills_stats], f)
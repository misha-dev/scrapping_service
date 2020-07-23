import sys
import codecs
import datetime as dt
import os
import asyncio
proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scrapping_service.settings"
import django
django.setup()
from scrapper.parsers import *
from scrapper.models import Jobs, City, Language
from django.db import DatabaseError
parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'), (dou,
                                                         'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D0%B5%D0%B2&category=Python'),
    (djinni, 'https://djinni.co/jobs/?location=%D0%9A%D0%B8%D0%B5%D0%B2&primary_keyword=Python'),
    (rabota, 'https://rabota.ua/jobsearch/vacancy_list?keyWords=Python&regionId=1')
)
city = City.objects.filter(slug='kiev').first()
language = Language.objects.filter(slug='python').first()
jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e
if errors:
    er = Error(data=errors).save()

for job in jobs:
    v = Jobs(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass


h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()

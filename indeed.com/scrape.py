from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import csv
import math
import httpx
import asyncio

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37" #type:ignore
headers = {
    'User-Agent': agent
}

def extract_num(str):
    list = [i for i in str if i.isdigit()]
    num = ''.join(list)
    return int(num or 0)

currencyValue = {
    '$': 78,
    '€': 80
}

def yearlySalary(salary):
    if not salary:
        return [0, 0]
    price = salary.split('-')
    if len(price) == 1:
        price.append('0')

    start = extract_num(price[0])
    end = extract_num(price[1])
    try:
        currency = currencyValue[salary[0]]
    except:
        currency = ''

    if currency:
        start *= currency
        end *= currency
    if salary.__contains__('year'):
        return [start, end]
    elif salary.__contains__('month'):
        return [extract_num(price[0])* 12, extract_num(price[1])* 12]

def apply_jobs(j):
    base_url = 'https://in.indeed.com/viewjob?jk='
    try:
        res = requests.get(f"{base_url}{j['jobkey']}", headers=headers)
        html = BeautifulSoup(res.content, 'html.parser')
        apply = html.find('div', class_ = 'ia-IndeedApplyButton')
        details = apply.find('span').attrs
        posturl = details.get('data-indeed-apply-posturl', '')
        questions = details.get('data-indeed-apply-questions', '')
        status = details.get('data-indeed-apply-onappliedstatus', '')
        onready = details.get('data-indeed-apply-onready', '')
        jobid = details.get('data-indeed-apply-jobid', '')
        cover = details.get('data-indeed-apply-coverletter', '')
        pingbackurl = details.get('data-indeed-apply-pingbackurl', '')
        # nobuttonui = details.get('data-indeed-apply-nobuttonui', '')
        apitoken = details.get('data-indeed-apply-apitoken', '')
        phone = details.get('data-indeed-apply-phone', '')
    except:
        pass
    finally:
        job = {**j, 'posturl': posturl or '', 'questions': questions or '', 'status': status or '', 'onready': onready or '', 'jobid': jobid or '', 'cover': cover or '', 'pingbackurl': pingbackurl or '', 'apitoken': apitoken or '', 'phone': phone or ''}
        return job

def init_jobs(job_query: str, job_location: str, posted_days: int):
    base_url = 'https://in.indeed.com/jobs?'
    total_jobs = 0
    def total_pages():
        nonlocal total_jobs
        params = {'q': job_query, 'l': job_location, 'start': 0, 'fromage': posted_days}
        url = f'{base_url}{urlencode(params)}'
        res = requests.get(url, headers=headers)
        html = BeautifulSoup(res.content, 'html.parser')
        pages = html.find('div', id='searchCountPages').text.replace('Page 1 of ', '').replace('jobs', '').replace(' | 13', '').strip()
        total_jobs = math.floor(int(pages))
    total_pages()
    print(f'{total_jobs} Total jobs found')

    async def get():
        start = 0
        with open('jobs.csv', 'a') as f:
                    header = ['jobkey', 'title', 'company', 'location', 'salary']
                    writer = csv.DictWriter(f, header)
                    writer.writeheader()
                    async with httpx.AsyncClient() as client:
                        while(start<total_jobs):
                            print('Getting data...')
                            params = {'q': job_query, 'l': job_location, 'start': start, 'fromage': posted_days}
                            start += 10
                            url = f'{base_url}{urlencode(params)}'
                            res = await client.get(url, headers=headers)
                            html = BeautifulSoup(res.content, 'html.parser')
                            results = html.find_all('td', class_ = 'resultContent')
                            for item in results:
                                a = item.find('a')
                                jobkey = a.attrs['data-jk']
                                title = a.text.strip()
                                company_and_location = item.find('div', class_ = 'companyInfo')
                                company = company_and_location.find('span').text
                                location = company_and_location.find('div').text
                                salary_and_shift = item.find('div', class_='salaryOnly')
                                try:
                                    salary = salary_and_shift.find('div', class_ = 'attribute_snippet').text
                                except:
                                    salary = ''
                                writer.writerow({
                                'jobkey': jobkey,
                                'title': title,
                                'company': company,
                                'location': location,
                                'salary': yearlySalary(salary)
                            })
                            print('Data added')
    return get

jobs = init_jobs('front end developer', 'remote', 14)()
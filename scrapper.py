import requests
from bs4 import BeautifulSoup

def extract_pages(url):
    result=requests.get(url)
    soup=BeautifulSoup(result.text,'html.parser')
    paginations= (soup.find("div",{"class":"s-pagination"})).find_all("span")
    last_page=int(paginations[-2].string)
    
    return last_page

def extract_jobs(last_page,url):
    jobs=[]
    for page in range(last_page):
        result= requests.get(f"{url}&pg={page+1}")
        soup=BeautifulSoup(result.text,'html.parser')
        results=soup.find_all("div",{"class":"-job"})
        for result in results:
            jobs.append(extract_job(result))
    return jobs

def extract_job(html):
    title=(html.find("a",{"class":"s-link"})).string
    company,location=html.find("h3",{"class":"fc-black-700"}).find_all("span",recursive=False)
    company=company.get_text(strip=True)
    location=location.get_text(strip=True).strip("-")
    id=html["data-jobid"]

    return {'title':title,'company':company,'location':location,'link':f'https://stackoverflow.com/jobs/{id}'}

def get_jobs(word):
    url=f"https://stackoverflow.com/jobs?q={word}&sort=i"
    last_page=extract_pages(url)
    jobs=extract_jobs(last_page,url)  

    return jobs
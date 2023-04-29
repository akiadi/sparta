from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests import get
from bs4 import BeautifulSoup

def get_page_count(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dav-shm-usage")
    options.add_argument("lang=ko_KR")
    browser = webdriver.Chrome(options=options)

    base_url = "https://kr.indeed.com/jobs"
    browser.get(f"{base_url}?q={keyword}")
    if True:
        soup = BeautifulSoup(browser.page_source, "html.parser")
        pagination = soup.find_all("div", class_="css-tvvxwd ecydgvn1")
        count = (len(pagination))
        if pagination is None:
            return 1
        elif count >= 5:
            return 5
        else:
            return count


def extract_indeed_jobs(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dav-shm-usage")
    options.add_argument("lang=ko_KR")
    browser = webdriver.Chrome(options=options)
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        browser.get(final_url)
        print("Requesting", final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul",class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)
        
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://kr.indeed.com{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title
                }
                for _ in job_data:
                    if job_data[_] != None:
                        job_data[_] = job_data[_].replace(",", " ")
                results.append(job_data)
    return results
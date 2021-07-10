from selenium import webdriver
from selenium.webdriver import ActionChains
import bs4
import requests
import re


def result_clicker(producturl):
    res = requests.get(producturl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    temp = soup.find_all('a', class_='text-dark text-truncate_3')

    url_list = []

    for each_result in temp:
        each_result = str(each_result)
        x = each_result.split("href=", 1)[1]
        x = x.split(" onclick")[0]
        x = x.strip('"')
        url_list.append(x)
    return url_list


def gpustockcheck(producturl):
    res = requests.get(producturl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    temp = soup.find('div', class_='pi-prod-availability')
    temp = temp.text.strip()

    return temp


def gpucheck(keyword):
    search_url = 'https://www.canadacomputers.com/search/results_details.php?language=en&keywords=' + keyword + '&cpath=43' # cpath=43 is GPU filter

    temp = []
    for each_result in result_clicker(search_url):
        temp.append(gpustockcheck(each_result))
    return temp



"""
def result_clicker2(searchpage):
    res = requests.get(searchpage)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    temp = soup.find_all('a', class_='text-dark text-truncate_3')
    browser = webdriver.Chrome()
    browser.get(searchpage)

    ActionChains(browser).move_to_element(menu).click(hidden_submenu).perform()
    
    for i in range(temp):
        selenium clicks each link specified by css element  text-dark text-truncate_3
"""



"""
def gpucheck():
    for gpudict_url in gpulist:
        browser = webdriver.Chrome()
        browser.get(gpudict_url)
        searchElem = browser.find_element_by_css_selector('#pi-form > div.col-12.py-2 > div.bg-grey.border.position-relative.pi_loc-stock__box.border-danger > div.check-bg.stocklevel.bg-danger')
        return searchElem
        
        gpucheck('https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183210')
        
        
         
def no_results(keyword):
    ccurl = 'https://www.canadacomputers.com/search/results_details.php?language=en&keywords=' + keyword + '&cpath=43'

    res = requests.get(ccurl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    num_results = soup.select('#search-results > div.row.mb-1 > div.col-auto.small.text-secondary')
    return num_results[0].text.strip()
"""




from selenium import webdriver
import bs4
import requests

gpudict = ['https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183210',
           'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183499'
           ]


def gpucheck(keyword):
    ccurl = 'https://www.canadacomputers.com/search/results_details.php?language=en&keywords=' + keyword + '&cpath=43'

    res = requests.get(ccurl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    num_results = soup.select('#search-results > div.row.mb-1 > div.col-auto.small.text-secondary')
    return num_results[0].text.strip()

    return num_results

    for gpudict_url in gpudict:
        browser = webdriver.Chrome()
        browser.get('gpudict_url')
        searchElem = browser.find_element_by_css_selector('#pi-form > div.col-12.py-2 > div.bg-grey.border.position-relative.pi_loc-stock__box.border-danger > div.check-bg.stocklevel.bg-danger')
        if 'danger' in searchElem




"""
browser = webdriver.Chrome()
searchElem = browser.find_element_by_css_selector('jquery-live-search')
searchElem.send_keys('3070')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
"""

from selenium import webdriver
from selenium.webdriver import ActionChains

import bs4
import requests

"""
Only to be used with Canadacomputers.com
ex: result_clicker('3070')

"""
def result_clicker(keyword):
    search_url = 'https://www.canadacomputers.com/search/results_details.php?language=en&keywords=' + keyword + '&cpath=43'  # cpath=43 is GPU filter

    driver = webdriver.Chrome()
    driver.get(search_url)

    res = requests.get(search_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    num_results = soup.select('#search-results > div.row.mb-1 > div.col-auto.small.text-secondary')
    num_results = num_results[0].text.strip()
    num_results = num_results[0]
    num_results = int(num_results)

    n = 2  # starting position for page results
    temp = '#product-list > div:nth-child(' + str(n) + ') > div > div > div.col-12.productImageDesc > div > div.px-0.col-12.productInfoSearch.pt-2 > span.text-dark.d-block.productTemplate_title > a'
    css_button = driver.find_element_by_css_selector(temp)

    in_stock_list = []

    for i in range(num_results):  #potential error?
        ActionChains(driver).move_to_element(css_button).click().perform()
        if gpustockcheck(driver.current_url):
            in_stock_list.append(driver.current_url)
        n += 2
        driver.back()

    return in_stock_list


def gpustockcheck(producturl):
    res = requests.get(producturl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    stock_check = soup.find('div', class_='pi-prod-availability')
    stock_check = stock_check.text.strip()

    return not "Not Available" in stock_check



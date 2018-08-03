import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

zapProductsList = []

def search_results_zap(keyword, zapProductsList):
    del zapProductsList[:]

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    values = {'keyword': keyword}
    p_values = urllib.parse.urlencode(values)

    url = 'https://www.zap.co.il/search.aspx?' + p_values
    req = urllib.request.Request(url, headers=header)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html, "lxml")

    products = soup.find_all(class_="ProductBox CompareModel")


    for p in products:
        element = {}

        price = p.find(class_="Prices")
        price_only = str(p.find(class_="pricesTxt").text)
        new_price2 = price_only.replace(" ", "")
        last_price = new_price2[2:-2]

        p_info = str(p.find(class_="ProdInfo").find(class_="ProdInfoTitle").text)
        last_info = p_info.replace("\n", "")

        element["title"] = last_info
        element["price"] = last_price
        zapProductsList.append(element)


odProductList = []

def search_results_officeDepot(keyword, zapProductsList):
    del odProductList[:]

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    values = {'q': keyword}
    p_values = urllib.parse.urlencode(values)

    url = 'http://www.officedepot.co.il/?' + p_values
    req = urllib.request.Request(url, headers=header)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html, "lxml")
    # print(soup.prettify())

    products = soup.find(class_="store_list_items").find_all('div', class_="grid a")

    for p in products:
        element = {}

        price = p.find(class_="list_item_show_price").strong.text
        p_info = p.find(class_="list_item_title_with_brand").text
        last_info = p_info.replace("\n", "")

        element["title"] = str(last_info)
        element["price"] = str(price)
        odProductList.append(element)


ivoryProductList = []

def search_results_ivory(keyword, ivoryProductList):
    del ivoryProductList[:]

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    values = {'q': keyword}
    p_values = urllib.parse.urlencode(values)

    url = 'https://www.ivory.co.il/catalog.php?act=cat&site-search=1&' + p_values
    req = urllib.request.Request(url, headers=header)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html, "lxml")
    # print(soup.prettify())

    products = soup.find_all(class_="js-item_block")

    for p in products:
        lines = p.find_all('tr')
        p_price = lines[5]
        if p_price.span != None:
            new_price = str(p_price.span.text).replace("\t", "")
            new_price2 = new_price.replace("\n", "")

            p_info = str(lines[0].text)
            last_info = p_info.replace("\n", "")

            element = {}
            element["title"] = last_info
            element["price"] = new_price2
            ivoryProductList.append(element)











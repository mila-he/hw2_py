import requests
import time
from bs4 import BeautifulSoup

start_url = 'https://onoff.ee/et/35-televiisorid'


# print(page)
def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
    print (soup)

    tvs_list = soup.find_all("article", class_='ajax_block_product')
    # print(tvs_list)

    for tv in tvs_list:
        data = {'name': '', 'price': '', 'image': '', }
        data['name'] = tv.h1.get_text()
        data['price'] = tv.find('div', class_='col').dd.text
        data['image'] = tv.a['href']
        print(data)

    try:
        next_page = soup.find("li", class_='page-item ').a['href']
        if next_page:
            time.sleep(6)  # to avoid http response 429
            print("----------------------------", next_page)
            parse(next_page)
    except:
        print("No more pages")


if __name__ == '__main__':
    parse(start_url)


    #class ="fto-right-open-3"
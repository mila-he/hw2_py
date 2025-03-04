import requests
import time
from bs4 import BeautifulSoup

start_url = 'https://onoff.ee/et/35-televiisorid'


# print(page)
def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
    #    print (soup)

    tvs_list = soup.find_all("article", class_='set')
    # print(brics_list)

    for tv in tvs_list:
        data = {'name': '', 'price': '', 'image': '', }
        try:
            data['name'] = tv.h1.get_text()
            data['pieces'] = tv.find('div', class_='col').dd.text
            dataminif = tv.find('dt', string='Minifigs').find_next('dd').string
            # for minif in dataminif:
            data['minifigs'] = dataminif
        except AttributeError:
            data['minifigs'] = "No minifigs"
        data['image'] = tv.a['href']
        print(data)

    try:
        next_page = soup.find("li", class_='next').a['href']
        if next_page:
            time.sleep(6)  # to avoid http response 429
            print("----------------------------", next_page)
            parse(next_page)
    except:
        print("No more pages")


if __name__ == '__main__':
    parse(start_url)
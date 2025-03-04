import requests
import time
from bs4 import BeautifulSoup

start_url = 'https://onoff.ee/et/35-televiisorid'


def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')

    tvs_list = soup.find_all("article", class_='ajax_block_product')

    for tv in tvs_list:
        data = {'name': '', 'price': '', 'image': ''}

        # Toote nimi ja URL
        link = tv.find('a')
        data['name'] = link.get('title')  # Toote nimi title atribuudist

        # Hinna leidmine
        price_tag = tv.find('span', class_='price')
        data['price'] = " ".join(price_tag.get_text().split()).replace("\n", "")

        # Pildi leidmine data-src alt
        image_tag = tv.find('img')
        img_url = image_tag['data-src']
        # Kontrollime, kas URL on täielik või suhteline
        data['image'] = img_url

        print(data)

    # Järgmise lehe kontroll

    try:
        next_page_tag = soup.find('a', rel='next')  # Otsime <a> tagi rel="next" atribuudiga
        if next_page_tag:
            next_page = next_page_tag.get('href')
            if next_page:
                time.sleep(6)  # et vältida HTTP 429 vastust
                print("----------------------------", next_page)
                parse(next_page)
        else:
            print("No more pages")
    except Exception as e:
        print("Viga järgmise lehe leidmisel:", e)


if __name__ == '__main__':
    parse(start_url)
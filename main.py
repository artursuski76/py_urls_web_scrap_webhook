import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = 'https://www.website_for_scrap.com'
WEBHOOK_URL = 'https://your_apps_for_webhook_send_with_internal_links.com/webhook'

def send_webhook(url):
    params = {'url': url}
    response = requests.get(WEBHOOK_URL, params=params)
    if response.status_code == 200:
        print(f'Successfully sent webhook for URL: {url}')
    else:
        print(f'Failed to send webhook for URL: {url}')

def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Znajdź wszystkie linki na stronie
    links = soup.find_all('a')

    # Licznik znalezionych linków
    count = 0

    # Przejdź przez każdy znaleziony link
    for link in links:
        href = link.get('href')

        # Pomijaj linki oznaczone jako "#"
        if href and href != '#':
            # Użyj urljoin, aby połączyć względny link z bazowym adresem URL
            full_link = urljoin(BASE_URL, href)

            # Wyślij webhook z linkiem
            send_webhook(full_link)

            # Poczekaj 1 sekundę przed przetworzeniem następnego linku
            time.sleep(1)

            count += 1

    return count

# Główna funkcja, rozpoczynająca przeszukiwanie stron
def main():
    url = 'https://www.website_for_scrap.com'
    link_count = scrape_links(url)
    print(f'Total links found: {link_count}')

if __name__ == '__main__':
    main()

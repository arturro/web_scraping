import os

import requests
from bs4 import BeautifulSoup

# Zadanie 1
# Pobierz link do aktualnego artykułu dnia na wikipedii
# (ale przy pomocy BeautifulSoup)

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(response.content, 'html.parser')

my_div = soup.find(id="mp-tfa")
my_a_tag = my_div.find("a", string="Full\xa0article...")
full_link = "https://en.wikipedia.org" + my_a_tag.get("href")
print(full_link)

# Zadanie 2
# Pobierz listę dat z sekcji "On this day" na wikipedii
# (ale przy pomocy BeautifulSoup)

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup = BeautifulSoup(response.content, 'html.parser')

my_div = soup.find(id="mp-otd")
first_list = my_div.find("ul")
list_items = first_list.find_all("li")

years = []
for item in list_items:
    first_link = item.find("a")
    years.append(first_link.text)

print(years)

# Zadanie 3
# Pobierz najnowsze wyniki losowania Lotto ze strony lotto.pl
# (ale przy pomocy BeautifulSoup)
# to działa

headers = {
    'authority': 'www.lotto.pl',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'pl,en-US;q=0.9,en;q=0.8,en-GB;q=0.7,ru;q=0.6',
    'cookie': 'ai_user=zSWWsqs2ElMZUeV+bNxT8Z|2021-06-12T07:50:31.860Z; ai_session=87L7vwHm17boAqgeoKdQKt|1641570860274|1641570860274',
}

response = requests.get("https://www.lotto.pl/lotto/wyniki-i-wygrane", headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

newest_lotto_result = soup.find("div", class_="recent-result-item Lotto")
value_divs = newest_lotto_result.find_all("div", class_="scoreline-item circle")

numbers = []
for tag in value_divs:
    value = tag.text
    numbers.append(int(value.strip()))

print(numbers)

# Zadanie 4
# Pobierz losowy komiks z xkcd.com (sam obrazek) i zapisz na dysku
# (Po pobraniu obrazka wystarczy zapisać do pliku w trybie binarnym)

response = requests.get("https://c.xkcd.com/random/comic/")
soup = BeautifulSoup(response.content, 'html.parser')

comic_div = soup.find("div", id="comic")
img_tag = comic_div.find("img")
image_src = img_tag.get("src")

print(image_src)

response = requests.get("https:" + image_src)
image_data = response.content

comic_filename = os.path.basename(image_src)
with open(comic_filename, "wb") as comic_file:
    comic_file.write(image_data)

# Zadanie 5
# Pobierz aktualny kurs CDPROJEKT ze strony gpw.pl

response = requests.get("https://www.gpw.pl/spolka?isin=PLOPTTC00011")
soup = BeautifulSoup(response.content, 'html.parser')

summary_span = soup.find("span", class_="summary")
text_value = summary_span.text
value = float(text_value.replace(",", "."))

print(value)

# Zadanie 6
# Napisz skrypt, który będzie sprawdzał listę najnowszych pytań na stackoverflow.com co minutę
# Wypisz linki do pytań z tagiem python
# BONUS Zadbaj o to, aby nie powtarzać raz wypisanych linków

# ZADANIE DOMOWE
# Są dwa podejścia:
# 1. Przejdź przez wszystkie najnowsze pytania i sprawdź, czy mają tag python
# 2. W sekcji najnowsze pytania znajdź wszystkie tagi python i z tego wyłuskaj pytania których dotyczą

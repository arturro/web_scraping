import requests
from lxml import html

# Zadanie 1
# Pobierz link do aktualnego artykułu dnia na wikipedii

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
tree = html.fromstring(response.content)

# W określonym div szukam linka z konkretnym tekstem
result = tree.xpath("//div[@id=\"mp-tfa\"]//a[contains(text(),\"Full\xa0article...\")]/@href")[0]
full_link = "https://en.wikipedia.org" + result
print(full_link)

# Zadanie 2
# Pobierz listę dat z sekcji "On this day" na wikipedii

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")
tree = html.fromstring(response.content)

dates = tree.xpath("//div[@id=\"mp-otd\"]/ul[1]/li/a[1]/text()")
print(dates)

# Zadanie 3
# Pobierz najnowsze wyniki losowania Lotto ze strony lotto.pl
# do poprawy, zdezaktualizowało się

response = requests.get("https://www.lotto.pl/lotto/wyniki-i-wygrane")
tree = html.fromstring(response.content)

lotto_results = tree.xpath("//div[@class=\"recent-result-item Lotto\"]")
newest_result = lotto_results[0]
values = newest_result.xpath(
    "./div/div[@class=\"result-item__balls-box\"]/div[@class=\"scoreline-item circle\"]/text()")
numbers = [int(val.strip()) for val in values]
print(numbers)

import os

from bs4 import BeautifulSoup

# Wczytanie zawartości strony z pliku

page_path = os.path.join(os.path.dirname(__file__), "example.html")
# page_path = os.path.join(os.getcwd(), ""example.html")
# page_path = os.path.join("exercises", "code", "example.html")
with open(page_path) as page_file:
    page = page_file.read()

# Parsowanie zawartości strony

soup = BeautifulSoup(page, 'html.parser')
print(soup)
# dir(soup)
print(soup.title)

# Wyszukiwanie elementów (równiez po atrybutach)

# id
result = soup.find(id="test")
print(result)

# class
result = soup.find_all("table", {"class": "content_table"})
print(result)
print(type(result[0]))

print(result[0].name)
print(result[0].attrs)

# Znaczniki
result = soup.find_all("li")
print(result)
text_only = [tag.text for tag in result]
print(text_only)

# Wykorzystanie lambda w wyszukiwaniu
result = soup.find_all(lambda tag: tag.name == "p" in tag.text)
print(result)

# Przejście do rodzica
row_1 = soup.find(id="row_1")
print(row_1)

headers_parent = row_1.parent
print(headers_parent.name)
result = headers_parent.find_all("p")
print(result)

# Wyszukiwanie wewnątrz elementów działa tak samo
body = soup.body
print(body)
print(type(body))

links = body.find_all("a")
print(links)

urls = [tag.get("href") for tag in links]
print(urls)

# jeszcze takie chodzenie
body.find(id="test").p.string

links = body.find_all("a")
print(links)

[{'href': el.attrs['href'], 'name': el.text} for el in links]


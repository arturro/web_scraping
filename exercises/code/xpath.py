import os

import requests
from lxml import html

# Wczytanie zawartości strony z pliku

page_path = os.path.join(os.path.dirname(__file__), "example.html")
with open(page_path) as page_file:
    page_content = page_file.read()

print(page_content)

# Parsowanie zawartości strony

tree = html.fromstring(page_content)
print(tree)

# dir Twoim przyjacielem
dir(tree)

# bierzemy wszystkie węzły
result = tree.xpath("//*")
print(result)

# dir Twoim przyjacielem
dir(result)

# lista więc może spróbujmy tak
for item in result:
    print(item)

print(type(result[0]))
print(result[2].text)
for item in result:
    print(f'{item}: {item.text}')

# Korzystanie z węzłów

result = tree.xpath("//h1")
print(result)
print(type(result))

print(result[0].attrib)
print(result[0].text)

# Przejście do rodzica
header_node = tree.xpath("//h1")[0]

result = header_node.xpath("./p")
print(result)

result = header_node.xpath("../p")
print(result)

result = tree.xpath("//a")
print(result)

print(result[0].attrib)
print(result[0].text)

# Otrzymywanie wyników z zapytania xpath

# Text
result = tree.xpath("//li/text()")
print(result)

# Wartość atrybutu
result = tree.xpath("//a/@href")
print(result)

# Określanie warunków liczbowych
result = tree.xpath("//table[@border>3]")
print(result)

# Zaprzeczenia
result = tree.xpath("//table[not(@border>3)]")
print(result)

# Określanie warunków tekstowych
result = tree.xpath("//a[contains(text(), \"inny\")]/@href")
print(result)

# Tworzenie drzewa na podstawie wyniku zapytania

page = requests.get("https://pl.wikipedia.org/wiki/XPath")
tree = html.fromstring(page.content)

result = tree.xpath("//*[@id=\"toc\"]/ul/li/a/span[@class=\"toctext\"]/text()")
print(result)

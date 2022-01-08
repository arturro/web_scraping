import requests
from bs4 import BeautifulSoup
from lxml import html

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://nagrzyby.pl/atlas-obrazkowy',
    'Accept-Language': 'pl,en-US;q=0.9,en;q=0.8,en-GB;q=0.7,ru;q=0.6',
    'Cookie': 'cookielawinfo-checkbox-necessary=yes',
}
response = requests.get("https://nagrzyby.pl/atlas?id=269", headers=headers)

###################################################################
# BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

fungi_name = soup.find("div", id="div_nazwa").find("h1").text
print(fungi_name)
# płomiennica zimowa


###################################################################
# lxml
from lxml import etree

my_parser = etree.HTMLParser(encoding="utf-8")
tree = etree.HTML(response.content, parser=my_parser)
tree = html.fromstring(response.content, parser=my_parser)
fungi_name = tree.xpath('//*[@id="div_nazwa"]/h1/text()')
print(fungi_name)

result = tree.xpath('//*[@id="toc"]/ul/li/a/span[@class="toctext"]/text()')

tree.xpath('//*[@id="div_nazwa"]/text()')
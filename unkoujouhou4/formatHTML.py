from bs4 import BeautifulSoup

with open('index_before.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

with open('index.html', mode='w') as f:
    f.write(soup.prettify())

# print(soup.prettify())
from bs4 import BeautifulSoup
html = "C:\\Users\\Ivan Podmogilniy\\Desktop\\My life\\Sites\\Etsy\\JohnnyAlex\\pages\\etsy1.html"
html2 = "C:\\Users\\Ivan Podmogilniy\\Desktop\\My life\\Sites\\Etsy\\JohnnyAlex\\pages\\etsy2.html"
html3 = "C:\\Users\\Ivan Podmogilniy\\Desktop\\My life\\Sites\\Etsy\\JohnnyAlex\\pages\\etsy3.html"

data1 = open(html, 'r').read()
data2 = open(html2, 'r').read()
data3 = open(html3, 'r').read()

soup1 = BeautifulSoup(data1)
soup2 = BeautifulSoup(data2)
soup3 = BeautifulSoup(data3)

soups = [soup1, soup2, soup3]

gathered_data = []

def find_entries_in_soup(soup):
    data = []
    for a in soup.findAll('a', {'class':'text-gray'}):
        if '@' in a.text.strip():
            data.append(a.text.strip())
    return data

for soup in soups:
    entries = find_entries_in_soup(soup)
    for entry in entries:
        gathered_data.append(entry)

print(gathered_data)


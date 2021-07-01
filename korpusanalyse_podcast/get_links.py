from lxml import etree



data = etree.parse("coronaticker_2021_05.xml")
all_urls = ""
for element in list(data.iter("text")):
    date = element.get("url")
    all_urls += "\n" + date



with open('urls.txt', 'w') as f:
    f.write(all_urls)

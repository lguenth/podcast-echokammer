from os import link
import requests
import re
from bs4 import BeautifulSoup
output_path = "new_texts_dlf"
links_path = "urls copy.txt"
weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
month_number_dict =	{
  "Januar": "01" ,
  "Februar": "02",
  "März": "03",
  "April": "04",
  "Mai": "05",
  "Juni": "06",
  "Juli": "07",
  "August": "08",
  "September": "09",
  "Oktober": "10",
  "November": "11",
  "Dezember": "12",
}
h3_urls= ["https://www.deutschlandfunk.de/newsblog-zum-coronavirus-die-entwicklungen-vom-27-bis-28.2852.de.html?dram:article_id=486669", "https://www.deutschlandfunk.de/newsblog-zum-coronavirus-die-entwicklungen-vom-29-bis-30.2852.de.html?dram:article_id=486762",
"https://www.deutschlandfunk.de/newsblog-zum-coronavirus-die-entwicklungen-vom-31-oktober.2852.de.html?dram:article_id=486964"]

with open(links_path) as f:
    urls = [line.rstrip() for line in f]

year = "2020"

andere_Formatierung = ""
month=""

for url in urls:
    
    print(2)
    print(url)
    print(3)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    aufgenommen = False
    if url in h3_urls:
        ps= soup.find_all(["p", "h3", "h2"])
    else:
        ps = soup.find_all("p")
    text = ""
    date = "delete"

    for p in ps:
        if p.text.startswith(tuple(weekdays)) or p.text.startswith("Entwicklungen"):
            if month=="01":
                year = "2021"
                print("jahreswechsel")
            if month=="12":
                year = "2020"
            with open('%s/%s.txt' %(output_path, date), 'a') as f:
                f.write(text)
            month = ""
            for key in month_number_dict:
                if key in p.text:
                    month = month_number_dict[key]
            
            day_list=re.findall(r'\d+',p.text)
            if len(day_list[0]) == 1:
                day = "0"+day_list[0]
            else: 
                day = day_list[0]
            
            date = year+ "-" + month + "-" + day
            text = ""
            
            print(date)
            aufgenommen = True
        elif p.text.startswith("Unser Archiv"):
            print("archiv")
            break
        else:
            text += p.text
    if aufgenommen is not True:
        andere_Formatierung += "\n"+url
    with open('%s/%s.txt' %(output_path, date), 'a') as f:
        f.write(text)

with open ("andere_formatierung.txt", 'a') as f:
    f.write(andere_Formatierung)
        


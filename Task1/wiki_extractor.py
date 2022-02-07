import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import wikipedia
import json

keyword = ""
if("--keyword=" in  sys.argv):
    keyword = sys.argv[sys.argv.index("--keyword=") + 1]

num_urls=0
if("--num_urls=" in sys.argv):
    num_urls = sys.argv[sys.argv.index("--num_urls=") + 1]

output="none"
if("--output=" in sys.argv):
    output = sys.argv[sys.argv.index("--output=") + 1]

print(keyword, num_urls, output)

result = wikipedia.search(keyword, results=num_urls)

file=[]

for s in result:
    s=s.replace(" ","_")
    page = "https://en.wikipedia.org/wiki/" + s
    print(page)
    dict = {}
    try:
        source = urlopen(page).read()
        soup = BeautifulSoup(source,'html.parser')
        para = soup.findAll('p', {'class':''})[1].get_text()
        # print(para)
        dict['url'] = page
        dict['paragraph'] = para

        file.append(dict)
    except:
        continue

with open(output, "w") as outfile:
    json.dump(file, outfile)


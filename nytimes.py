from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

article = []

url = 'https://cn.nytimes.com/usa/20181010/tax-report-part-3/dual/'

url_ob = urlopen(url)

soup = BeautifulSoup(url_ob, 'html.parser')

text_html = soup.find_all('div', class_ = 'article-paragraph')


for i in text_html:
	article.append(i.text)
	

header = ['EN','CN']
whole = [header]

EN = article[::2]
CN = article[1::2]
EN_CN = [EN, CN]

'''>>> lst = [['a','b','c'], [1,2,3], ['x','y','z']]
>>> lst2 = [item[0] for item in lst]
>>> lst2
['a', 1, 'x']'''

for i in range(0, len(EN)):
	each_part = [item[i] for item in EN_CN]
	whole.append(each_part)

print(whole)

with open('nyt.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(whole)

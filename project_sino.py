from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time

chrome_path = r"/home/wow/Desktop/selenium_test/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get('http://210.72.20.108')


print('tasks done, now sleeping for 15 seconds')
for i in range(15,0,-1):
    time.sleep(1)
    print(i)

driver.get('http://210.72.20.108/index/list_1.jsp?fn_name=&fn_orig=&fn_lang=10591002')

cn = []
en = []

for i range(0, 776):
	try:
		print('now sleeping for 5 seconds')
		for i in range(3,0,-1):
		    time.sleep(1)
		    print(i)
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		
		lists_cn = soup.find_all('div', class_ = 'datagrid-cell datagrid-cell-c1-fn_name')
		for a in lists_cn:
			print(a.text)
			cn.append(a.text)
		
		lists_en = soup.find_all('div', class_ = 'datagrid-cell datagrid-cell-c1-fn_orig')
		for b in lists_en:
			print(b.text)
			en.append(b.text)
		elem = driver.find_element_by_xpath("//span[@class='l-btn-icon pagination-next']")    
		elem.click()
	except:
		break	


pair = [cn, en]
entire = [['cn', 'en']]

for i in range(0, len(cn)):
	pairs = [a[i] for a in pair]
	entire.append(pairs)

with open('chi.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(entire)	
print('completed')

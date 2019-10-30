from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import csv
import time

class NYT:
	def __init__(self, channel):
		self.channel = channel
	def get_page_links(self, start_page, end_page):
		endpage = end_page + 1
		base_url = 'https://cn.nytimes.com'
		urls = []
		for p in range(start_page, endpage):
			time.sleep(1)
			url = 'https://cn.nytimes.com/' + self.channel + '/' + str(p)
			suffix = 'dual'
			for a in range(0,3):
				try:
					url_ob = urlopen(url)
				except:
					print('get links one more last time')
				else:
					break
			else:
				print('we have tried')		
			soup = BeautifulSoup(url_ob, 'html.parser')
			h3_tags = soup.find_all('h3')
			for i in h3_tags:
				a_tag = i.contents
				for i in a_tag:
					ref = i.get('href')
					whole_url = base_url + ref + suffix
					urls.append(whole_url)			
		return urls	
	
	def urls_generator(self, urls):
		with open('links_weve_downloaded.txt', 'a') as f:
			for i in urls:
				f.write(i + '\n')
							
	def parse_each_url(self, page_links):		
		with open('links_weve_downloaded.txt') as f:
			links_downloaded = f.readlines()
		page_links_n = [i+'\n' for i in page_links]	
		for each_url in page_links_n:
			if each_url in links_downloaded:
				print(each_url + 'is duplicated')
				time.sleep(1)
				continue
			else:	
				time.sleep(1)
				for attempt in range(0,3):
					try:
						ob = urlopen(each_url)
					except URLError:
						print('will try one more time')
					except HTTPError:
						print('this site is not bilingual, will try one more time')
					else:
						break
				else:
					with open('error_urls_for_3_times.txt', 'a') as f:
						f.write(each_url)
					continue			
						
				soup = BeautifulSoup(ob, 'html.parser')
				header = soup.find('div',class_ = 'article-header')
				h1_tag = header.find_all('h1')		
				head = [i.text for i in h1_tag]
				print(head) # a list of cn and en title #
				
				p_tag = soup.find_all('div', class_ = 'article-paragraph')
				en_cn = [i.text for i in p_tag]
				en = en_cn[::2]
				cn = en_cn[1::2]
				para = [en, cn]
				csv_format = [head]
				for i in range(0,len(en)):
					pair = [a[i] for a in para]
					csv_format.append(pair)
				with open('bi_' + self.channel + '.csv', 'a') as f:
					writer = csv.writer(f)
					writer.writerows(csv_format)
				
	
	
	

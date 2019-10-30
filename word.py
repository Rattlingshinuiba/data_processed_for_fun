from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import re
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, %(levelname)s, %(message)s')
logging.debug('The start of the program')
class PAGE:
	def pagelinks_for_word(self, page):
		base_url = 'https://cn.nytimes.com/culture/'
		res = urlopen(base_url + str(page))
		soup = BeautifulSoup(res, 'html.parser')
		h4_tags = soup.find_all('h4',string=re.compile('每日'))
		urls = []
		for h4_tag in h4_tags:
			h3_tag = h4_tag.next_sibling.next_sibling
			logging.debug('每日一词 == ' + h4_tag.text)
			a_tag = h3_tag.a
			ref = a_tag.get('href')
			url = 'https://cn.nytimes.com' + ref
			logging.debug('url： ' + url)
			urls.append(url)
		return urls	
	def parse_it(self, links):
		
		for each_link in links:
			res = urlopen(each_link)
			soup = BeautifulSoup(res, 'html.parser')
			p = soup.find_all('div', class_ = 'article-body-item col-lg-5')
			with open('每日一word.txt', 'a') as f:
				for i in p:
					f.write(i.text)
					logging.debug(i.text)

crawler = PAGE()

urls = crawler.pagelinks_for_word(1)
crawler.parse_it(urls)

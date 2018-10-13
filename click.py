from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = r"/home/wow/Desktop/selenium_test/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chrome_path)  # Optional argument, if not specified will search path.
driver.get("https://ted2srt.org/")

elem = driver.find_elements_by_xpath("//a[@class='Link']")

links = []
for i in elem:
	print(i.get_attribute('href'))
	links.append(i.get_attribute('href'))
for link in links:
	driver.get(link)
	each_elem = driver.find_element_by_link_text('TXT')
	each_elem.click()

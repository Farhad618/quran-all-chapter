# from bs4 import BeautifulSoup
# import requests
# with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
# req = requests.get(url)
# page = req.content

# soup = BeautifulSoup(page, 'html.parser')

# print(soup)


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


for j in range(1, 114):
	service = Service(executable_path="./chromedriver")
	browser = webdriver.Chrome(service=service)
	
	main_txt = ""

	url = "https://al-quran.info/#"+str(j)
	 
	browser.get(url)
	browser.implicitly_wait(20)
	# print(browser.title)
	article = browser.find_element(By.XPATH, '//*[@id="content-container"]/article')
	sections = article.find_elements(By.TAG_NAME, 'section')
	for s in sections:
	    main_txt += s.find_element(By.XPATH, 'div[2]/div[2]').get_attribute("innerText") + "\n"
	# print(elements.get_attribute("innerText"))
	# for e in elements:
	#     print(e)
	browser.quit()

	# print(main_txt)

	f = open("./contents/"+str(j)+".txt", "w")
	f.write(main_txt)
	f.close()

	print(str(j)+" completed...")
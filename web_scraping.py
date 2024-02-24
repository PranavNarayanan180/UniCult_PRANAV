from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pprint
import time
import llama

web=webdriver.Chrome()
web.get("https://www.linkedin.com/search/results/all/?heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAACasooBI0aD9v5Up_7b2JX1KnkN4EvG_8Y&keywords=Kunal%20Shah&origin=ENTITY_SEARCH_HOME_HISTORY&sid=%40(4")
time.sleep(2)
key=web.find_element(By.XPATH,'/html/body/div[1]/main/div/p/a')
key.click()
print("OPENING LINKEDIN...\nSIGN IN...")
time.sleep(2)

userid="<USERID>"
password="<PASSWORD>"

# //*[@id="email-or-phone"]
id=web.find_element(By.XPATH,'//*[@id="username"]')
id.send_keys(userid)

# //*[@id="password"]
id=web.find_element(By.XPATH,'//*[@id="password"]')
id.send_keys(password)

# //*[@id="join-form-submit"]
key=web.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
key.click()

time.sleep(5)
print("SIGN IN DONE...")
src = web.page_source
print("SCRAPING DATA...")
# Now using beautiful soup
soup = BeautifulSoup(src, 'html.parser')

sample1 = soup.find_all("p", {'class': 'relative'})

sample1_list = []

for name in sample1:
	sample1_list.append(name.text.strip())

sample_1=[a for a in sample1_list[0].split() if a not in ["...see","more"," "]]
sample_1=" ".join(sample_1)
sample_2=[a for a in sample1_list[0].split() if a not in ["...see","more"," "]]
sample_2=" ".join(sample_2)
sample_3=[a for a in sample1_list[0].split() if a not in ["...see","more"," "]]
sample_3=" ".join(sample_3)
print("SCRAPING DONE...")

llama.title_module(sample_1,sample_2,sample_3)


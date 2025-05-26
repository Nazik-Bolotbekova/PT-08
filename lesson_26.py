# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://cinematica.kg/movies")
# # print(driver.title)
# # elements = driver.find_elements(By.TAG_NAME, 'a' )
# # elements = driver.find_elements(By.CLASS_NAME, 'movie-dummy')
# time.sleep(5)
# elements = driver.find_elements(By.XPATH, "//a[@class='movie-dummy']")
#
# for element in elements:
#     source = element.get_attribute('href')
#     title = element.find_element(By.XPATH, ".//div[@class='movie-title']").text
#     image = element.find_element(By.XPATH, ".//img").get_attribute('src')
#
#     print(title)
#     print(image)
#     print(source)
#
#
# driver.quit()

import requests
from bs4 import BeautifulSoup



# for i in range(1,3):
#     url = f"https://www.kivano.kg/elektronika{i}"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'lxml')
#
# item = soup.find('div', class_ = "product-index product-index oh")


url = "https://www.kivano.kg/elektronika"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

products = soup.find_all('div', class_ ="product-index product-index oh")

for product in products:
    title = product.find_all('')
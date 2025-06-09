import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://store.steampowered.com/search/?term=')
print(driver.title)
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(15)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(15)

games = driver.find_elements(By.CLASS_NAME,'search_result_row')

for game in games:
    title = game.find_element(By.CLASS_NAME,'title').text
    img = game.find_element(By.XPATH, ".//img").get_attribute('src')
    prices = game.find_elements(By.CLASS_NAME,"discount_prices")
    if prices:
        real_price = prices[0].text
    else:
        real_price = 'No discount'
    print(title)
    print(img)
    print(real_price)

driver.quit()
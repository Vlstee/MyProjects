import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_options("detach", True)
g = Service("C:\\Users\\Влад\\PycharmProjects\\pythonProject5\\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=g)
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
Square = driver.find_element(By.XPATH,"//input[@id='id2']")
action.click_and_hold(Square).move_by_offset(-210,50).release().perform()


time.sleep(5)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.fsb.or.kr/mobbusmagequar_0100.act")
elem = driver.find_element(By.ID,"BANK_NAME")
elem.send_keys("바로")
elem.send_keys(Keys.RETURN)
driver.find_element(By.ID,"busiSearch").click()

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
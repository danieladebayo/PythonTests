from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = "C:\Selenium\Browser\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to_frame("packageListFrame") #1st frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to_default_content()
driver.switch_to_frame("packageFrame")#2nd frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)


driver.switch_to_default_content()
time.sleep(3)

driver.switch_to_frame("classFrame") #3rd frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
driver.quit()



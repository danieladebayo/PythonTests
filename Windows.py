from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = "C:\Selenium\Browser\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_link_text("click").click()
print(driver.current_window_handle) #CDwindow-8E63FF8D1A3E71358769FC064689A285 parent window
handles = (driver.window_handles) #returns all the handle values of open windows

for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)
    if driver.title =="Frames & windows":
        driver.close() #will close only parent window

#driver.quit()

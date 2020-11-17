from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = "C:\Selenium\Browser\chromedriver.exe")
driver.get("file:///C:/SeleniumPractice/sample.html")

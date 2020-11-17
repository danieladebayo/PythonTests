from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="C:\Selenium\Browser\chromedriver.exe")

# driver.set_page_load_timeout(10)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Dan")
driver.find_element(By.NAME, 'RESULT_TextField-2').send_keys("DMAN")
driver.find_element_by_id("RESULT_TextField-3").send_keys("123456789")

status = driver.find_element(By.NAME, 'RESULT_TextField-2').is_displayed()
print(status)

drp = Select(driver.find_element_by_id("RESULT_RadioButton-9"))

# drp.select_by_visible_text("Morning")

# drp.select_by_index(2)

drp.select_by_value("Radio-2")

print(len(drp.options))

all_options = drp.options

for option in all_options:
    print(option.text)
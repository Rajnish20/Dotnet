from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

application_no = input("Enter Application No: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://portal.uspto.gov/pair/PublicPair")

try:
	search = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "number_id"))
	)
except:
	driver.quit()


search.send_keys(application_no)
search.send_keys(Keys.RETURN)


print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[1]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[1]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[1]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[1]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[2]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[2]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[2]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[2]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[3]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[3]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[3]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[3]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[4]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[4]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[4]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[4]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[5]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[5]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[5]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[5]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[6]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[6]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[6]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[6]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[7]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[7]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[7]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[7]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[8]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[8]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[8]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[8]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[9]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[9]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[9]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[9]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[10]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[10]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[10]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[10]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[11]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[11]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[11]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[11]/td[4]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[12]/td[1]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[12]/td[2]").text)
print("")
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[12]/td[3]").text)
print(driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[12]/td[4]").text)


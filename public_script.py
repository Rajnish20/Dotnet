from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyodbc

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


APPLICATION_NO = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[1]/td[2]").text
print(APPLICATION_NO)

CORRESPONDEC_NUMBER = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[1]/td[4]").text
print("")

FILING_DATE = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[2]/td[2]").text
#print("")

STATUS = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[2]/td[4]").text
#print("")

APPLICATION_TYPE = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[3]/td[2]").text
#print("")


STATUS_DATE = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[3]/td[4]").text
print("")

EXAMINER_NAME = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[4]/td[2]").text
print("")

LOCATION = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[4]/td[4]").text
#print("")

GROUP_ART_UNIT = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[5]/td[2]").text
#print("")

LOCATION_DATE = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[5]/td[4]").text
#print("")

CONFIRMATION_NO = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[6]/td[2]").text
#print("")

EARLIEST_PUBLICATION_NO = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[6]/td[4]").text
#print("")

ATTORNEY_DOCKET_NO = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[7]/td[2]").text
#print("")

EARLIEST_PUBLICATION_DATE = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[7]/td[4]").text
#print("")

CLASS_SUBCLASS = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[8]/td[2]").text
#print("")

PATENT_NUMBER = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[8]/td[4]").text
#print("")

ISSUE_DATE = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[9]/td[4]").text
#print("")

FIRST_NAMED_APPLICANT = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[10]/td[2]").text
#print("")

IRN = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[10]/td[4]").text
#print("")

ENTITY_STATUS = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[11]/td[2]").text
#print("")

IRPD = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[11]/td[4]").text
#print("")

AIA = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div[2]/table/tbody/tr[12]/td[2]").text


conn = pyodbc.connect('DRIVER={SQL SERVER};'
	                  'SERVER=DESKTOP-38KI29F;'
	                  'Database=sqlpractice;'
	                  'TRUSTED CONNECTION=yes;')

cursor = conn.cursor()
cmd = ''' INSERT INTO PUBLICPAIRUSPTO VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
cursor.execute(cmd,APPLICATION_NO,CORRESPONDEC_NUMBER,FILING_DATE,STATUS,APPLICATION_TYPE,STATUS_DATE,EXAMINER_NAME,LOCATION,GROUP_ART_UNIT,LOCATION_DATE,CONFIRMATION_NO,EARLIEST_PUBLICATION_NO,ATTORNEY_DOCKET_NO,EARLIEST_PUBLICATION_DATE,CLASS_SUBCLASS,PATENT_NUMBER,ISSUE_DATE,FIRST_NAMED_APPLICANT,IRN,ENTITY_STATUS,IRPD,AIA)
conn.commit()
print("record inserted")

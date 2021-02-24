from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyodbc
import json
import traceback

def json_to_db(json_string):
    """This Function will push json data to Database"""
    conn = pyodbc.connect('DRIVER={SQL SERVER};'
	                  'SERVER=DESKTOP-38KI29F;'
	                  'Database=sqlpractice;'
	                  'TRUSTED CONNECTION=yes;')
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('EXEC prcJsonInsertData @json = ?', json_string)  # Passing Json Data to DataBase through Stored Procedure(prcJsonInserData)
       
        conn.close()
        
        print('     ************** Json inserted Successful **************\n')
        return True
    else:
        print('Error : %s' % 'Data Not Inserted Due to pyodbc Exception')
        logging.error('Data Not Inserted Due to pyodbc Exception')
        return None

def JsonStringSerialize(dataDictionary):
    """This Function Will Convert Formal Parameter(dataDictionary) to json_string and Write in .json File"""
    try:
        jsonData = json.dumps(dataDictionary, indent=4)  # serialazing dataDictionary
        
        with open('ApplicationData.json', 'w') as f_Out:
            
            f_Out.write(jsonData)  # writing in .json file 
            
            f_Out.close()  # closing .json File
            return jsonData
    except json.encoder.JSONEncoder:
        print('Cannot Serializable')
        
    except:
        print('Serialization Failed')
        


def ScrapData(application_no):
    """This Function will scrap data from public pair USPTO"""
    try:
        
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://portal.uspto.gov/pair/PublicPair")
        try:
        	search = WebDriverWait(driver,10).until(
        		EC.presence_of_element_located((By.ID,"number_id"))
        	)
        except:
            driver.quit()   
        
        search.send_keys(application_no)
        search.send_keys(Keys.RETURN)
        Data = [td.get_attribute("textContent").split("\n")[0] 
                           for td in driver.find_elements_by_xpath('//td[@class="wpsTableNrmRow"]')]
   
        return {
                'ApplicationNumber': Data[0], 'CorrespondenceAddressCustomerNumber': Data[1],
                'FilingOr371_c_Date': Data[2], 'Status': Data[3], 'ApplicationType': Data[4],
                'StatusDate': Data[5], 'ExaminerName': Data[6], 'Location': Data[7],
                'GroupArtUnit': Data[8], 'LocationDate': Data[9],
                'ConfirmationNumber': Data[10], 'EarliestPublicationNo': Data[11],
                'AttorneyDocketNumber': Data[12], 'EarliestPublicationDate': Data[13],
                'ClassSubclass': Data[14], 'PatentNumber': Data[15],
                'FirstNamedInventor': Data[16], 'IssueDateOfPatent': Data[17],
                'FirstNamedApplicant': Data[18], 'InternationalRegistrationNumberHague': Data[19],
                'EntityStatus': Data[20], 'InternationalRegistrationPublicationDate': Data[21],
                'AiaFirstInventorToFile': Data[22]}
        
    except:
        traceback.print_exc()
    finally:
        driver.quit()



if __name__ == '__main__':
	application_no = input("Enter Application No")
	json_to_db(JsonStringSerialize(ScrapData(application_no)))

"""
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
cmd = ''' INSERT INTO PUBLICPAIRUSPTO_1 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
cursor.execute(cmd,APPLICATION_NO,CORRESPONDEC_NUMBER,FILING_DATE,STATUS,APPLICATION_TYPE,STATUS_DATE,EXAMINER_NAME,LOCATION,GROUP_ART_UNIT,LOCATION_DATE,CONFIRMATION_NO,EARLIEST_PUBLICATION_NO,ATTORNEY_DOCKET_NO,EARLIEST_PUBLICATION_DATE,CLASS_SUBCLASS,PATENT_NUMBER,ISSUE_DATE,FIRST_NAMED_APPLICANT,IRN,ENTITY_STATUS,IRPD,AIA)
conn.commit()
print("record inserted")
"""



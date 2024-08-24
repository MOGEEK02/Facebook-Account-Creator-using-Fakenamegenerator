
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time



option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.fakenamegenerator.com/")
driver.switch_to.new_window('tab')
driver.get('http://facebook.com/')
def details():
      
      driver.switch_to.window(driver.window_handles[0])
      generatebtn = driver.find_element(By.ID,'genbtn')
      generatebtn.click()
      
      fullname = driver.find_element(By.CLASS_NAME,"address").find_element(By.TAG_NAME,"h3").text
      fullname.split()
      global firstname
      firstname=fullname.split()[0]
      global lastname
      lastname=fullname.split()[-1]
      global email
      email = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd')
      email = email.text
      email=email.split()[0]
      global passsword
      passsword = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[11]/dd').text
      
      fulldate = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[6]/dd')
      fulldate = fulldate.text
      global mounth
      mounth=fulldate.split()[0]
      mounth= mounth[:3]
      global year
      year=fulldate.split()[-1]
      year=year[:4]
      global day
      day=fulldate.split()[-2]
      day=day.replace(",","")
      global gendre
      gendre=driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[1]/div/div[1]/img').get_attribute('alt')
def signup():
     #switch to facebook tab 
     driver.switch_to.window(driver.window_handles[1]) 
     wait=WebDriverWait(driver,20)
#//*[@id="u_0_0_mN"]
#//a[@data-testid='open-registration-form-button']
#//input[@name="firstname"]     
     btn=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-testid='open-registration-form-button']")))
     btn.click() 
     
     print (gendre)
     time.sleep(3)
     driver.find_element(By.NAME,"firstname").send_keys(firstname)
     driver.find_element(By.NAME,"lastname").send_keys(lastname)
     driver.find_element(By.NAME,"reg_email__").send_keys(email)
     time.sleep(1)
     try:
          driver.find_element(By.NAME,"reg_email_confirmation__").send_keys(email)
     except:
          pass

     
     driver.find_element(By.ID,"password_step_input").send_keys(passsword)
     monthh=Select(driver.find_element(By.NAME,"birthday_month"))
     monthh.select_by_visible_text(mounth)
     dayy=Select(driver.find_element(By.NAME,"birthday_day"))
     dayy.select_by_visible_text(day)
     yearr=Select(driver.find_element(By.NAME,"birthday_year"))
     yearr.select_by_visible_text(year)
     
     if gendre == "Male" :
         driver.find_element(By.XPATH,"//label[text()='Male']").click() 
     else:
          driver.find_element(By.XPATH,"//label[text()='Female']").click() 

        
                                                      
                                                  
details()
signup()

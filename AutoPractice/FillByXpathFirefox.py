import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

class FillByXPath():

    def test(self):

        baseUrl = "http://automationpractice.com/index.php"
        registryEntryPoint = baseUrl + "?controller=authentication&back=my-account"
        accountCreationPage = baseUrl + "?controller=authentication&back=my-account#account-creation"
        currentdir = os.getcwd()
        screenshot_dir = currentdir + "/screenshots/"

        # Grab the test data from a CSV and put it into Panda Dataframes (Note that Amount of Data is Determined by CSV)
        base_file_name = "/firefox_datasheet.csv"
        csv_path = os.getcwd() + base_file_name
        my_csv = pd.read_csv(csv_path)
        username_df = my_csv.username
        firstname_df = my_csv.First_Name
        lastname_df = my_csv.Last_Name
        phone_df = my_csv.Phone
        address1_df = my_csv.Address1
        address2_df = my_csv.Address2
        email_df = my_csv.Email
        city_df = my_csv.City
        state_df = my_csv.State
        country_df = my_csv.Country
        zipcode_df = my_csv.Zipcode
        password_df = my_csv.password
        advertising_df = my_csv.advertising

        #  Step through the dataframes to load individual data elements in the UI with Selenium
        for profile_row in range(1, 10):
            index = profile_row - 1
            username_load = list(username_df[index:profile_row])
            firstname_load = list(firstname_df[index:profile_row])
            lastname_load = list(lastname_df[index:profile_row])
            phone_load = list(phone_df[index:profile_row])
            email_load = list(email_df[index:profile_row])
            address1_load = list(address1_df[index:profile_row])
            address2_load = list(address2_df[index:profile_row])
            city_load = list(city_df[index:profile_row])
            zipcode_load = list(zipcode_df[index:profile_row])
            state_load = list(state_df[index:profile_row])
            country_load = list(country_df[index:profile_row])
            password_load = list(password_df[index:profile_row])
            confirmpassword_load = list(password_df[index:profile_row])
            advertising_load = list(advertising_df[index:profile_row])

            driver = webdriver.Firefox()
            driver.get(registryEntryPoint)

            # Now Enter Email Address to begin User Registration at Registration Entry Point on Home Page
            # First Wait until Selenium finds the Email field using xpath using implicit wait command
            # This takes care of any page loading issues because of javascript execution delays

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='email']")))
            email_xpath = driver.find_element_by_xpath("//input[@name='email_create']")
            if email_xpath is not None:
                print("We found email field on Register page using  XPATH")
                email_xpath.send_keys(email_load)
                email_check = driver.find_element_by_xpath("//input[@name='email']").get_attribute('value')
                print ("email text field checked and has entered value  = " + str(email_check))

            #Find the Submit button and click it
            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='SubmitCreate']")))
            elementByXpath = driver.find_element_by_xpath("//button[@name='SubmitCreate']")
            if elementByXpath is not None:
                print("We found the submit button on the Registration Page using XPATH")
                submit_registration_xpath = driver.find_element_by_xpath("//button[@name='SubmitCreate']")
                submit_registration_xpath.click()

            print("Taking a screenshot after entering email for new account...")
            screenshot_path = screenshot_dir + "Enter_Email_For_New_Account_" + str(username_load) + ".png"
            driver.save_screenshot(screenshot_path)
            #driver.close()

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='customer_firstname']")))

            cfirstname_xpath = driver.find_element_by_xpath("//input[@id='customer_firstname']")
            if cfirstname_xpath is not None:
                print("We found the firstname field on registration page using XPATH")
                print('firstname_load = ' + str(firstname_load))
                cfirstname_xpath.send_keys(firstname_load)
                cfirstname_check = driver.find_element_by_xpath("//input[@id='customer_firstname']").get_attribute('value')
                print ("firstname text field checked and has entered value = " + str(cfirstname_check))


            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='firstname']")))

            clastname_xpath = driver.find_element_by_xpath("//input[@name='customer_lastname']")
            if clastname_xpath is not None:
                print("We found an Last Name field on registration page using  XPATH")
                clastname_xpath.send_keys(lastname_load)
                clastname_check = driver.find_element_by_xpath("//input[@name='customer_lastname']").get_attribute('value')
                print ("lastname text field checked and has entered value  = " + str(clastname_check))


            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='passwd']")))

            password_xpath = driver.find_element_by_xpath("//input[@name='passwd']")
            if password_xpath is not None:
                print("We found an password field on registration page using  XPATH")
                password_xpath.send_keys(password_load)
                password_check = driver.find_element_by_xpath("//input[@name='passwd']").get_attribute('value')
                print("password text field checked and has entered value  = " + str(password_check))


            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='address1']")))

            address1_xpath = driver.find_element_by_xpath("//input[@name='address1']")
            if address1_xpath is not None:
                print("We found an address1 field on registration page using  XPATH")
                address1_xpath.send_keys(address1_load)
                address1_check = driver.find_element_by_xpath("//input[@name='address1']").get_attribute('value')
                print ("address1 text field checked and has entered value  = " + str(address1_check))


            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='address2']")))

            address2_xpath = driver.find_element_by_xpath("//input[@name='address2']")
            if address2_xpath is not None:
                print("We found an address2 field on Registration page using  XPATH")
                address2_xpath.send_keys(address2_load)
                address2_check = driver.find_element_by_xpath("//input[@name='address2']").get_attribute('value')
                print ("address2 text field checked and has entered value  = " + str(address2_check))

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='city']")))

            city_xpath = driver.find_element_by_xpath("//input[@name='city']")
            if city_xpath is not None:
                print("We found an city field on Registration page using  XPATH")
                city_xpath.send_keys(city_load)
                city_check = driver.find_element_by_xpath("//input[@name='city']").get_attribute('value')
                print ("city text field checked and has entered value  = " + str(city_check))


            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//select[@name='id_state']")))

            state_xpath = driver.find_element_by_xpath("//select[@name='id_state']")
            if state_xpath is not None:
                print("We found an state field on Registration page using  XPATH")
                state_xpath.send_keys(state_load)
                state_check = driver.find_element_by_xpath("//select[@name='id_state']").get_attribute('value')
                print ("state text field checked and has entered value  = " + str(state_check))

                countrycode = driver.find_element_by_xpath("//select[@name='id_country']").get_attribute('value')
                print ("countrycode pulldown field checked and has entered value = " + str(countrycode))
                country_check = driver.find_element_by_xpath("//option[@value='" + str(countrycode) + "']").get_attribute('text')
                print ("country pulldown field checked and has entered value = " + str(country_check))

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='city']")))
            

            zipcode_xpath = driver.find_element_by_xpath("//input[@name='postcode']")
            if zipcode_xpath is not None:
                print("We found an postalCode field on Registration page using  XPATH")
                zipcode_load = ", ".join(str(e) for e in zipcode_load) #last minute clean up of zipcode parsing issue
                print('zipcode_load = ' + str(zipcode_load))
                zipcode_xpath.send_keys(str(zipcode_load))
                zipcode_check = driver.find_element_by_xpath("//input[@name='postcode']").get_attribute('value')
                print ("postalcode text field checked and has entered value  = " + str(zipcode_check))

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//select[@name='id_country']")))
            

            country_xpath = driver.find_element_by_xpath("//select[@name='id_country']")
            if country_xpath is not None:
                print("We found the country option in pulldown on Register page and entered United States")
                country_xpath.send_keys(country_load)
                countrycode = driver.find_element_by_xpath("//select[@name='id_country']").get_attribute('value')
                print ("countrycode pulldown field checked and has entered value = " + str(countrycode))
                country_check = driver.find_element_by_xpath("//option[@value='" + str(countrycode) + "']").get_attribute('text')
                print ("country pulldown field checked and has entered value = " + str(country_check))

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='phone']")))

            phone_xpath = driver.find_element_by_xpath("//input[@name='phone']")
            if phone_xpath is not None:
                print("We found a phone field on registration page using  XPATH")
                driver.find_element_by_xpath("//input[@name='phone']").clear()
                phone_xpath.send_keys(phone_load)
                phone_check = driver.find_element_by_xpath("//input[@name='phone']").get_attribute('value')
                print ("phone text field checked and has entered value  = " + str(phone_check))


            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='phone_mobile']")))

            phone_xpath = driver.find_element_by_xpath("//input[@name='phone_mobile']")
            if phone_xpath is not None:
                print("We found a mobile phone field on registration page using  XPATH")
                driver.find_element_by_xpath("//input[@name='phone_mobile']").clear()
                phone_xpath.send_keys(phone_load)
                phone_check = driver.find_element_by_xpath("//input[@name='phone_mobile']").get_attribute('value')
                print ("mobile phone text field checked and has entered value  = " + str(phone_check))

            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//input[@name='alias']")))

            phone_xpath = driver.find_element_by_xpath("//input[@name='alias']")
            if phone_xpath is not None:
                print("We found the Address Alias field on registration page using  XPATH")
                driver.find_element_by_xpath("//input[@name='alias']").clear()
                phone_xpath.send_keys(email_load)
                phone_check = driver.find_element_by_xpath("//input[@name='alias']").get_attribute('value')
                print ("Address alias text field checked and has entered value  = " + str(phone_check))

            driver.execute_script("window.scrollTo(0, 400)")
            screenshot_path = screenshot_dir + "Top_Filled_Registration_for_" + str(username_load) + ".png"
            driver.save_screenshot(screenshot_path)
            driver.execute_script("window.scrollTo(0, 700)")
            screenshot_path = screenshot_dir + "Mid_Filled_Registration_for_" + str(username_load) + ".png"
            driver.save_screenshot(screenshot_path)
            driver.execute_script("window.scrollTo(0, 1000)")
            screenshot_path = screenshot_dir + "Bottom_Filled_Registration_for_" + str(username_load) + ".png"
            driver.save_screenshot(screenshot_path)
            wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, \
                   "//button[@name='submitAccount']")))

            elementByXpath = driver.find_element_by_xpath("//button[@name='submitAccount']")
            if elementByXpath is not None:
                print("We found the submit button on the Registration Page using XPATH")
                submit_registration_xpath = driver.find_element_by_xpath("//button[@name='submitAccount']")
                submit_registration_xpath.click()

            print("Taking a screenshot of Registration Confirmation Page After Submit Account Button pressed...")
            screenshot_path = screenshot_dir + "Registry_Comfirmation_Page_" + str(username_load) + ".png"
            driver.save_screenshot(screenshot_path)

            driver.close()

ff = FillByXPath()
ff.test()
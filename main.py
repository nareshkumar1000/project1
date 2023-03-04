from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from html_locators import naresh_locators
from html_locators import naresh_Data


class naresh:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(naresh_Data().url)
    
    def invalid_login(self):
        sleep(7)
        self.driver.find_element(by=By.NAME, value=naresh_locators().username_inputbox).send_keys(naresh_Data().username)
        self.driver.find_element(by=By.NAME, value=naresh_locators().password_inputbox).send_keys(naresh_Data().invalid_passord)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().loginbutton).click()


    def login(self):
        sleep(7)
        self.driver.find_element(by=By.NAME, value=naresh_locators().username_inputbox).send_keys(naresh_Data().username)
        self.driver.find_element(by=By.NAME, value=naresh_locators().password_inputbox).send_keys(naresh_Data().password)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().loginbutton).click()

    def add_employee(self):
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Pimbutton_locator).click()
        sleep(7)
        self.driver.find_element(by=By.LINK_TEXT, value=naresh_locators().Add_employee).click()
        sleep(7)
        self.driver.find_element(by=By.NAME, value=naresh_locators().First_name).send_keys(naresh_Data().First_name)
        self.driver.find_element(by=By.NAME, value=naresh_locators().Middle_name).send_keys(naresh_Data().Middle_name)
        self.driver.find_element(by=By.NAME, value=naresh_locators().Last_name).send_keys(naresh_Data().Last_name)
        self.driver.find_element(by=By.XPATH, value=naresh_locators.Click_save).click()

    def Edit_employee(self):
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Pimbutton_locator).click()
        sleep(7)
        self.driver.find_element(by=By.LINK_TEXT, value=naresh_locators().Click_Employee_list).click()
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Edit_employee_details).click()
        sleep(7)
        self.driver.find_element(by=By.NAME, value=naresh_locators().Edit_fristname).send_keys(naresh_Data().Edit_frist_name)
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Edit_click_save_button).click()
        

    def delete_employee(self):
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Pimbutton_locator).click()
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Delete_employee).click()
        sleep(7)
        self.driver.find_element(by=By.XPATH, value=naresh_locators().Delete_yes).click()
        while(True):
            pass
          
      
naresh().invalid_login()
naresh().login()
naresh().add_employee()
naresh().Edit_employee()
naresh().delete_employee()

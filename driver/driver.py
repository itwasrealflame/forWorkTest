from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def page_open(self,url):
        self.driver.get(url)

    def element_find(self,value):
        return self.driver.find_element(By.XPATH, value)

    def send_text(self,value,text):
        self.driver.find_element(By.XPATH, value).send_keys(text)

    def click_button(self,value):
        self.driver.find_element(By.XPATH, value).click()



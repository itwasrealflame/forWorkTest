from confing.confing import json_read


xpath_lst = ["//input[@placeholder='Логин']", "//input[@placeholder='Пароль']"]

class Authorization:
    def __init__(self,driver):
        self.driver = driver

    def get_url(self):
        url = json_read().get('urlPageSecond')
        self.driver.page_open(url)

    def password_login_input(self,element):
        self.driver.send_text(xpath_lst[1], element)
        self.driver.send_text(xpath_lst[0], json_read().get('email'))


    def login_click(self):
        self.driver.click_button("//button[@class='login-form__submit']")




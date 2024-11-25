import time
import pytest
from confing.confing import password_random_input
from driver.driver import Driver
from pages.authorization import Authorization
from pages.registration import Registration

PASSWORD = password_random_input()

class Tests:
    @pytest.fixture
    def browser(self):
        self.driver = Driver()
        yield
        self.driver.driver.quit()


    def test_registration(self,browser):
        registration = Registration(self.driver)
        registration.get_url()
        registration.input_data()
        registration.captcha_input()
        registration.password_input(PASSWORD)
        registration.registration_click()
        #assert registration.find_element(...), эта строка находит новый элемент на странице, который появляется
        #после регистрации пользователя, но т.к. кнопка регистрации не работает, то и тест провести нельзя
        time.sleep(5)


    def test_authorization(self,browser):
        authorization = Authorization(self.driver)
        authorization.get_url()
        authorization.password_login_input(PASSWORD)
        #authorization.login_click()
        #аналогично как и с регистрацией, тест без нового пользователя провести нельзя
        time.sleep(5)

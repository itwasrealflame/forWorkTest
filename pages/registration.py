from PIL import Image
import pytesseract
from confing.confing import json_read, extraxt_values




xpath_lst = ["//input[@placeholder='Имя*']", "//input[@placeholder='Фамилия*']", "//input[@placeholder='Отчество']", "//input[@placeholder='Телефон*']", "//input[@placeholder='Email*']", "//input[@placeholder='Пароль']","//input[@placeholder='Подтверждение пароля']"]



class Registration:
    def __init__(self, driver):
        self.driver = driver


    def get_url(self):
        url = json_read().get('urlPageFirst')
        self.driver.page_open(url)


    def input_data(self):
        data = extraxt_values(json_read())
        for i in range(len(data)):
            self.driver.send_text(xpath_lst[i], data[i])


    def registration_click(self):
        self.driver.click_button("//button[@disabled='disabled']")


    def captcha_input(self):
        captcha = self.driver.element_find("//img[contains(@src, 'captcha.php?captcha_code=')]")
        captcha.screenshot('captcha.png')
        captcha_text = pytesseract.image_to_string(Image.open('captcha.png'), lang='eng')
        captcha_text = captcha_text.strip()
        self.driver.send_text("//input[@placeholder='Captcha']", captcha_text)
        #способ прочтения капчи некорректный, ниже написан код с платным API, где капча читается корректно
        #self.driver.send_text(captcha_input_xpath, captcha_text)
        #api_key = os.getenv('APIKEY_2CAPTCHA', '8523bf0514458e8134e0c8557acdb1a8')
        #solver = TwoCaptcha(api_key)
        #result = solver.normal('captcha.png')
        #print(result)

    def password_input(self,element):
        self.driver.send_text(xpath_lst[5], element)
        self.driver.send_text(xpath_lst[6], element)




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException


CHROME_PATH="C:/Development/chromedriver.exe"
MY_USERNAME="YOUR USERNAME"
MY_PASSWORD="YOUR PASSWORD"

class InstaFollower():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=CHROME_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        cookies_accept=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        sleep(2)
        cookies_accept.click()
        sleep(2)
        username=self.driver.find_element_by_name("username")
        username.send_keys(MY_USERNAME)
        password=self.driver.find_element_by_name("password")
        password.send_keys(MY_PASSWORD)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        sleep(3)
        self.driver.get("https://www.instagram.com/python.learning/")
        sleep(2)
        followers=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)
        modal = self.driver.find_element_by_css_selector('.isgrP')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight",modal)
            sleep(2)


    def follow(self):
       buttons=self.driver.find_elements_by_css_selector("li button")
       for button in buttons:
          try:
           button.click()
           sleep(2)
          except ElementClickInterceptedException:
              cancel_button=self.driver .find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
              cancel_button.click()


instagram=InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()

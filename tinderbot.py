#A python bot project using selenium and chromedriver
#Written By Ninad Sunil Jangle at 12:17 am 17/08/2020
#tutorial referred Aaron Jack: https://www.youtube.com/watch?v=lvFAuUcowT4


from selenium import webdriver
from time import sleep


class tinder_bot_swiper():
    def __init__(self):
        #self is basically self= tinder_bot_swiper() in principle

        self.driver = webdriver.Chrome()

    def login(self):
        #opens chrome of same version and goes on tinder.com
        self.driver.get('https://tinder.com')
        sleep(2)
        #saving the xpath of the login button into loginbtn
        #to find the value, go to login btn on website
        #inspect the button and right click on it: copy->copyxpath
        loginbtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        loginbtn.click()
        sleep(2)
        google_login_btn=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div/div/button')
        google_login_btn.click()
        

        #An issue that arises with a popup window is: driver is still on base window
        #Solution use driver.window_handles to get IDs for both windows
        #use driver.switch_to_window to switch to the popup window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        #entering our email IDs into the textbox, same process
        emailtext=self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        emailtext.send_keys('YYYY')
        #clicking the next button
        next_btn=self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_btn.click()
        sleep(2)

        #entering the password
        passtext = bot.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        passtext.send_keys('XXXX')

        #clicking next button on password window
        next_btn_pass=self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        next_btn_pass.click()

#creating the bot for the interface to run 
bot = tinder_bot_swiper()
bot.login()




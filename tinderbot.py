#A python bot project using selenium and chromedriver
#Written By Ninad Sunil Jangle at 12:17 am 17/08/2020
#tutorial referred Aaron Jack: https://www.youtube.com/watch?v=lvFAuUcowT4


from selenium import webdriver
from time import sleep
from credentials import emailID,password
#from selenium.webdriver.support.ui import WebDriverWait       
#from selenium.webdriver.common.by import By       
#from selenium.webdriver.support import expected_conditions as EC
import random



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
        emailtext.send_keys(emailID)
        #clicking the next button
        next_btn=self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_btn.click()
        sleep(2)

        #entering the password
        passtext = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        passtext.send_keys(password)

        #clicking next button on password window
        next_btn_pass=self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        next_btn_pass.click()
        sleep(5)

        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)
        location_allow=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location_allow.click()
        sleep(1)
        notif_enable=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notif_enable.click()
        accept_btn=bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_btn.click()

    def like(self):
        sleep(random.randint(0,4))
        like_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()
    def dislike(self):
        sleep(random.randint(0,3))
        dislike_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        dislike_btn.click()
    def close_tinder_add_HS(self):
        popup_close=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_close.click()
    def close_match(self):
        match_close= self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_close.click()


#creating the bot for the interface to run 
bot = tinder_bot_swiper()
bot.login()



a = [0,1,2,3,4,5,6,7,8,9]
for i in a:
    n = random.randint(0,9)
    try:
        if((n*2)>4):
            bot.like()
        else:
            bot.dislike()
    except Exception: 
        sleep(2)
        try:
            bot.close_tinder_add_HS()
        except Exception:
            bot.close_match()
        
        









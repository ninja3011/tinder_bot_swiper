#A python bot project using selenium and chromedriver
#Written By Ninad Sunil Jangle at 12:17 am 17/08/2020
#tutorial referred Aaron Jack: https://www.youtube.com/watch?v=lvFAuUcowT4


from selenium import webdriver
from time import sleep
from credentials import emailID,password
import random
import sys

i=1
args=sys.argv
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
        if(len(self.driver.window_handles)>1):
            self.driver.switch_to_window(self.driver.window_handles[1])
        
        #entering our email IDs into the textbox, same process
        emailtext=self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        try:
            emailtext.send_keys(sys.argv[4])
            print('try email')
        except Exception:
            emailtext.send_keys(emailID)
        #clicking the next button
        next_btn=self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_btn.click()
        sleep(2)

        #entering the password
        passtext = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        try:
            passtext.send_keys(sys.argv[5])
            print('try pass')
        except Exception:
            passtext.send_keys(password)

        #clicking next button on password window
        next_btn_pass=self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        next_btn_pass.click()
        sleep(3)

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
        sleep(random.randint(0,2))
        like_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()
    def dislike(self):
        sleep(random.randint(0,2))
        dislike_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        dislike_btn.click()
    def close_tinder_add_HS(self):
        popup_close=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_close.click()
    def close_match(self):
        match_close= self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_close.click()
    def messaging(self):
        for i in list(range(2,(int(args[2])+1))):
            sleep(1)
            messages_tab=  self.driver.find_element_by_xpath('//*[@id="messages-tab"]')
            messages_tab.click()
            chatlink = self.driver.find_element_by_xpath('//*[@id="matchListWithMessages"]/div[2]/a[%d]'%int(i))
            chatlink.click()
            textarea=self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            try:
                textarea.send_keys(sys.argv[3])
                print('try msg')
            except Exception:
                textarea.send_keys('How are you?')
            sendmsg=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            sendmsg.click()








#creating the bot for the interface to run 
bot = tinder_bot_swiper()
bot.login()
sleep(3)



for i in list(range(1, int(args[1]))):
    n = random.randint(0,4)

    try:
        if((n*2)>4):
            bot.like()
        else:
            bot.dislike()
    except Exception: 
        sleep(1)
        try:
            bot.close_tinder_add_HS()
        except Exception:
            bot.close_match()

flag=0
while(flag==0):
    try:
        bot.messaging()
        flag=1
    except Exception:
        try:
            bot.close_tinder_add_HS()
        except Exception:
            bot.close_match()    


        









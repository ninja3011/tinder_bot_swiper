#A python bot project using selenium and chromedriver
#Written By Ninad Sunil Jangle at 12:17 am 17/08/2020
#tutorial referred Aaron Jack: https://www.youtube.com/watch?v=lvFAuUcowT4
#importing the gui lib
#named it tk so can use tk.funcname()
import tkinter as tk
#importing the font lib to give font-type
from tkinter import font



root = tk.Tk()

#parameters of the gui screen
HEIGHT = 600
WIDTH = 800


class tgm():
    def __init__(a,b):
    	emailID=a
    	assword=b
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    background_image = tk.PhotoImage(file='party.png') #getting the bg image
    background_label = tk.Label(root, image=background_image) #adding it to the label
    background_label.place(relwidth=1, relheight=1) #adding it to the gui
    canvas.pack() #adding it to the gui

	frame = tk.Frame(root, bd=5) #creating a container for entry and submit button
	frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.1, anchor='n') #anchor gives fix dir
	entry1 = tk.Entry(frame, font=('Courier',12)) #adding a Textbox to frame container
	entry1.place(relwidth=0.65, relheight=0.5) #adding to gui
	entry2 = tk.Entry(frame, font=('Courier',12)) #adding a Textbox to frame container
	entry2.place(relx=0,rely=0.6,relwidth=0.65, relheight=0.4) #adding to gui
	button = tk.Button(frame, text="submit", font=('Courier',12), command=lambda: tgm(entry1.get(),entry2.get())) #adding to frame container and calling get_weather()
	button.place(relx=0.7, relheight=1, relwidth=0.3) #adding gui
	print(emailID,password)

'''
button = tk.Button(frame, text="Get Weather", font=('Courier',12), command=lambda: get_credentials_epass(entry1.get(),entry.get())) #adding to frame container and calling get_weather()
button.place(relx=0.7, relheight=1, relwidth=0.3) #adding gui 
'''
#print(emailID, password)
tgm(null,null)
root.mainloop()








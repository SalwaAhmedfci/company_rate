from easygui import *
from easygui import msgbox, multenterbox
from app import *
from tkinter import *
from tabulate import tabulate


msgbox("Welcome to Company Info App",image='profile.png')
name = enterbox("Enter the company name:", "Info")
msgbox("Welcome to  " + name)
tableinfo=[]
tableinfo.append(["profits : " ,get_profit(name)])
tableinfo.append(["marketvalue :  " ,get_marketvalue(name)])
tableinfo.append(["revenue :  " ,get_reveune(name)])
tableinfo.append(["price : " ,get_price(name)])
msgbox(tabulate(tableinfo),"Company Info ")
array = get_company_rating(name)
count = 0
rates = array[0]
names = array[1]
r = []
table = []
while count < rates.__len__():
    table.append([names[count],rates[count]])
    count=count+1
msgbox(tabulate(table),"Company Rating ")
ind =get_company_indusrty(name)


msgbox(get_company_indusrty(name),"industry and SIC ")






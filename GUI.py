from easygui import *
from easygui import msgbox, multenterbox
from app import *
from tkinter import *
from tabulate import tabulate


msgbox("Welcome to Company Info App",image='profile.png')
name = enterbox("Enter the company name:", "Info")
msgbox("Welcome to  " + name)

msgbox("profits : "+get_profit(name),"profit")
msgbox("marketvalue :"+get_marketvalue(name),"marketvalue")
msgbox("revenue :" +get_reveune(name),"revenue")
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
count = 1
table1 = []
if(ind[0].__len__()==2):
    while count < ind[0].__len__():
        table1.append([ind[0][count][0][count], ind[0][0][0][0]])
        table1.append([ind[0][0][0][count], ind[0][count][0][0]])
        msgbox(tabulate(table1), "industry and SIC ")
        count = count + 1
# elif((ind[0].__len__()==3)):
#
#     msgbox(tabulate(table1), "industry and SIC ")
# elif((ind[0].__len__()==4)):
#     count = 1
#     while count < ind[0].__len__():
#         table1.append([ind[0][1][0][0], ind[0][0][0][0]])
#         table1.append([ind[0][0][0][1], ind[0][1][0][0]])
#         table1.append([ind[0][1][0][2], ind[0][2][0][0]])
#         table1.append([ind[0][1][0][3], ind[0][3][0][0]])
#         count =count+1
#     msgbox(tabulate(table1), "industry and SIC ")
# elif((ind[0].__len__()==5)):
#
#     msgbox(tabulate(table1), "industry and SIC ")
else:

    msgbox(get_company_indusrty(name),"industry and SIC ")

# industry



msgbox("price : " +get_price(name),"price")

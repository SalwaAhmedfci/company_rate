# bigRating strong margRtSm h1

# !/usr/bin/env python
from bs4 import BeautifulSoup
from userAgent import randomUserAgents
from flask import Flask, render_template, request
from database_setup import *
import requests
from database_setup import *

#
#
#
app = Flask(__name__)
def soup(url, headers):
    session = requests.Session()
    req = session.get(url, headers=headers )
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs


# eiHdrModule module snug

@app.route('/', methods=['POST', 'GET'])
def my_form_post():

    if request.method == 'GET':

        return render_template("welcome.html")
    elif request.method == 'POST':
        companyname = request.form['company_name']
        head = randomUserAgents()
    #scraping companyrating
        page1_link = "https://www.glassdoor.com/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=false&clickSource" \
                "=searchBtn&typedKeyword='{0}'&sc.keyword='{1}'&locT=&locId=&jobType=".format(
        companyname, companyname)
        bs = soup(page1_link, head)

        mylist = []
        matched_companies = []

        main_div = bs.findAll('div', {'class': "eiHdrModule module snug"})
        for rate in main_div:
            if rate.find('span', {'class': "bigRating strong margRtSm h2"}) is not None:
                mylist.append(rate.find('span', {'class': "bigRating strong margRtSm h2"}).get_text())
            else:
                mylist.append("Not rated yet")
            matched_companies.append(rate.find('a', {'class': "tightAll h2"}))
        # loop of printing

        mylist_names = []
        mylist_rates = []
        count = 0
        while count < matched_companies.__len__():
            mylist_names.append(matched_companies[count].get_text())
            mylist_rates.append(mylist[count])
            count = count + 1
        #scraping price
        page2_link ="https://finance.yahoo.com/quote/{0}?p={1}&.tsrc=fin-srch".format(companyname,companyname)
        head1 = randomUserAgents()
        bs2 = soup(page2_link, head1)
        #cell = bs2.select("span[data-reactid ='39']")
        price = bs2.find('span', {'class': "Trsdu(0.3s)"}).get_text()
       

        #showing results
        return render_template("show.html", companyname=companyname, mylist_rates=mylist_rates, mylist_names=mylist_names, price =price)


# print (rate)

if __name__ == '__main__':

     app.run(debug=True)

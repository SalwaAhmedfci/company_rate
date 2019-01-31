# bigRating strong margRtSm h1

# !/usr/bin/env python
from bs4 import BeautifulSoup
from userAgent import randomUserAgents
from flask import Flask, render_template, request
from database_setup import *
import requests
from database_setup import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from excrating import *
from sqlalchemy.orm import load_only
import sqlite3
import re
#
#
app = Flask(__name__)

# def extractnum(input):
#     numbers = re.sub(r'[a-z]+', '', input, re.I)
#     return numbers


def get_company_name():
    companyname = request.form['company_name']
    return companyname

def soup(url, headers):
    session = requests.Session()
    req = session.get(url, headers=headers )
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs

def get_company_info():
    companyinfo = []
    try:
        companyname = get_company_name()
        print(companyname)
            # pick up the target company
        company = session.query(Company).filter_by(
        name=companyname).one()
            # fuzzy match here
        query = company.industry
        allindustries = []
            # load only indusrty column from look_up
        industries = session.query(look_up).all()
        for ind in industries:
            allindustries.append(ind.industry)
        #do fuzzuy matching
        industry = process.extract(query, allindustries)
        #print(industry)
        matched_industry = []
        for i in industry:
            matched_industry.append(i[0])
        #print(matched_industry)
            # pick up the matched company indusrty and SIC
            #print(matched_industry)

        conn = sqlite3.connect('CompainesData.db')
        c = conn.cursor()
        result = []
        for i in matched_industry:
            res=c.execute(
                "select industry,SIC from look_up where industry like ?",('%'+i+'%',))

            result.append(res.fetchall())
        #print(result)
        conn.commit()
        conn.close()
        companyinfo.append(company.name)
        companyinfo.append(company.profits)
        companyinfo.append(company.revenue)
        companyinfo.append(company.marketValue)
        companyinfo.append(result)

        return companyinfo
    except:

        companyinfo.append(get_company_name())
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")

        return companyinfo



@app.route('/', methods=['POST', 'GET'])
def my_form_post():

    if request.method == 'GET':

        return render_template("welcome.html")
    elif request.method == 'POST':
        companyname = get_company_name()
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
        #data - test = "PREV_CLOSE-value"
        close =[]

        p =bs2.find("td", {"data-test": "PREV_CLOSE-value"})
        #exract numbers from text
        #price = p.replace("Previous Close", "")
        #print(p.get_text())
        info=get_company_info()
        #showing results
        return render_template("show.html", companyname=companyname, mylist_rates=mylist_rates, mylist_names=mylist_names, price =p.get_text(), info =info)


# print (rate)

if __name__ == '__main__':

     app.run(debug=True)

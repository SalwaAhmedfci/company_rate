# bigRating strong margRtSm h1

# !/usr/bin/env python
from bs4 import BeautifulSoup
from database_setup import *
from database_setup import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from excrating import *
import sqlite3
import re



def scrape_company_info(name):
    companyname = name
    head = randomUserAgents()
    # scraping companyrating
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
    # scraping price
    page2_link = "https://finance.yahoo.com/quote/{0}?p={1}&.tsrc=fin-srch".format(companyname, companyname)
    head1 = randomUserAgents()
    bs2 = soup(page2_link, head1)
    # cell = bs2.select("span[data-reactid ='39']")
    # data - test = "PREV_CLOSE-value"
    close = []

    p = bs2.find("td", {"data-test": "PREV_CLOSE-value"})
    # exract numbers from text
    # price = p.replace("Previous Close", "")
    # print(p.get_text())
    info = get_company_info(companyname)
    # showing results
    price = p.get_text()
    array = []
    array.append(mylist_rates)
    array.append(mylist_names)
    array.append(price)
    array.append(info)
    return array


def get_company_name(name):
    companyname = name
    return scrape_company_info(companyname)

def soup(url, headers):
    session = requests.Session()
    req = session.get(url, headers=headers )
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs

def get_company_info(name):
    companyinfo = []
    enhancement_ratio = 50
    companyname = name
    try:
        # pick up the target company
        company = session.query(Company).filter_by(
        name=companyname).one()
        # fuzzy match here
        query = company.industry
        allindustries = []
                # load only indusrty column from look_up
        industries = session.query(look_up).all()
        for ind in industries:

            if fuzz.ratio(query,ind.industry) > enhancement_ratio :

                allindustries.append(ind.industry)
            else:
                continue
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

        companyinfo.append(companyname)
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")
        companyinfo.append("not covered yet")

        return companyinfo





name = input('enter the company name:')
print(get_company_name(name))





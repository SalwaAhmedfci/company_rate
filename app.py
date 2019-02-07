# !/usr/bin/env python3
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from excrating import *
import sqlite3
import requests
from userAgent import *


def get_price(name):
    """Scrap the price and returns it"""
    page2_link = "https://finance.yahoo.com/quote/{0}?p={1}&.tsrc=fin-srch".format(name, name)
    head1 = randomUserAgents()
    bs2 = soup(page2_link, head1)
    try:
        p = bs2.find('tr', attrs={'class': 'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($c-fuji-grey-c) H(36px)'})
        price = p.find('td', attrs={'class': 'Ta(end) Fw(600) Lh(14px)'})
        text1 = price.find('span', attrs={'class': 'Trsdu(0.3s)'}).get_text()
        return text1
    except:

        p = bs2.find('td', attrs={'class': 'data-col2 Ta(end) Pstart(20px) Pend(15px)'}).get_text()

        return p


def get_marketvalue(name):
    """returns marketvalue of the company from the database"""
    try:
        company = session.query(Company).filter_by(
            name=name).one()
        return company.marketValue

    except:

        return "not covered yet"


def get_reveune(name):
    """returns revenue of the company from the database"""
    try:
        company = session.query(Company).filter_by(
            name=name).one()
        return company.revenue
    except:
        return "not covered yet"


def get_profit(name):
    """returns the profit of the company from the database"""
    try:
        company = session.query(Company).filter_by(
            name=name).one()
        return company.profits
    except:
        return "not covered yet"


def get_company_rating(name):
    """scrap the rating from glassdoor and returns it"""
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

    array = []
    array.append(mylist_rates)
    array.append(mylist_names)

    return array


def get_company_name(name):
    companyname = name
    return companyname


def soup(url, headers):
    """creating the session , parsing the html tree to beautifulsoup"""
    session = requests.Session()
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs


def get_company_indusrty(name):
    """do fuzzy logic to get the best matched keywords to use it in searching for industries from the database"""
    enhancement_ratio = 50  # you can control the precentage of matching from here by increasing the number you are restricting the matches
    companyname = name
    try:
        # pick up the target company
        company = session.query(Company).filter_by(
            name=companyname).one()
        # fuzzy match here
        query = company.industry
        allindustries = []
        # load only industry column from look_up
        industries = session.query(look_up).all()
        for ind in industries:

            if fuzz.ratio(query, ind.industry) > enhancement_ratio:

                allindustries.append(ind.industry)
            else:
                continue
        # do fuzzuy matching

        industry = process.extract(query, allindustries)
        # print(industry)
        matched_industry = []
        for i in industry:
            matched_industry.append(i[0])
        # print(matched_industry)
        # pick up the matched company indusrty and SIC
        conn = sqlite3.connect('CompainesData.db')
        c = conn.cursor()
        result = []
        for i in matched_industry:
            res = c.execute(
                "select industry,SIC from look_up where industry like ?", ('%' + i + '%',))

            result.append(res.fetchall())

        conn.commit()
        conn.close()

        return result
    except:

        return "not covered yet"

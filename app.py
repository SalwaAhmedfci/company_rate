# bigRating strong margRtSm h1

# !/usr/bin/env python
from bs4 import BeautifulSoup
from userAgent import randomUserAgents
from flask import Flask, render_template, request
import urllib.request  as urllib2
# App config.
import requests


app = Flask(__name__)
#
#
#
#
#


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

        page_link = "https://www.nytimes.com/"

        bs = soup(page_link, head)

        mylist = []
        matched_companies = []

        #main_div = bs.find('div', {'class': "masthead-mini-nav"})

        matched_companies = bs.findAll('a', {'class': "css-1wjnrbv"})

        # loop of printing

        mylist_names = []
        mylist_rates = []
        count = 0
        while count < matched_companies.__len__():
            mylist_names.append(matched_companies[count].get_text())
            print(mylist_names[count])
            count = count + 1


        return render_template("show.html", companyname=companyname, mylist_names=mylist_names)


# print (rate)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(port=5000, host='localhost')

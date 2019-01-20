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
APPLICATION_NAME = "CompanyApp"



import re # for regular expression matching operations
# import requests # for sending HTTP requests
# from urllib.parse import urlsplit # for breaking URLs down into component parts
# from collections import deque # is a list-like container with fast appends and pops on either end
# from bs4 import BeautifulSoup # for pulling data out of HTML files of websites



# target_webpage = input("Enter a target url to have the emails scraped: ")
# unscraped_url = deque(target_webpage)
# scraped_url = set()
# scraped_email = set()


#===================================================================
#Regex Examples
#===================================================================

email = input("Type email: ")

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

isValid(email)
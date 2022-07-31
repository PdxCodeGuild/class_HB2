#===================================================================
#Install Libraries
#===================================================================

import re
import requests
from bs4 import BeautifulSoup
import pprint
from requests import get



# https://www.redhat.com/en/contact #email page to scrape

#===================================================================
#Collect HTML w/ Beautiful Soup
#===================================================================
target_webpage = input("Type a target url to scrape the emails from that page: ")
# # print(target_webpage)

target_html = requests.get(target_webpage).text
# print(target_html)

target_html_parsed = BeautifulSoup(target_html, "lxml")
a_tags = target_html_parsed.find_all(['a'])
# print(target_html_parsed)
# print(a_tags)

# print(type(a_tags))


# pprint.pprint((target_html_parsed.prettify()))
# print(target_html_parsed.title.text)
# print(target_html_parsed.get_text())


#===================================================================
#
#===================================================================

regex_pattern = '\S+@\S+'


for tag in a_tags:
    a_tag_text = tag.get_text()
    # print(type(a_tag_text))
    # print("a_tag_text: ", a_tag_text)
    email = re.findall(regex_pattern, a_tag_text)
    print(email)



#===================================================================
#Regex Examples
#===================================================================

# email = input("Type email: ")

# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


# def isValid(email):
#     if re.fullmatch(regex, email):
#         print("Valid email")
#     else:
#         print("Invalid email")

# isValid(email)

# (separator=" ")
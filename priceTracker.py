import requests
# used to grab website data
from bs4 import BeautifulSoup
# used to prettify the data
import os
# used to create custom notifications using Script Editor
import time
# used to implement a timer

URL = "https://www.flipkart.com/apple-iphone-x-space-gray-64-gb/p/itmexrgv6hctyrav"
# replace the URL variable with the url of your choice

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"}
# replace the value part of the key User-Agent with your user agent
# to check your user google "my user agent" and copy the result

def notify(title, text): # create the custom notification
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def check():
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find("span", class_="_35KyD6").get_text() 			# find the title container using Inspect Element
	price = soup.find("div",class_="_1vC4OE _3qQ9m1").get_text()	# find the price container using Inspect Element
	converted_price = int(price[1:3])*1000+int(price[4:])			# change this for prices other than 5 digits
	if(converted_price<70000):										# condition for alert
		msg = title+" - ₹"+str(converted_price)
		notify("Price Dropped!", msg)

while(True):
	check()
	time.sleep(60*60*24) # change the parameter of time.sleep as per your requirements (in seconds)
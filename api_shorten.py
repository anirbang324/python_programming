from pyshorteners import Shortener

#ACCESS_TOKEN = ""

long_url = input()
url_shortener = Shortener(domain="bit.ly", api_key="https://bit.ly/37sFpNT") #as we are using bitly so the domain name is bit.ly
print("Short URL is : ", format(url_shortener.bitly.short(long_url)))

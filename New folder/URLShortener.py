from pyshorteners import Shortener
ACCESS_TOKEN = "d9eac69f900d2ad5e76e31785156b1477b65056e"
long_url = input()
url_shortener = Shortener(domain="bit.ly", api_key=ACCESS_TOKEN) #as we are using bitly so the domain name is bit.ly
print("Short URL is : ", format(url_shortener.bitly.short(long_url)))

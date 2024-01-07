import requests
response=requests.get("http://api.open-notify.org/")
#print(response.json())
print(response.status_code)

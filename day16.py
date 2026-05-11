import requests
response=requests.get("https://www.pittsburgh.com/")
print(response.status_code)
print(response.text)
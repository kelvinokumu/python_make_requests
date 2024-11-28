import requests


url = "https://restcountries.com/v3.1/all"

response = requests.get(url)


all = response.text

# print(response.status_code)
print(all)
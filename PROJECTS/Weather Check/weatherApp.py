import win32com.client
import requests
import json

city=input("Enter Which city You WAnt Weather: \n")

url=f"https://api.weatherapi.com/v1/current.json?key=7d297e538b944b93a3095227240305&q={city}"

r=requests.get(url)
print(r.text)

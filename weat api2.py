import requests, json

apiKey="53391df2b87e740ed7fc4959583616d2"

baseURL= "http://api.openweathermap.org/data/2.5/weather?q="

cityname= input("Enter your city :")

completeURL=baseURL + cityname + "&appid="  + apiKey

response=requests.get(completeURL)

data=response.json()

print("Temperature :",data["main"]["temp"])
print("Humidity :",data["main"]["humidity"])
print("Pressure :",data["main"]["pressure"])



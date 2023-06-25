import requests
import win32com.client
import json
speaker = win32com.client.Dispatch("SAPI.Spvoice")
G ="Welcome to Weather app by Gurwinder singh"
speaker.speak(G)

city = input("Enter the name of the city")
url = f"https://api.weatherapi.com/v1/current.json?key=17c658af7bbc4d839e0103638231506&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
W = (wdic["current"]["temp_c"])
print(wdic["current"]["temp_c"])
H = (wdic["current"]["humidity"])
print(wdic["current"]["humidity"])
Ws = wdic['current']['wind_kph']
print(wdic['current']['wind_kph'])



T = (f"'temperature of {city} is {W} degrees',humidity is {H} and wind speed is {Ws} kph.")

speaker.speak(T)

























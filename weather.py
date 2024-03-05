import tkinter as tk
#import  requests 
import time
global requests 

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 274.15)
    min_temp = int(json_data['main']['temp_min'] - 274.15) #strona internetowa Postman http...> tam wszytko jest
    max_temp = int(json_data['main']['temp_max'] - 274.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.getime(json_data['sys']['sunrise'] - 21600 ))
    sunset = time.strftime("%I:%M:%S",time.getime(json_data['sys']['sunset'] - 21600 ))


    final_info = condition + "\n" + str(temp) + " *C"
    final_data = "\n" + "Max Tempz: " + str(max_temp) +"\n" + "Min TEmp: " +str(min_temp ) + "\n" + "Presure" + str(pressure) + "\n" + "Humidity: " + str(humidity) +"\n" + "Wind Speed: " +str(wind) +"\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
     
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(canvas,font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas,font = t)
label1.pack()
label2 = tk.Label(canvas,font = f)
label2.pack()

canvas.mainloop()


#Youtube https://www.youtube.com/watch?v=Sz0_2fp27Q0
#Strona internetowa 
#By city name 
#You can call by city name or city name state code and country code.Please note that searching by states
#available only for the USA locations 
### API call ###
#1. api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#2. api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}
#3. api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}  

#1.{
#      "cod":401,
#      "message":"Invalid API key,Please see http://openweathermap.org/faq#error401 for more info."
#  }
#1. W GET wpisujemy  api.openweathermap.org/data/2.5/weather?q={london}&appid=06c921750b9e82dBf5d1294e1586276f
#{
#    "coord":{
#        "lon": -0.13,
#        "lat": 51.51
#    },
#    "weather":[
#        {
#            "id": 801,
#            "main":"Clouds",
#            "description": 'few clouds',
#            "icon":"02n"
#        }
#    ]
#    "base":"stations",
#    "main":{
#        "temp": 284.52,
#        "feels_like": 280.32,
#        "temp_min": 284.26,
#        "temp_max": 285.15,
#        "presure": 1025,
#        "numinidy": 76
#    }
#    "visibility": 10000,
#    "wind":{
#        "speed":5.1,
#        "deg":240
#    },
#    "clouds":{
#        "all":20
#    },
#    "ot": 1605998215,
#    "sys":{
#        "type": 1,
#        "id":1414
#        "country":"GB"
#        "sunrise": 1605943761,
#        "sunset": 1605974638
#    },
#    "timezone": 0,
#    "id": 2643743,
#    "name": "London"
#    "cod": 200
#}


    
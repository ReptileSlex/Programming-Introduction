import requests
import time

with open("EventosSeguridad.txt", "r") as file:
    lineas = [linea.split() for linea in file]

dicc = ["Múnich", "Buenos Aires", "Manizales", "España", "México", "Monterrey", "Estados Unidos", "Bogotá",
        "California", "Los Ángeles", "Guadalajara", "Colombia", "Brasil", "New Brunswick", ]

for i in range(len(lineas)):
    req = requests.get(lineas[i][0])
    statusCode = req.status_code
    htmlText = req.text
    print("Buscando coincidencias en el link: ", i+1, "por favor espere...")
    for i in range(len(dicc)):
        time.sleep(2)
        if dicc[i] in htmlText:
            print("Ciudad ", dicc[i], " encontrada")
            api_key = "bf2b4d379231897f6184333a6fc3a408"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = dicc[i].lower()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)
            x = response.json()
            # print(response)
            # print(x)

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                city = x["name"]
                weather_description = z[0]["description"]
                file = open("clima.txt", "a")
                file.write("Ciudad: ")
                file.write(city + "\n")
                file.write("Temperatura: ")
                file.write("{0:.2f}".format(current_temperature - 273.15) + "°C" + "\n")
                file.write("Presión atmosférica: ")
                file.write(str(current_pressure) + " hPa \n")
                file.write("Humedad: ")
                file.write(str(current_humidity) + "% \n")
                file.write("Descripción: ")
                file.write(str(weather_description) + "\n")
                file.write("\n")
                file.close()
                time.sleep(2)
            else:
                print("Ciudad no encontrada en el sistema")
                time.sleep(2)
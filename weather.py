import requests
from tkinter import *

class Application(Frame):
    """ GUI-приложение, владеющее секретом долголетия. """
    def __init__(self, master):
        """ Инициализирует рамку. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text="Чтобы узнать погоду, введите название вашего города:")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=0, column=2, columnspan=2, sticky=W)

        self.submit_bttn = Button(self, text="Узнать Погоду", command=self.getweather)
        self.submit_bttn.grid(row=0, column=4, sticky=W)

        self.city_lbl = Label(self, text="")
        self.city_lbl.grid(row=1, column=0, columnspan=2, sticky=W)

        self.weather_lbl = Label(self, text="")
        self.weather_lbl.grid(row=2, column=0, columnspan=2, sticky=W)

        self.temp_lbl = Label(self, text="")
        self.temp_lbl.grid(row=3, column=0, columnspan=2, sticky=W)

        self.wind_lbl = Label(self, text="")
        self.wind_lbl.grid(row=4, column=0, columnspan=2, sticky=W)
    def getweather(self):
        url = "http://api.openweathermap.org/data/2.5/weather"
        city = self.pw_ent.get()
        parameters = {
            'q': city,
            'appid': "778d98cf94b6609bec655b872f24b907",
            'units':'metric',
            'lang' : 'ru'
        }
        res = requests.get(url,params=parameters)
        data = res.json()
        try:
            self.city_lbl.config(text = "Город: " + data["name"])

            self.weather_lbl.config(text = str(data["weather"][0]["description"]))

            self.temp_lbl.config(text = "Температура: " + str(data["main"]["temp"]) + "С")

            self.wind_lbl.config(text = "Скорость ветра: " + str(data["wind"]["speed"]) + " м/с")
        except KeyError:
            self.city_lbl.config(text = "Город с таким названием не найден!")

root = Tk()
root.title("Погода")
app = Application(root)

root.mainloop()
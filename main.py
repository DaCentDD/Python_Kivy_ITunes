from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
import json

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')


class MyApp(App):
    def got_json(self, req, result):  # JSON processing function
        dict_data, i = json.loads(result), 0
        for key in dict_data['results']:
            if i > 9:
                break
            globals()['a' + str(i)].text = key['trackName']
            i += 1

    def build(self):  # Main function, interface rendering
        bl, bl1, self.artist = BoxLayout(orientation='vertical',  spacing=2), BoxLayout(orientation='vertical', spacing=2), TextInput(size_hint=[1, 0.08])
        bl.add_widget(self.artist)
        bl.add_widget(Button(size_hint=[1, 0.08],
                             text="Get top 10 from ITunes",
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1]))
        bl.add_widget(bl1)
        for i in range(10):
            globals()['a' + str(i)] = Button()
            bl1.add_widget(globals()['a' + str(i)])
        return bl

    def btn_press(self, instance):  # Button click processing function, sending request
        art_rq = self.artist.text
        if ' ' in art_rq:
            art_rq = art_rq.replace(' ', '+')
        request = 'https://itunes.apple.com/search?term=' + art_rq
        req = UrlRequest(request, self.got_json)


if __name__ == "__main__":
    MyApp().run()
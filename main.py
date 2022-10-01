from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.controllers import WindowController
from kivymd.uix.screen import MDScreen
from selenium import webdriver


class Srapping():
    def srape():
        url = 'https://www.youtube.com/watch?v=lTypMlVBFM4'
        driver = webdriver.Chrome()
        driver.get(url)



class MyScreen(MDScreen, WindowController):
    def on_width(self, *args):
        print(self.get_window_width_resizing_direction())


class MainApp(MDApp):

    data = {
        'Search': 'magnify',
    }


    

    def build(self):
        url = 'https://www.youtube.com/watch?v=lTypMlVBFM4'
        driver = webdriver.Chrome()
        driver.get(url)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('project.kv')


MainApp().run()
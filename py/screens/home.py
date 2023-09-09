from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import requests

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.name = "Screen7"

    def checkAppNav(self, app):
        print(app.NAVIGATION)

    def on_enter(self):
        self.app = MDApp.get_running_app()

        # GET ALL USERS IN THE SYSTEM
        url = "http://127.0.0.1:8000/api/users/"
        token = self.app.ACCESS_TOKEN
        headers = {
            "Authorization": f"Token {token}"
        }

        #MAKE API CALL
        response = requests.get(url, headers=headers)
        #WAS API CALL SUCCESSFUL
        if response.status_code == 200:
            data = response.json()
            self.app.contacts = data

        #WAS API CALL UNSUCCESSFUL
        else:
            print(f"Failed to retrieve data. Status Code: {response.status_code}")
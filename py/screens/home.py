from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.name = "Screen7"
        self.dialog = None

    def checkAppNav(self, app):
        print(app.NAVIGATION)

    def on_enter(self):
        self.app = MDApp.get_running_app()
        # GET ALL USERS IN THE SYSTEM
        try:
            url = "https://atary.pythonanywhere.com/api/account/users/"
            token = self.app.ACCESS_TOKEN
            headers = {
                'Authorization': f'Bearer {token}'
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
        except requests.exceptions.ConnectionError:
            loginErrorMsg = "Sorry, something is wrong with the server. Please try again later"
            print(loginErrorMsg)
            tryAgainBtn = MDFlatButton(
                    text="Try Again", 
                    theme_text_color="Custom",
                    text_color=(36/255, 120/255, 109/255, 1),
                    )
            tryAgainBtn.bind(on_release=self.refresh_screen) 
            if not self.dialog:
                self.dialog = MDDialog(
                title= loginErrorMsg,
                buttons= [tryAgainBtn]
                )
            self.dialog.open()

    def refresh_screen(self, button):
        self.app.sm.current = "Screen5"
        self.dialog.dismiss()
        self.dialog = None

from kivy.uix.screenmanager import Screen, NoTransition
from kivy.animation import Animation
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
import re
import asyncio
import aiohttp


class LoginIn(Screen):
    def __init__(self, **kwargs):
        super(LoginIn, self).__init__(**kwargs)
        self.name  = "Screen5"
        self.BUTTON_ACTIVE = False
        self.dialog = None

    def activateButton(self, *args):
        logInButton = self.ids['log_in_button2']
        if self.BUTTON_ACTIVE:
            return
        else:
            logInButton.back_color = (36/255, 120/255, 109/255, 1)
            logInButton.color =  (1, 1, 1, 1)
            self.BUTTON_ACTIVE = True

    # HANDLING USER ACTIONS
    def handlePress(self, *args):
        logInButton = self.ids['log_in_button2']
        if self.BUTTON_ACTIVE:
            logInButton.color = (121/255, 124/255, 123/255, 1)
            logInButton.back_color = (243/255, 246/255, 246/255, 1)
        else:
            logInButton.color = (1, 1, 1, 1)
            logInButton.back_color = (36/255, 120/255, 109/255, 1)
        
    def handleRelease(self, *args):
        logInButton = self.ids['log_in_button2']
        if self.BUTTON_ACTIVE:
            logInButton.color = (1, 1, 1, 1)
            logInButton.back_color = (36/255, 120/255, 109/255, 1)
        else:
            logInButton.color = (121/255, 124/255, 123/255, 1)
            logInButton.back_color = (243/255, 246/255, 246/255, 1)

    # INPUT VALIDATIONS
    def check_pattern(self,pattern, s):
        """Checks if a string follows the specified pattern.

        Args:
            s: The string to check.

        Returns:
            True if the string follows the pattern, False otherwise.
        """

        if re.match(pattern, s):
            return True
        else:
            return False
        
    def validateUserID(self, *args):
        userID = self.ids['login_text_input1']
        error_msg = self.ids["invalid_userID_msg"]
        if userID.text != "":
            pattern = r"^[0-9]+$"
            if self.check_pattern(pattern=pattern, s=userID.text):
                userID.line_color = [205/255, 209/255, 208/255, 1]
                error_msg.opacity = 0
            else:
                userID.line_color = [255/255, 45/255, 27/255, 1]
                error_msg.opacity = 1
        else:
            userID.line_color = [205/255, 209/255, 208/255, 1]
            error_msg.opacity = 0

    def validatePassword(self, *args):
        password = self.ids['login_text_input2']
        error_msg = self.ids["invalid_password_msg"]
        if password.text != "":
            pattern = r"^.{6,}$"
            if self.check_pattern(pattern=pattern, s=password.text):
                password.line_color = [205/255, 209/255, 208/255, 1]
                error_msg.opacity = 0
            else:
                password.line_color = [255/255, 45/255, 27/255, 1]
                error_msg.opacity = 1
        else:
            password.line_color = [205/255, 209/255, 208/255, 1]
            error_msg.opacity = 0

    # HANDLE USER LOGIN
    def handleUserLogin(self, button, app=None):
        self.app = app
        user_id, password = self.extractUserInput()
        self.loginUser(user_id, password)

    def extractUserInput(self):
        userID = self.ids['login_text_input1'].text
        password = self.ids['login_text_input2'].text
        return userID, password
    
    def loginUser(self, user_id, password):
        asyncio.run(self._main_login_user(
            user_id = user_id,
            password = password
        ))
    
    async def _main_login_user(self, user_id, password):
        task1 = asyncio.create_task(
            self.loginUserAPICall(user_id, password)
        )
        result, response = await task1
        self.show_alert_dialog(result, response)

    async def loginUserAPICall(self, user_id, password):
        login_url = "http://127.0.0.1:8000/api/account/login/"
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                headers={'Accept': 'application/json'},
                url=login_url,
                data = {
                    "username": user_id,
                    "email": "",
                    "password": password,
                }
            )
            result = await response.json()
            raw_response = response
            return result, raw_response
        
    def show_alert_dialog(self, result, response):
        #print("result: ", result)
        #print("response: ", response)
        if response.status == 200:
            self.app.ACCESS_TOKEN = result['key']
            print(self.app.ACCESS_TOKEN)
            loginBtn = MDFlatButton(
                    text="CONTINUE", #TODO
                    theme_text_color="Custom",
                    text_color=(36/255, 120/255, 109/255, 1),
                    )
            loginBtn.bind(on_release=self.changeScreenToHomeScreen) 
            if not self.dialog:
                self.dialog = MDDialog(
                title= "Log In Successful",
                buttons= [loginBtn]
                )
            self.dialog.open()
        elif response.status == 400:
            loginErrorMsg = str(result['non_field_errors'][0])
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
        self.dialog.dismiss()
        
    def changeScreenToHomeScreen(self, button):
        self.manager.current = "Screen7"
        self.dialog.dismiss()



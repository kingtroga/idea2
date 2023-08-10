from kivy.uix.screenmanager import Screen, NoTransition
from kivy.animation import Animation
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.clock import Clock
import re
import asyncio
import aiohttp


class SignUp(Screen):
    def __init__(self, **kwargs):
        super(SignUp, self).__init__(**kwargs)
        self.name  = "Screen4"
        self.BUTTON_ACTIVE = False
        self.dialog = None


    def activateButton(self, *args):
        signUpButton = self.ids['signUpBtn2']
        if self.BUTTON_ACTIVE:
            return
        else:
            signUpButton.back_color = (36/255, 120/255, 109/255, 1)
            signUpButton.color =  (1, 1, 1, 1)
            self.BUTTON_ACTIVE = True


    # HANDLING USER ACTIONS
    def handlePress(self, *args):
        signUpButton = self.ids['signUpBtn2']
        if self.BUTTON_ACTIVE:
            signUpButton.color = (121/255, 124/255, 123/255, 1)
            signUpButton.back_color = (243/255, 246/255, 246/255, 1)
        else:
            signUpButton.color = (1, 1, 1, 1)
            signUpButton.back_color = (36/255, 120/255, 109/255, 1)
        
    def handleRelease(self, *args):
        signUpButton = self.ids['signUpBtn2']
        if self.BUTTON_ACTIVE:
            signUpButton.color = (1, 1, 1, 1)
            signUpButton.back_color = (36/255, 120/255, 109/255, 1)
        else:
            signUpButton.color = (121/255, 124/255, 123/255, 1)
            signUpButton.back_color = (243/255, 246/255, 246/255, 1)

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

    def validateFullName(self, *args):
        full_name = self.ids['full_name_textInput']
        error_msg = self.ids['invalid_full_name_msg']
        if full_name.text != "":
            pattern = r"^[a-zA-Z]+\s*[a-zA-Z]+$"
            if self.check_pattern(pattern=pattern, s=full_name.text):
                full_name.line_color = [205/255, 209/255, 208/255, 1]
                error_msg.opacity = 0
            else:
                full_name.line_color = [255/255, 45/255, 27/255, 1]
                error_msg.opacity = 1
        else:
            full_name.line_color = [205/255, 209/255, 208/255, 1]
            error_msg.opacity = 0

    def validateUserID(self, *args):
        userID = self.ids['user_id']
        error_msg = self.ids["invalid_user_id_msg"]
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
        password = self.ids['password']
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

    def validatePassword2(self, *args):
        password = self.ids['password']
        password2 = self.ids['password2']
        error_msg = self.ids['invalid_password2_msg']
        if password2.text != "":
            if password.text == password2.text:
                password2.line_color = [205/255, 209/255, 208/255, 1]
                error_msg.opacity = 0
            else:
                password2.line_color = [255/255, 45/255, 27/255, 1]
                error_msg.opacity = 1
        else:
            password2.line_color = [205/255, 209/255, 208/255, 1]
            error_msg.opacity = 0
   

    # HANDLE USER REGISTRATION
    def handleUserRegistration(self, *args):
        full_name, user_id, password, password2 = self.extractUserInput()
        self.registerUser(full_name, user_id, password, password2)

    def extractUserInput(self):
        full_name = self.ids['full_name_textInput'].text
        user_id = self.ids['user_id'].text
        password = self.ids['password'].text
        password2 = self.ids['password2'].text
        return full_name, user_id, password, password2
    
    def registerUser(self, full_name, user_id, password, password2):
        asyncio.run(self._main_register_user(
            full_name = full_name, 
            user_id = user_id, 
            password = password, 
            password2 = password2
        ))

    async def _main_register_user(self, full_name, user_id, password, password2):
        task1 = asyncio.create_task(self.registerUserAPICall(full_name, user_id, password, password2))
        response = await task1
        self.show_alert_dialog(response)

    async def registerUserAPICall(self, full_name, user_id, password, password2):
        registration_url = "http://127.0.0.1:8000/api/account/register/"
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                registration_url,
                data = {
                    'userID': user_id,
                    'fullName': full_name,
                    'password': password,
                    'password2': password2
                }
            )
            
            result = response
            return result
    
    def show_alert_dialog(self, response):
        #print(response.status)
        if response.status == 200 or response.status == 201:
            loginBtn = MDFlatButton(
                    text="Log In", #TODO
                    theme_text_color="Custom",
                    text_color=(36/255, 120/255, 109/255, 1),
                    )
            loginBtn.bind(on_release=self.changeScreenToLogInScreen) 
            if not self.dialog:
                self.dialog = MDDialog(
                title= "Registration Successful",
                buttons= [loginBtn]
                )
            self.dialog.open()
        else:
            tryAgainBtn = MDFlatButton(
                    text="Try Again", 
                    theme_text_color="Custom",
                    text_color=(36/255, 120/255, 109/255, 1),
                    )
            tryAgainBtn.bind(on_release=self.refresh_screen) 
            if not self.dialog:
                self.dialog = MDDialog(
                title= "Registration Unsuccessful, check for invalid inputs",
                buttons= [tryAgainBtn]
                )
            self.dialog.open()

        #self.dialog.close()

    def refresh_screen(self, button):
        self.dialog.dismiss()
        

    def changeScreenToLogInScreen(self, button):
        self.manager.current = "Screen5"
        self.dialog.dismiss()


            

        

    
        
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.clock import Clock
from py.widgets.chatitem import ChatItem
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.core.window import Window 
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
Builder.load_file('kv\widgets\messageitem.kv')
import websocket
import json
import threading
from kivymd.app import MDApp



class MessageItem(MDLabel):
    atext = StringProperty()
    inMessage = BooleanProperty(default=True)
    bcolor = ListProperty()
    rradius1 = NumericProperty()
    rradius2 = NumericProperty()

    def __init__(self, **kwargs):
        super(MessageItem,self).__init__(**kwargs)
        self.font_name = "fonts/Montserrat-Light.ttf"
        self.color = [1, 1, 1, 1]
        self.bcolor = get_color_from_hex("20A090")
        self.rradius1 = 10
        self.rradius2 = 0
        #RECIEVED MESSAGE
        if self.inMessage == False:
            self.bcolor = get_color_from_hex("F2F7FB")
            self.color = [0, 0, 0, 1]
            self.rradius1 = 0
            self.rradius2 = 10

    
    def caculate_width(self, widget):
        if len(widget.text) == 5:
            return dp(0.15)
        elif len(widget.text) == 1:
            return dp(0.08)
        elif len(widget.text) == 4:
            return dp(0.13)
        elif len(widget.text) <= 36:
            _ = len(widget.text)
            return dp(round((_/Window.width * 10), 1))
        else:
            return dp(0.6)
    
    def caculate_height(self, widget):
        if len(widget.text) <= 25:
            return dp(0.038)
        elif  47 <= len(widget.text) <= 55:
            return dp(0.053)
        else:
            return dp(round((len(widget.text)/(Window.height*2.5)), 1))

class MessageBox(TextInput):
    def __init__(self, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.counter = 1
        self.outmessage = []
        self.inmessage = []
        self.message = None
        self.startM = 0
        self.app = MDApp.get_running_app()
        self.max_characters = 35 # Set the maximum number of characters

    def handle_chatting(self):
        rm_thread = threading.Thread(target=self.remove_loading, daemon=True)
        rm_thread.start()

    def insert_text(self, substring, from_undo=False):
        # Check if adding the new text will exceed the character limit
        if len(self.text) + len(substring) > self.max_characters:
            # Calculate how many characters can be added to reach the limit
            substring = substring[:self.max_characters - len(self.text)]
        
        # Call the original insert_text method
        return super(MessageBox, self).insert_text(substring, from_undo)
    
    
        


    
    def printMessage(self):
        # CREATE THE MESSAGE
        self.msg = MessageItem(atext=self.text,inMessage=True, pos_hint={ "top":self.counter, "right": 0.98}, font_name="fonts/Montserrat-Light.ttf", )
        #SPACING
        self.counter = round((self.counter - 0.03),2)
        
        # SCROLL VIEW (add the message to the screen on user's side)
        self.parent.children[0].children[0].children[0].add_widget(self.msg)

        # send the message to everyone in the group
        self.app.wsapp.send(json.dumps({
            'type': 'chat_message',
            'message': str(self.text),
            'user_id': int(self.app.userID),
        }))
        
        # RESET THE MESSAGE BOX
        self.text = ""

        # FOR GOOD SPACING (Limit the input to 50 characters)
        if len(self.msg.text) >= 50:
            self.counter = round((self.counter - 0.016),2)

    def outMessage(self, dt=None):
        
        self.msg = MessageItem(atext=self.message,inMessage=False, pos_hint={ "top":self.counter, "left": 0}, font_name="fonts/Montserrat-Light.ttf", )

        self.counter = round((self.counter - 0.03),2)
        
        # SCROLL VIEW
        self.parent.children[0].children[0].children[0].add_widget(self.msg)
        

        # FOR GOOD SPACING (Limit the input to 50 characters)
        if len(self.msg.text) >= 50:
            self.counter = round((self.counter - 0.016),2)
    
    def outMessage2(self, dt=None):
        
        self.msg = MessageItem(atext=self.outmessage.pop(-1),inMessage=False, pos_hint={ "top":self.counter, "left": 0}, font_name="fonts/Montserrat-Light.ttf", )

        self.counter = round((self.counter - 0.03),2)
        
        # SCROLL VIEW
        self.parent.children[0].children[0].children[0].add_widget(self.msg)
        

        # FOR GOOD SPACING (Limit the input to 50 characters)
        if len(self.msg.text) >= 50:
            self.counter = round((self.counter - 0.016),2)

    def inMessage2(self, dt=None):
        
        self.msg = MessageItem(atext=self.inmessage.pop(-1),inMessage=True, pos_hint={ "top":self.counter, "right": 0.98}, font_name="fonts/Montserrat-Light.ttf", )

        self.counter = round((self.counter - 0.03),2)
        
        # SCROLL VIEW
        self.parent.children[0].children[0].children[0].add_widget(self.msg)
        

        # FOR GOOD SPACING (Limit the input to 50 characters)
        if len(self.msg.text) >= 50:
            self.counter = round((self.counter - 0.016),2)
    
    def remove_loading(self):
        self.app.wsapp = websocket.WebSocketApp(
            "ws://" +
            "127.0.0.1:8000" +
            "/ws/chat/" +
            self.getRoom() +
            "/" +
            str(self.app.userID) +
            "/", 
            on_message=self.on_message,
            on_open=self.on_open,
            on_close=self.on_close)
        self.app.wsapp.run_forever()

    def getRoom(self):
        room = ""
        contactID = int(self.app.contactUserID)
        userID = int(self.app.userID)
        maxID = max(contactID, userID)
        minID = min(contactID, userID)
        room = f"{minID}_{maxID}"
        return room

    def on_message(self,wsapp, message):
        print(json.loads(message))
        data = json.loads(message)
        if int(data['user_id']) == int(self.app.contactUserID):
            self.message = str(data['message'])
            Clock.schedule_once(self.outMessage, 0.2)



    def on_open(self, wsapp):
        pass

    def on_close(self, wsapp,close_status_code, close_msg):
        print(close_status_code, close_msg)


        




    

        
        
        
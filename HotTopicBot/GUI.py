import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel

from script import *




class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)

        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="Link: "))
        self.link = TextInput(multiline = False)
        self.inside.add_widget(self.link)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="Number: "))
        self.number = TextInput(multiline = False)
        self.inside.add_widget(self.number)

        self.inside.add_widget(Label(text="First Name: "))
        self.firstname = TextInput(multiline = False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline = False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Address: "))
        self.address = TextInput(multiline = False)
        self.inside.add_widget(self.address)

        self.inside.add_widget(Label(text="City: "))
        self.city = TextInput(multiline = False)
        self.inside.add_widget(self.city)

        self.inside.add_widget(Label(text="Postal Code: "))
        self.postalCode = TextInput(multiline = False)
        self.inside.add_widget(self.postalCode)

        self.inside.add_widget(Label(text="Card Name: "))
        self.cardName = TextInput(multiline = False)
        self.inside.add_widget(self.cardName)

        self.inside.add_widget(Label(text="Card Number: "))
        self.cardNumber = TextInput(multiline = False)
        self.inside.add_widget(self.cardNumber)

        self.inside.add_widget(Label(text="Expire #: "))
        self.expire = TextInput(multiline = False)
        self.inside.add_widget(self.expire)

        self.inside.add_widget(Label(text="CVN: "))
        self.CVN = TextInput(multiline = False)
        self.inside.add_widget(self.CVN)
        
        self.add_widget(self.inside)

        self.submit = Button(text="Run",font_size=50)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed (self, instance):

        addToCart(self.link.text)
        checkOut(self.email.text,self.number.text,self.firstname.text,self.lastname.text, self.address.text,self.city.text,self.postalCode.text)
        dropDown(self.cardName.text,self.cardNumber.text,self.expire.text,self.CVN.text)


      


    






class HotTopicBot(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    HotTopicBot().run()


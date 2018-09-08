from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
temp=""

from os import listdir
#kv_path = './kv/'
Builder.load_file("buttons.kv")


class AddButton(Button):
    pass


class SubtractButton(Button):
    pass

class MultiplyButton(Button):
	pass
class DivideButton(Button):
	pass

class two(Button):
	pass

class one(Button):
	pass
class zero(Button):
	pass
class three(Button):
	pass
class four(Button):
	pass
class five(Button):
	pass
class six(Button):
	pass
class seven(Button):
	pass
class eight(Button):
	pass
class nine(Button):
	pass
class left_brace(Button):
	pass
class right_brace(Button):
	pass
class EqualButton(Button):
	pass
class dot(Button):
	pass
class modulo(Button):
	pass
class exponent(Button):
	pass
class clr(Button):
	pass


class Container(GridLayout):
    display = ObjectProperty()
    def _init_(self,temp):
	self.temp=temp
	

    def add_one(self):
        self.temp = self.display.text
	self.temp=self.temp+"+"
        self.display.text = self.temp

    def subtract_one(self):
	self.temp = self.display.text
        self.temp = self.temp+"-"
        self.display.text = self.temp
    def multiply_one(self):
	self.temp = self.display.text
        self.temp = self.temp+"*"
        self.display.text = self.temp
    def divide_one(self):
	self.temp = self.display.text
        self.temp = self.temp+"/"
        self.display.text = self.temp
    def left_brace_one(self):
	self.temp = self.display.text
        self.temp = self.temp+"("
        self.display.text = self.temp
    def right_brace_one(self):
	self.temp = self.display.text
        self.temp = self.temp+")"
        self.display.text = self.temp

    def one_1(self):
	self.temp = self.display.text
	self.temp=self.temp+"1"
	self.display.text = self.temp
    def two_2(self):
	self.temp = self.display.text
	self.temp=self.temp+"2"
	self.display.text = self.temp
    def zero_0(self):
	self.temp = self.display.text
	self.temp=self.temp+"0"
	self.display.text = self.temp
    def three_3(self):
	self.temp = self.display.text
	self.temp=self.temp+"3"
	self.display.text = self.temp
    def four_4(self):
	self.temp = self.display.text
	self.temp=self.temp+"4"
	self.display.text = self.temp
    def five_5(self):
	self.temp = self.display.text
	self.temp=self.temp+"5"
	self.display.text = self.temp
    def six_6(self):
	self.temp = self.display.text
	self.temp=self.temp+"6"
	self.display.text = self.temp
    def seven_7(self):
	self.temp = self.display.text
	self.temp=self.temp+"7"
	self.display.text = self.temp
    def eight_8(self):
	self.temp = self.display.text
	self.temp=self.temp+"8"
	self.display.text = self.temp
    def nine_9(self):
	self.temp = self.display.text
	self.temp=self.temp+"9"
	self.display.text = self.temp
    def equal(self):
	self.temp=self.display.text
	#c=0
	#if '+' in self.temp:
	#	split_value=self.temp.split('+')
	#	self.display.text=str(int(split_value[0])+int(split_value[1]))
	#if '-' in self.temp:
	#	split_value=self.temp.split('-')
	#	self.display.text=str(int(split_value[0])-int(split_value[1]))
	#self.display.text=str(c)
	self.temp=eval(self.temp)
	self.display.text=str(self.temp) 
    def dot(self):
	self.temp = self.display.text
	self.temp=self.temp+"."
	self.display.text = self.temp
    def modulo(self):
	self.temp = self.display.text
	self.temp=self.temp+"%"
	self.display.text = self.temp
    def exponent(self):
	self.temp = self.display.text
	self.temp=self.temp+"**"
	self.display.text = self.temp
    def clr(self):
	self.temp = ""
	#self.temp=self.temp+"9"
	self.display.text = ""

class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()

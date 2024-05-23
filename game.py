from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen



class Screen1(Screen):
    def __init__(self, name="welcome"):
        super().__init__(name=name)

        self.instr = Label(text="Скоро буде!!!")
        self.btn = Button(text="Перейти до гри")

        layout = BoxLayout(orientation="vertical")

        layout.add_widget(self.instr)
        layout.add_widget(self.btn)

        self.add_widget(layout)

        self.btn.on_press = self.next
    def next(self):
        self.manager.current = "pers"



class Screen2(Screen):
    def __init__(self, name="pers"):
        super().__init__(name=name)

        self.name_text = Label(text="Введіть ім'я")
        self.age_text = Label(text="Введіть вік")

        self.cont = Button(text="Продовжити")

        name = TextInput(multiline=False)
        age = TextInput(multiline=False)


        layout1 = BoxLayout(orientation ="vertical")

        name_layout = BoxLayout()
        age_layout = BoxLayout()

        name_layout.add_widget(self.name_text)
        name_layout.add_widget(name)

        age_layout.add_widget(self.age_text)
        age_layout.add_widget(age)

        layout1.add_widget(name_layout)
        layout1.add_widget(age_layout)
        layout1.add_widget(self.cont)

        self.add_widget(layout1)

        self.cont.on_press = self.next
    def next(self):
        self.manager.current = "click"

class Screen3(Screen):
    def __init__(self, name="click"):
        super().__init__(name=name)

        self.balance = 0
        self.profit = 1

        self.money = Label(text=f"Ваш баланс: {self.balance}\nВаш прибуток: {self.profit}")



        self.click = Button(text="Клікай")
        self.menu = Button(text = "Меню")

        layout = BoxLayout(orientation = "vertical")

        layout.add_widget(self.money)
        layout.add_widget(self.click)
        layout.add_widget(self.menu)

        self.add_widget(layout)

        self.menu.on_press = self.next

        self.click.on_press = self.profit1

    def profit1(self):
        self.balance += self.profit
        self.money.text = f"Ваш баланс: {self.balance}\nВаш прибуток: {self.profit}"

    def next(self):
        self.manager.current = "menu"

class Screen4(Screen):
    def __init__(self, name="menu"):
        super().__init__(name=name)

        self.shop = Button(text = "Магазин")
        self.business = Button(text = "Бізнеси")
        self.shares = Button(text = "Акції")
        self.achievement = Button(text = "Досягнення")
        self.back = Button(text = "Перейти назад")

        layout = BoxLayout(orientation = "vertical")
        layout1 = BoxLayout()
        layout2 = BoxLayout()

        layout1.add_widget(self.shop)
        layout1.add_widget(self.business)

        layout2.add_widget(self.shares)
        layout2.add_widget(self.achievement)

        layout.add_widget(layout1)
        layout.add_widget(layout2)

        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1
        self.shop.on_press = self.shop1
        self.shares.on_press = self.shares1
        self.business.on_press = self.business1
        self.achievement.on_press = self.achievement1

    def shop1(self):
        self.manager.current = "shop"

    def shares1(self):
        self.manager.current = "shares"

    def business1(self):
        self.manager.current = "business"

    def achievement1(self):
        self.manager.current = "achievement"

    def back1(self):
        self.manager.current = "click"


class Shop(Screen):
    def __init__(self, name="shop"):
        super().__init__(name=name)

        self.products = [{"name": "Бустер1",
                    "price": 100,
                    "description": "Цей бустер збільшить ваш прибуток до 5"},

                    {"name": "Бустер2",
                     "price": 1000,
                     "description": "Цей бустер збільшить ваш прибуток до 10"},

                    {"name": "Бустер3",
                     "price": 2000,
                     "description": "Цей бустер збільшить ваш прибуток до 20"},

                    {"name": "Бустер4",
                     "price": 4000,
                     "description": "Цей бустер збільшить ваш прибуток до 50"}
                    ]

        product1 = Label(text = f"Назва: {self.products[0]['name']}\nЦіна: {self.products[0]['price']}\nОпис: {self.products[0]['description']}")
        product2 = Label(text= f"Назва: {self.products[1]['name']}\nЦіна: {self.products[1]['price']}\nОпис: {self.products[1]['description']}")
        product3 = Label(text= f"Назва: {self.products[2]['name']}\nЦіна: {self.products[2]['price']}\nОпис: {self.products[2]['description']}")
        product4 = Label(text= f"Назва: {self.products[3]['name']}\nЦіна: {self.products[3]['price']}\nОпис: {self.products[3]['description']}")

        self.buy_product1 = Button(text = "Купити Бустер1")
        self.buy_product2 = Button(text="Купити Бустер2")
        self.buy_product3 = Button(text="Купити Бустер3")
        self.buy_product4 = Button(text="Купити Бустер4")

        layout_product1 = BoxLayout()
        layout_product2 = BoxLayout()
        layout_product3 = BoxLayout()
        layout_product4 = BoxLayout()

        layout_product1.add_widget(product1)
        layout_product1.add_widget(self.buy_product1)

        layout_product2.add_widget(product2)
        layout_product2.add_widget(self.buy_product2)

        layout_product3.add_widget(product3)
        layout_product3.add_widget(self.buy_product3)

        layout_product4.add_widget(product4)
        layout_product4.add_widget(self.buy_product4)

        self.back = Button(text = "Повернутися")

        layout = BoxLayout(orientation = "vertical")

        layout.add_widget(layout_product1)
        layout.add_widget(layout_product2)
        layout.add_widget(layout_product3)
        layout.add_widget(layout_product4)

        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1

        self.buy_product1.on_press = self.Buy1
        self.buy_product2.on_press = self.Buy2
        self.buy_product3.on_press = self.Buy3
        self.buy_product4.on_press = self.Buy4

    def Buy1(self):
        pass

    def Buy2(self):
        pass

    def Buy3(self):
        pass

    def Buy4(self):
        pass

    def back1(self):
        self.manager.current = "menu"

class Shares(Screen):
    def __init__(self, name="shares"):
        super().__init__(name=name)

        buy_shares = Button(text = "Купити акції")
        sell_shares = Button(text = "Продати акції")

        self.back = Button(text = "Повернутися")

        layout = BoxLayout(orientation = "vertical")

        layout.add_widget(buy_shares)
        layout.add_widget(sell_shares)
        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1

    def back1(self):
        self.manager.current = "menu"

class Business(Screen):
    def __init__(self, name="business"):
        super().__init__(name=name)

        buy_business = Button(text = "Купити бізнес")
        sell_business = Button(text = "Продати бізнес")
        self.back = Button(text = "Повернутися")

        layout = BoxLayout(orientation = "vertical")

        layout.add_widget(buy_business)
        layout.add_widget(sell_business)
        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1

    def back1(self):
        self.manager.current = "menu"

class Achievement(Screen):
    def __init__(self, name="achievement"):
        super().__init__(name=name)

        text = Label(text = "Скоро буде")
        self.back = Button(text = "Повернутися")

        layout = BoxLayout(orientation = "vertical")

        layout.add_widget(text)
        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1

    def back1(self):
        self.manager.current = "menu"
class Game(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1())
        sm.add_widget(Screen2())
        sm.add_widget(Screen3())
        sm.add_widget(Screen4())
        sm.add_widget(Shop())
        sm.add_widget(Shares())
        sm.add_widget(Business())
        sm.add_widget(Achievement())

        return sm

app=Game()
app.run()
import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.progressbar import ProgressBar
from screen_base import ScreenBase
from player import player
from shares import Share



class Screen1(ScreenBase):
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



class Screen2(ScreenBase):
    def __init__(self, name="pers"):
        super().__init__(name=name)

        self.name_text = Label(text="Введіть ім'я")
        self.age_text = Label(text="Введіть вік")

        self.cont = Button(text="Продовжити")

        self.player_name = TextInput(multiline=False)
        self.player_age = TextInput(multiline=False)

        layout1 = BoxLayout(orientation ="vertical")

        name_layout = BoxLayout()
        age_layout = BoxLayout()

        name_layout.add_widget(self.name_text)
        name_layout.add_widget(self.player_name)

        age_layout.add_widget(self.age_text)
        age_layout.add_widget(self.player_age)

        layout1.add_widget(name_layout)
        layout1.add_widget(age_layout)
        layout1.add_widget(self.cont)

        self.add_widget(layout1)

        self.cont.on_press = self.next

    def next(self):
        player.name = self.player_name.text
        player.age = self.player_age.text
        app.load_player_progress(player.name)
        self.manager.current = "click"
        app.update_text_on("click")


class Screen3(ScreenBase):
    def __init__(self, name="click"):
        super().__init__(name=name)

        self.money = Label(text=f"Ваш баланс: {player.balance}\nВаш прибуток: {player.profit}")

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
        player.update_balance(player.profit)
        self.update_text()

    def update_text(self):
        self.money.text = f"Ваш баланс: {player.balance}\nВаш прибуток: {player.profit}"

    def next(self):
        self.manager.current = "menu"


class Screen4(ScreenBase):
    def __init__(self, name="menu"):
        super().__init__(name=name)

        self.shop = Button(text = "Магазин")
        self.business = Button(text = "Бізнеси")
        self.shares = Button(text = "Акції")
        self.achievement = Button(text = "Досягнення")
        self.back = Button(text = "Перейти назад")
        self.save = Button(text = "Зберегти гру")

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
        layout.add_widget(self.save)

        self.add_widget(layout)

        self.back.on_press = self.back1
        self.shop.on_press = self.shop1
        self.shares.on_press = self.shares1
        self.business.on_press = self.business1
        self.achievement.on_press = self.achievement1
        self.save.on_press = self.save1

    def save1(self):
        app.save_player_progress()

    def shop1(self):
        self.manager.current = "shop"

    def shares1(self):
        self.manager.current = "shares"
        for share in player.shares:
            share.update_price()
        app.update_text_on("shares")


    def business1(self):
        self.manager.current = "business"

    def achievement1(self):
        self.manager.current = "achievement"
        app.update_text_on("achievement")

    def back1(self):
        self.manager.current = "click"
        app.update_text_on("click")


class Shop(ScreenBase):
    def __init__(self, name="shop"):
        super().__init__(name=name)

        with open('data/data.json', 'rb') as file:
            data = json.load(file)
            self.products = data["products"]

        product_labels = [
            Label(text = f"Назва: {item['name']}\nЦіна: {item['price']}\nОпис: {item['description']}")
            for item in self.products
        ]

        buy_buttons = [
            Button(text= f"Купити {item['name']}" if not item['purchased'] else "Куплено")

            for item in self.products
        ]

        layouts = [
            BoxLayout()
            for i in range(len(self.products))
        ]

        for index, layout in enumerate(layouts):
            layout.add_widget(product_labels[index])
            layout.add_widget(buy_buttons[index])

        self.back = Button(text = "Повернутися")

        layout = BoxLayout(orientation = "vertical")

        for l in layouts:
            layout.add_widget(l)

        layout.add_widget(self.back)
        self.add_widget(layout)

        self.back.on_press = self.back1

        for index, button in enumerate(buy_buttons):
            button.on_press = lambda x = None, index=index: self.purchase(index ,self.products[index])

    def purchase(self, index ,product):
        if self.products[index]["purchased"]:
            return

        if player.balance <  product["price"]:
            return

        self.products[index]["purchased"] = True
        player.profit = product["profit"]
        player.update_balance(-product["price"])

    def back1(self):
        self.manager.current = "menu"
        app.update_text_on("menu")


class Shares(ScreenBase):
    def __init__(self, name="shares"):
        super().__init__(name=name)

        buy_shares = Button(text = "Купити акції")
        sell_shares = Button(text = "Продати акції")

        self.back = Button(text = "Повернутися")

        share_prices = [share.price for share in player.shares]
        total_price = sum(share_prices)

        self.shares_amount = Label(text = f"Кількість акцій: {len(player.shares)}")
        self.total_price_text = Label(text = f"Ціна ваших акцій: {total_price}")
        self.price_shares_text = Label(text = f"Ціна одної акції: {Share.price}")

        layout_price = BoxLayout()

        layout_price.add_widget(self.price_shares_text)
        layout_price.add_widget(self.shares_amount)
        layout_price.add_widget(self.total_price_text)

        layout = BoxLayout(orientation = "vertical")

        layout.add_widget(layout_price)
        layout.add_widget(buy_shares)
        layout.add_widget(sell_shares)
        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1

    def back1(self):
        self.manager.current = "menu"

    def buy_shares(self):
        player.shares.append(Share())

    def update_text(self):
        share_prices = [share.price for share in player.shares]
        total_price = sum(share_prices)

        self.shares_amount.text = f"Кількість акцій: {len(player.shares)}"
        self.total_price_text = f"Ціна ваших акцій: {total_price}"
        self.price_shares_text = f"Ціна одної акції: {Share.price}"







class Business(ScreenBase):
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

class Achievement(ScreenBase):
    def __init__(self, name="achievement"):
        super().__init__(name=name)

        self.progress_bar = ProgressBar(max = 1000, value = 0)
        self.progress_text = Label (text = "Заробіть свою першу тисячу грн.")


        self.back = Button(text = "Повернутися")

        layout_progress = BoxLayout()

        layout_progress.add_widget(self.progress_text)
        layout_progress.add_widget(self.progress_bar)

        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(layout_progress)
        layout.add_widget(self.back)

        self.add_widget(layout)

        self.back.on_press = self.back1

    def update_text(self):
        self.progress_bar.value = player.total_balance


    def back1(self):
        self.manager.current = "menu"


class Game(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Screen1())
        self.sm.add_widget(Screen2())
        self.sm.add_widget(Screen3())
        self.sm.add_widget(Screen4())
        self.sm.add_widget(Shop())
        self.sm.add_widget(Shares())
        self.sm.add_widget(Business())
        self.sm.add_widget(Achievement())

        return self.sm

    def update_text_on(self, screen_name):
        screen = self.sm.get_screen(screen_name)
        screen.update_text()
    
    def save_player_progress(self):
        data = {}
        with open('data/data.json', 'rb') as file:
            data = json.load(file)

            for index, saved_player in enumerate(data['players']):
                if saved_player['name'] == player.name:
                    data["players"][index] = player.to_json()
                    break
            else:
                data['players'].append(player.to_json())
        
        with open('data/data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def load_player_progress(self, username):
        with open('data/data.json', 'rb') as file:
            data = json.load(file)
            for index, saved_player in enumerate(data['players']):
                if username == saved_player['name']:
                    player.load_data(data["players"][index])

    def on_start(self):
        self.load_player_progress("admin")

    def on_stop(self):
       self.save_player_progress()


app = Game()

app.run()

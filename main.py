from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class MeatCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super(MeatCalculator, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Поля ввода для расчета стоимости мяса
        self.price_per_kg_label = Label(text='Цена за килограмм:', font_size='18sp', size_hint_y=None, height=40)
        self.price_per_kg_input = TextInput(input_filter='float', multiline=False, halign='center', size_hint_y=None, height=40, hint_text='Введите цену за кг')
        self.price_per_kg_input.bind(focus=self.center_text)
        self.weight_label = Label(text='Вес продукта в граммах:', font_size='18sp', size_hint_y=None, height=40)
        self.weight_input = TextInput(input_filter='int', multiline=False, halign='center', size_hint_y=None, height=40, hint_text='Введите вес в граммах')
        self.weight_input.bind(focus=self.center_text)
        self.discount_label = Label(text='Процент скидки:', font_size='18sp', size_hint_y=None, height=40)
        self.discount_input = TextInput(input_filter='float', multiline=False, halign='center', size_hint_y=None, height=40, hint_text='Введите процент скидки (если есть)')
        self.discount_input.bind(focus=self.center_text)

        # Кнопка для расчета стоимости мяса
        self.calculate_meat_button = Button(text='Рассчитать стоимость мяса', font_size='20sp', background_color=(0.2, 0.6, 0.8, 1), size_hint_y=None, height=50)
        self.calculate_meat_button.bind(on_press=self.calculate_meat_cost)

        # Поля ввода для расчета стоимости по акции
        self.promo_price_label = Label(text='Цена по акции:', font_size='18sp', size_hint_y=None, height=40)
        self.promo_price_input = TextInput(input_filter='float', multiline=False, halign='center', size_hint_y=None, height=40, hint_text='Введите цену товара')
        self.promo_price_input.bind(focus=self.center_text)
        self.promo_discount_label = Label(text='Процент скидки:', font_size='18sp', size_hint_y=None, height=40)
        self.promo_discount_input = TextInput(input_filter='float', multiline=False, halign='center', size_hint_y=None, height=40, hint_text='Введите процент скидки')
        self.promo_discount_input.bind(focus=self.center_text)

        # Кнопка для расчета стоимости по акции
        self.calculate_promo_button = Button(text='Рассчитать стоимость по акции', font_size='20sp', background_color=(0.2, 0.6, 0.8, 1), size_hint_y=None, height=50)
        self.calculate_promo_button.bind(on_press=self.calculate_promo_cost)

        # Добавляем виджеты на экран
        self.add_widget(self.price_per_kg_label)
        self.add_widget(self.price_per_kg_input)
        self.add_widget(self.weight_label)
        self.add_widget(self.weight_input)
        self.add_widget(self.discount_label)
        self.add_widget(self.discount_input)
        self.add_widget(self.calculate_meat_button)
        self.add_widget(self.promo_price_label)
        self.add_widget(self.promo_price_input)
        self.add_widget(self.promo_discount_label)
        self.add_widget(self.promo_discount_input)
        self.add_widget(self.calculate_promo_button)

    def center_text(self, instance, value):
        if not value:
            instance.text = instance.text.center(10)

    def calculate_meat_cost(self, instance):
        try:
            price_per_kg = float(self.price_per_kg_input.text)
            weight = float(self.weight_input.text) / 1000  # Переводим граммы в килограммы
            discount = float(self.discount_input.text) / 100
            total_cost = price_per_kg * weight
            total_cost -= total_cost * discount
            self.show_result(total_cost)
        except ValueError:
            self.show_error()

    def calculate_promo_cost(self, instance):
        try:
            promo_price = float(self.promo_price_input.text)
            promo_discount = float(self.promo_discount_input.text) / 100
            promo_price -= promo_price * promo_discount
            self.show_result(promo_price)
        except ValueError:
            self.show_error()

    def show_result(self, total_cost):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Итого', font_size='20sp'))
        content.add_widget(Label(text=f'Цена: {total_cost:.2f} руб', font_size='18sp'))
        ok_button = Button(text='OK', size_hint_y=0.2, font_size='18sp', background_color=(0.3, 0.9, 0.4, 1))
        content.add_widget(ok_button)

        popup = Popup(title='Результат',
                      content=content,
                      size_hint=(0.8, 0.5))

        ok_button.bind(on_press=popup.dismiss)
        popup.open()

    def show_error(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Ошибка: Проверьте введенные данные.', font_size='18sp'))
        ok_button = Button(text='OK', size_hint_y=0.2, font_size='18sp', background_color=(0.9, 0.3, 0.4, 1))
        content.add_widget(ok_button)

        popup = Popup(title='Ошибка',
                      content=content,
                      size_hint=(0.8, 0.5))

        ok_button.bind(on_press=popup.dismiss)
        popup.open()

class MeatCalculatorApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MeatCalculator()

if __name__ == '__main__':
    MeatCalculatorApp().run()

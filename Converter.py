from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class ConverterApp(MDApp):
    def help(self):
        if self.state == 0:
            self.state = 1
            self.converted.text = "Enter the number and press 'Convert'"
        else:
            self.state = 0
            self.converted.text = ""

    def build(self):
        Window.size = [500, 600]
        self.state = 0
        screen = MDScreen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["help", lambda x: self.help()]]
        screen.add_widget(self.toolbar)
        self.tinput = MDTextField(
                    hint_text="Enter a binary number",
                    halign="center",
                    size_hint=(0.8, 1),
                    pos_hint={'center_x': 0.5, 'center_y': 0.46}
                    )
        screen.add_widget(self.tinput)
        headtitle = MDLabel(
                            text="Number Bases",
                            halign="center",
                            pos_hint={'center_x': 0.5, 'center_y': 0.85},
                            font_style="H5"
                        )
        screen.add_widget(headtitle)
        Title = MDLabel(
                        text="Converter",
                        theme_text_color="Custom",
                        text_color="orange",
                        halign="center",
                        pos_hint={'center_x': 0.5, 'center_y': 0.76},
                        font_style="H1"
                    )
        screen.add_widget(Title)
        self.converted = MDLabel(
                            halign="center",
                            pos_hint={'center_x': 0.5, 'center_y': 0.55},
                            theme_text_color="Custom",
                            text_color="orange",
                            font_style="H5"
                        )
        screen.add_widget(self.converted)
        self.label = MDLabel(
                            halign="center",
                            pos_hint={'center_x': 0.5, 'center_y': 0.6}
                        )
        screen.add_widget(self.label)

        btn = MDRectangleFlatButton(
                        text="Bin to Dec",
                        pos_hint={'center_x': 0.2, 'center_y': 0.3},
                        on_release=self.butnfunc
                        )
        screen.add_widget(btn)
        btn1 = MDRectangleFlatButton(
                        text="Dec to Bin",
                        pos_hint={'center_x': 0.4, 'center_y': 0.3},
                        on_release=self.butnfunc1
                        )
        screen.add_widget(btn1)
        btn2 = MDRectangleFlatButton(
                        text="Dec to Oct",
                        pos_hint={'center_x': 0.6, 'center_y': 0.3},
                        on_release=self.butnfunc2
                        )
        screen.add_widget(btn2)
        btn4 = MDRectangleFlatButton(
                            text="Dec to Hex",
                            pos_hint={'center_x': 0.8, 'center_y': 0.3},
                            on_release=self.butnfunc3
                        )
        screen.add_widget(btn4)
        self.btn3 = MDFillRoundFlatButton(
                            text="Convert",
                            font_size=20,
                            pos_hint={'center_x': 0.5, 'center_y': 0.16},
                            on_release=self.convert
                            )
        screen.add_widget(self.btn3)
        return screen

    def butnfunc(self, obj):
        self.converted.text = ""
        self.label.text = ""
        self.toolbar.title = "Binary to Decimal"
        self.tinput.hint_text = "Enter a binary number"

    def butnfunc1(self, obj):
        self.converted.text = ""
        self.label.text = ""
        self.toolbar.title = "Decimal to Binary"
        self.tinput.hint_text = "Enter a Decimal number"

    def butnfunc2(self, obj):
        self.converted.text = ""
        self.label.text = ""
        self.toolbar.title = "Decimal to Octal"
        self.tinput.hint_text = "Enter a Decimal number"

    def butnfunc3(self, obj):
        self.converted.text = ""
        self.label.text = ""
        self.toolbar.title = "Decimal to Hexadecimal"
        self.tinput.hint_text = "Enter a Decimal number"

    def convert(self, obj):
        if self.toolbar.title == "Binary to Decimal":
            try:
                inp = self.tinput.text
                self.converted.text = str(int(inp, 2))
                self.label.text = f"{self.tinput.text}\nIn decimal is:"
                self.tinput.text = ""
            except ValueError:
                self.toolbar.title = "Can't convert"
        elif self.toolbar.title == "Decimal to Binary":
            try:
                self.converted.text = bin(int(self.tinput.text))[2:]
                self.label.text = f"{self.tinput.text}\nIn binary is:"
                self.tinput.text = ""
            except ValueError:
                self.toolbar.title = "Can't convert"
        elif self.toolbar.title == "Decimal to Octal":
            try:
                self.converted.text = oct(int(self.tinput.text))[2:]
                self.label.text = f"{self.tinput.text}\nIn octal is:"
                self.tinput.text = ""
            except ValueError:
                self.toolbar.title = "Can't convert"
        elif self.toolbar.title == "Decimal to Hexadecimal":
            try:
                self.converted.text = hex(int(self.tinput.text))[2:]
                self.label.text = f"{self.tinput.text}\nIn hexadecimal is:"
                self.tinput.text = ""
            except ValueError:
                self.toolbar.title = "Can't convert"
        else:
            self.toolbar.title = "Can't convert"


if __name__ == '__main__':
    ConverterApp().run()

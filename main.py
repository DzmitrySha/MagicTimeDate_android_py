import toga

from toga.style import Pack

from toga.style.pack import COLUMN, ROW


class MyApplication(toga.App):

    def startup(self):

        # Код запуска вашего приложения

        self.main_window = toga.MainWindow(title="Название приложения")

        self.label = toga.Label(text='Привет, мир!', style=Pack(padding=10))

        self.main_window.content = self.label

        self.main_window.show()


def main():
    return MyApplication(formal_name='Мое первое приложение', app_id='com.example.myapp')


if __name__ == '__main__':
    main().main_loop()

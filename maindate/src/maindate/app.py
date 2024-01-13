"""
Generates main years for person base on his(her) birthday date.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from script.maindate_script import get_main_years
from script.magic_time_script import MagicTimeData
from script.nums_time_script import NumsTimeData


class MainDate(toga.App):

    app_name = "Магия времени и значимые даты"

    def __init__(self):
        super().__init__()
        self.main_box = None

        self.date_label = None
        self.date_input = None
        self.date_button = None
        self.result_date = None

        self.magic_time_label = None
        self.magic_time_list = None
        self.result_magic_time = None

        self.nums_times_label = None
        self.nums_times_list = None
        self.result_nums_time = None

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        # создание главного бокса (<span>)
        self.main_box = toga.Box(
            style=Pack(
                direction=COLUMN,
                background_color="#85C1E9",
                font_family="Segoe UI"
            )
        )

        self.date_label = toga.Label(
            text="Выберите дату рождения: ",
            style=Pack(
                padding=(20, 30, 10, 30),
                background_color="#85C1E9",
                font_size=12,
            )
        )

        self.date_input = toga.DatePicker(
            style=Pack(
                padding=(10, 30),
                direction=ROW,
                height=40,
                font_size=12,
            )
        )

        self.date_button = toga.Button(
            text="Вывести результат",
            on_press=self.get_maindates,
            style=Pack(
                padding=(0, 30, 10, 30),
                background_color="#1B4F72",
                color="#ffffff",
                font_size=10
            )
        )
        self.date_button.style.height = 40

        self.result_date = toga.Label(
            text="",
            style=Pack(
                padding=(0, 30, 10, 30),
                background_color="#85C1E9",
                font_size=10
            )
        )
        self.result_date.style.wrap = True
        self.result_date.style.height = 100
        self.result_date.style.width = 300

        self.magic_time_label = toga.Label(
            text="Выберите время (00:00-23:32): ",
            style=Pack(
                padding=(20, 30, 10, 30),
                background_color="#85C1E9",
                font_size=12,
            )
        )

        self.nums_times_label = toga.Label(
            text="Выберите цифру (0-23): ",
            style=Pack(
                padding=(20, 30, 10, 30),
                background_color="#85C1E9",
                font_size=12,
            )
        )
        magic_times_data = MagicTimeData()
        self.magic_time_list = toga.Selection(
            items=magic_times_data.magic_times.keys(),
            style=Pack(
                padding=(0, 30, 10, 30),
                font_size=10
            )
        )
        self.magic_time_list.on_select = self.get_magic_time_description

        nums_times_data = NumsTimeData()
        self.nums_times_list = toga.Selection(
            items=nums_times_data.nums_datetimes.keys(),
            style=Pack(
                padding=(0, 30, 10, 30),
                font_size=10
            )
        )
        self.nums_times_list.on_select = self.get_nums_time_description

        self.result_magic_time = toga.Label(
            text="",
            style=Pack(
                padding=(0, 30, 10, 30),
                background_color="#85C1E9",
                font_size=10
            )
        )
        self.result_magic_time.style.wrap = True
        self.result_magic_time.style.height = 100
        self.result_magic_time.style.width = 300

        self.result_nums_time = toga.Label(
            text="",
            style=Pack(
                padding=(0, 30, 10, 30),
                background_color="#85C1E9",
                font_size=10
            )
        )
        self.result_nums_time.style.wrap = True
        self.result_nums_time.style.height = 100
        self.result_nums_time.style.width = 300

        # Подключение полей
        self.main_box.add(self.date_label)
        self.main_box.add(self.date_input)
        self.main_box.add(self.date_button)
        self.main_box.add(self.result_date)

        self.main_box.add(self.magic_time_label)
        self.main_box.add(self.magic_time_list)
        self.main_box.add(self.result_magic_time)

        self.main_box.add(self.nums_times_label)
        self.main_box.add(self.nums_times_list)
        self.main_box.add(self.result_nums_time)

        # главное окно программы
        self.main_window = toga.MainWindow(
            title="Магия времени и значимые даты",
            position=(400, 200),
            resizable=False,
            size=(400, 500)
        )
        self.main_window.content = self.main_box
        self.main_window.show()

    def get_maindates(self, widget):
        year = self.date_input.value.year
        month = self.date_input.value.month
        day = self.date_input.value.day
        self.result_date.text = get_main_years(year, month, day)
        # self.main_window.info_dialog(
        #     title=f"Результат",
        #     message=get_main_years(year, month, day)
        # )

    def get_magic_time_description(self, widget):
        magic_time_data = MagicTimeData()
        selected_magic_time = self.magic_time_list.value
        self.result_magic_time.text = magic_time_data.get_magic_time_description(selected_magic_time)

    def get_nums_time_description(self, widget):
        nums_time_data = NumsTimeData()
        selected_nums_time = self.nums_times_list.value
        self.result_nums_time.text = nums_time_data.get_num_description(selected_nums_time)


def main():
    return MainDate()

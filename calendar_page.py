from flet import *

import calendar
import datetime

class SetCalendar(UserControl):
    def __init__(self, start_year=datetime.date.today().year):
        self.current_year = start_year
        self.current_month = datetime.date.today().month
        self.next_month = datetime.date.today().month + 1
        self.click_count: list = []
        self.long_press_cout: list = []

        self.current_color = "blue"
        self.selected_date = any
        self.calendar_grid = Column(
            wrap=True,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        super().__init__()

    def create_month_calendar(self, year):
        self.current_year = year
        self.calendar_grid.controls: list = []

        for month in range(self.current_month, self.next_month):
            month_label = Text(
                f"{calendar.month_name[month]} {self.current_year}",
                size=14,
            )
            month_matrix = calendar.monthcalendar(self.current_year, month)
            month_grid = Column(alignment=MainAxisAlignment.CENTER)
            month_grid.controls.append(
                Row(
                    alignment=MainAxisAlignment.START,
                    controls=[
                        month_label,
                    ]
                )
            )

            weekday_labels = [
                Container(
                    width=32,
                    height=28,
                    alignment=alignment.center,
                    content=Text(
                        weekday,
                        size=12,
                        selectable=True,
                    )
                )
                for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            ]

            weekday_row = Row(controls=weekday_labels)
            month_grid.controls.append(weekday_row)

            for week in month_matrix:
                week_container = Row()
                for day in week:
                    if day == 0:
                        day_container = Container(
                            width=32,
                            height=32,
                        )
                    else:
                        day_container = Container(
                            width=32,
                            height=32,
                            border_radius=7,
                            border=border.all(0.5, "#eaeaea"),
                            alignment=alignment.center,
                            data=datetime.date(
                                year=self.current_year,
                                month=month,
                                day=day,
                            ),
                            on_click=lambda e: self.one_click_date(e),
                            on_long_press=lambda e: self.show_two_dates(e),
                            animate=400,
                        )
                    day_label = Text(str(day), size=12)

                    if day == 0:
                        day_label = None
                    if (day == datetime.date.today().day and month == datetime.date.today().month and self.current_year == datetime.date.today().year):
                        day_container.bgcolor = "#8da3b9"
                        day_container.border = border.all(0.5, "#8da3b9")
                    day_container.content = day_label
                    week_container.controls.append(day_container)
                month_grid.controls.append(week_container)

        self.calendar_grid.controls.append(month_grid)

        return self.calendar_grid

    def change_month(self, delta):
        # recall that we stored the current month + month2 above as self.current_month and self.next_month
        # we can use hte max and min to make sure the numbers stay between 1 and 13, as per the calendar library
        self.current_month = min(max(1, self.current_month + delta), 12)
        self.next_month = min(max(2, self.next_month + delta), 13)

        new_calendar = self.create_month_calendar(self.current_year)
        self.calendar_grid = new_calendar
        self.update()

    def one_click_date(self, e):
        self.selected_date = e.control.data
        e.control.bgcolor = 'blue600'
        e.control.update()
        self.update()

    def build(self):
        return self.create_month_calendar(self.current_year)


class DateSetUp(UserControl):
    def __init__(self, calendar_grid):
        self.calendar_grid = calendar_grid

        self.prev_button = ButtonPagination(
            "Prev", lambda e: calendar_grid.change_month(-1))
        self.next_button = ButtonPagination(
            "Next", lambda e: calendar_grid.change_month(1))

        self.today = Text(
            datetime.date.today().strftime("%B %d, %Y"),
            width=260,
            size=13,
        )

        self.button_container = Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                self.prev_button,
                self.next_button,
            ]
        )

        self.calendar = Container(
            width=320,
            height=475,
            bgcolor="#ffffff",
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color='#10100000',
            ),
            border=border.all('0.8', '#eaeaea'),
            border_radius=10,
            animate=400,
            clip_behavior=ClipBehavior.HARD_EDGE,
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Divider(height=30, color='transparent'),
                    self.calendar_grid,
                    Container(height=20),
                    Container(
                        padding=padding.only(left=20, right=20, bottom=15),
                        content=Divider(height=1, thickness=0.25),
                    ),
                    self.button_container,
                ],
            )
        )

        super().__init__()


    def build(self):
        return self.calendar

class ButtonPagination(UserControl):
    def __init__(self, text_name, function):
        self.text_name = text_name
        self.function = function
        super().__init__()

    def build(self):
        return IconButton(
            content=Text(self.text_name, size=9),
            width=54,
            height=32,
            icon_size=18,
            on_click=self.function,
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6)
                }
            )
        )


def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.padding = 80
    page.theme_mode = ThemeMode.LIGHT
    calendar = SetCalendar()
    date = DateSetUp(calendar)

    page.add(
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                date,
            ],
        )
    )


if __name__ == "__main__":
    app(target=main)

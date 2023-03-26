from flet import *
from system_info import *


class Monitor(UserControl):
    def __init__(self, type):
        super().__init__()
        self.total, self.usage, self.percentage = get_type(type)
        self.type = type
        if type == 'memory':
            self.icon = icons.RECTANGLE_ROUNDED
        if type == 'cpu':
            self.icon = icons.COMPUTER
        if type == 'disk':
            self.icon = icons.PIE_CHART

    def update_information(self, e):
        print("hello")
        self.total, self.usage, self.percentage = get_type(self.type)
        self.progress_bar_inner.width = self.percentage * 350
        self.progress_bar_inner.update()

    def main_container(self):

        self.progress_bar_outer = Container(
            height=15,
            width=400,
            border_radius=8,
            bgcolor='#efefef',
            # gradient=LinearGradient(
            #     begin=alignment.top_left,
            #     end=alignment.bottom_right,
            #     colors=["#F5E0DC", "#F5D5E9"],
            # ),
            animate=animation.Animation(1000, "decelerate"),
        )

        self.progress_bar_inner = Container(
            height=15,
            width=350 * self.percentage,
            border_radius=8,
            bgcolor='#8da3b9',
            # gradient=LinearGradient(
            #     begin=alignment.top_left,
            #     end=alignment.bottom_right,
            #     colors=["#F5E0DC", "#F5D5E9"],
            # ),
            animate=animation.Animation(1000, "decelerate"),
        )

        self.progress_bar = Stack(
            controls=[
                self.progress_bar_outer,
                self.progress_bar_inner,
            ]
        )

        self.text_row = Row(
            width=400,
            alignment="spaceBetween",
            vertical_alignment="end",
            controls=[
                Container(
                    content=Text(
                        value=self.type.title(),
                        size=12,
                        # color="#fdfdfd",
                        weight="w500",

                    )
                ),
                Container(
                    content=Text(
                        f"Usage: {round(self.usage, 2)}GB/{round(self.total, 2)}GB",
                        size=12,
                        weight="w400",

                    )
                )
            ]
        )

        self.icon_type = IconButton(
            icon=self.icon,
            icon_size=23,
            icon_color='#bbbbbb',
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=7),
                },
            ),
        )

        self.information_display_container = Container(
            width=480,
            height=100,
            border_radius=12,
            bgcolor='#fefefe',
            border=border.all(0.5, '#dadada'),
            # opacity=0.6,
            alignment=alignment.center,
            content=Row(
                alignment='center',
                controls=[
                    Container(
                        content=self.icon_type,
                    ),
                    Container(
                        padding=padding.only(right=16),
                        alignment=alignment.center,
                        content=Column(
                            alignment='center',
                            controls=[
                                self.text_row,
                                self.progress_bar,
                            ]
                        ),
                    )
                ]
            )
        )

        self.view = Container(
            # height=100,
            width=480,
            # elevation=0,
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color='#10100000'
            ),
            margin=Margin(10, 5, 10, 5),
            content=Row(
                alignment='center',
                controls=[
                    self.information_display_container,
                ],
            )
        )

        return self.view

    def build(self):
        return self.main_container()


# def main(page: Page):
#     page.vertical_alignment='center'
#     page.horizontal_alignment='center'
#     monitor=Monitor('cpu')
#     page.add(
#         monitor
#     )


# app(target=main)

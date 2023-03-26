from flet import *
# import monitor


class ModernNavBar(UserControl):
    def __init__(self, page, page1, page2, page3, page4):
        super().__init__()
        self.page = page
        self.page1 = page1
        self.page2 = page2
        self.page3 = page3
        self.page4 = page4

        self.pages = {
            'page1': self.page1,
            'page2': self.page2,
            'page3': self.page3,
            'page4': self.page4,
        }
    # hover: #eaeaea
    # click: #ededed
    # accent: #8da3b9

    def icon_button_hover(self, e):
        if e.data == 'true':
            e.control.bgcolor = "#8da3b9"
        else:
            e.control.bgcolor = None
        e.control.update()

    def change_indictor_color(self, e):
        if e.data == 'true':
            e.control.border = border.only(bottom=border.BorderSide(
                width=3, color='#8da3b9'))
        else:
            e.control.border = border.only(bottom=border.BorderSide(
                width=2, color='#cecece'))
        e.control.update()

    def sidebar_button_hovered(self, e: HoverEvent):
        if e.data == 'true':
            if e.control.bgcolor == '#ededed':
                pass
            else:
                e.control.bgcolor = '#eaeaea'
        else:
            if e.control.bgcolor == '#ededed':
                pass
            else:
                e.control.bgcolor = None
        e.control.update()

    def search_line(self):
        self.search_line = Container(
            padding=padding.only(top=20),
            # expand=True,
            content=Row(
                alignment='center',
                controls=[
                    Container(
                        clip_behavior=ClipBehavior.ANTI_ALIAS,
                        border_radius=10,
                        content=Container(
                            on_hover=lambda e: self.change_indictor_color(e),
                            clip_behavior=ClipBehavior.HARD_EDGE,
                            border_radius=9,
                            height=40,
                            width=225,
                            bgcolor='#eaeaea',
                            animate=200,
                            border=border.only(bottom=border.BorderSide(
                                width=2, color='#cecece')),
                            content=Row(
                                controls=[
                                    Container(
                                        width=180,
                                        padding=padding.only(left=15),
                                        content=TextField(
                                            border=InputBorder.NONE,
                                            hint_text="Search ...",
                                            hint_style=TextStyle(
                                                size=13,
                                                color="#707070",
                                            ),
                                            text_style=TextStyle(
                                                size=13,
                                            ),
                                            content_padding=padding.only(
                                                bottom=10, top=0),
                                        )
                                    ),

                                    Container(
                                        height=25,
                                        width=25,
                                        border_radius=8,
                                        padding=padding.only(top=2),
                                        on_hover=self.icon_button_hover,
                                        content=Icon(
                                            icons.SEARCH_OUTLINED,
                                            size=16,
                                        ),
                                    )
                                ]
                            )
                        )
                    )
                ]
            )
        )
        return self.search_line

    def icon_list(self):
        self.function_icon_list = Column(
            controls=[
                self.contained_icon(icons.PIE_CHART, "Monitor", 'page1'),
                self.contained_icon(icons.CHAT,
                                    "Chat", 'page2'),
                self.contained_icon(icons.TASK_ALT_ROUNDED, "Task", 'page3'),
            ]
        )
        # for button in self.funcion_icon_list.controls[:]:
        #     if button.data == True:
        #         button.bgcolor = '#ededed'
        self.function_icon_list.controls[0].bgcolor = '#ededed'
        return self.function_icon_list

    def change_bgcolor(self, e):
        for button in self.function_icon_list.controls[:]:
            button.bgcolor, button.data = None, 'false'
            button.update()

        for button in self.settings_button_list.controls[:]:
            button.bgcolor = None
            button.update()

        if e.control.data != 'true':
            e.control.bgcolor = '#ededed'
            e.control.update()

    def user_data(self, initials: str, name: str, description: str):
        return Container(
            padding=padding.only(top=30, left=10),
            content=Row(
                controls=[
                    Container(
                        width=50,
                        height=42,
                        bgcolor="#dedede",
                        alignment=alignment.center,
                        border_radius=10,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
                            color="dedede",
                            font_family="DankMono Nerd Font",
                        )
                    ),
                    Column(
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight="bold",
                                opacity=1,
                                animate_opacity=200,
                                font_family="inter"
                            ),
                            Text(
                                value=description,
                                size=11,
                                # weight="bold",
                                opacity=1,
                                animate_opacity=200,
                                font_family="Inter",
                                color="#adadad"
                            ),
                        ],
                        spacing=1,
                        alignment='center',
                    )
                ]
            ),
        )

    def divider(self):
        return Container(
            padding=padding.only(top=10, left=10, right=10, bottom=7),
            content=Divider(thickness=1, color="#eaeaea"),
        )

    def contained_icon(self, icon_name: str, text: str, point: str):
        return Container(
            width=230,
            height=40,
            border_radius=10,
            padding=padding.only(right=10, left=10),
            animate=200,
            animate_opacity=200,
            on_hover=lambda e: self.sidebar_button_hovered(e),
            on_click=lambda e: self.button_click(e, point),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="#8da3b9",
                        selected=False,
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        size=12,
                        opacity=1,
                        animate_opacity=200,
                    ),

                ]
            ),
        )

    def settings_list(self):
        self.settings_button_list = Column(
            controls=[
                self.contained_icon("SETTINGS_OUTLINED", "Settings", 'page4')
            ]
        )
        return self.settings_button_list

    def toggle_side_bar(self):
        pass

    def button_click(self, e, point):
        self.change_bgcolor(e)
        self.switch_page(e, point)

    # def switch_page(self, e, point):
    #     print(point)
    #     for page in self.pages:
    #         self.pages[page].offset.x = 1
    #         self.pages[page].update()

    #     self.pages[point].offset.x = 0
    #     self.pages[point].update()

    def switch_page(self, e, point):
        print(point)
        for page in self.pages:
            self.pages[page].offset.y = 1
            # if page != point:
            #     self.pages[page].visible=False
            self.pages[page].opacity = 0
            self.pages[page].update()

        self.pages[point].offset.y = 0
        # self.pages[point].visible = True
        self.pages[point].opacity = 1
        self.pages[point].update()

    def build(self):
        self.view = Container(
            animate=animation.Animation(
                duration=500, curve=AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN),
            width=250,
            padding=10,
            expand=True,
            bgcolor='#f2f2f2',
            border=border.only(right=border.BorderSide(1, "#dbdbdb")),
            content=Column(
                alignment='end',
                controls=[
                    Container(
                        expand=True,
                        content=Column(
                            alignment=MainAxisAlignment.START,
                            controls=[
                                self.user_data("Z", "Developer: zxnix",
                                               "Software engineer"),
                                self.search_line(),
                                self.divider(),
                                self.icon_list(),
                            ],
                        ),
                    ),
                    Column(
                        #alignment=MainAxisAlignment.END,
                        controls=[
                            self.divider(),
                            self.settings_list(),
                        ],
                    ),

                ]
            )
        )
        return self.view


# def main(page: Page):
#     page.window_title_bar_hidden = True
#     page.window_opacity = 1
#     page.padding = 0


#     perctange = 0.8
#     WIDTH = page.window_width * 0.4

#     def page_resize(e):
#         if page.window_width < 800:
#             sidebar.view.width = 0
#         else:
#             sidebar.view.width = 250
#         sidebar.update()

#     page.on_resize = page_resize

#     progress_bar_outer = Container(
#         height=15,
#         width=WIDTH,
#         bgcolor='#ededed',
#         animate=animation.Animation(1000, "decelerate"),
#         border_radius=12,

#     )
#     progress_bar_inter = Container(
#         height=16,
#         width=progress_bar_outer.width * perctange,
#         border_radius=12,
#         bgcolor='#8da3b9',
#         animate=animation.Animation(1000, "decelerate"),
#         #expand=True,
#     )

#     infomation_display = Container(
#         #elevation=35,
#         content=Container(
#             alignment=alignment.center,
#             width=WIDTH,
#             height=40,
#             bgcolor='#ffffff',
#             animate=animation.Animation(1000, "accelerate"),
#             border_radius=10,
#             opacity=0.5,
#             content=Stack(
#                 # expand=True,
#                 controls=[
#                     progress_bar_outer,
#                     progress_bar_inter,
#                 ],
#             )
#         )
#     )

#     page1 = Container(
#         alignment=alignment.center,
#         offset=transform.Offset(0, 0),
#         # animate=animation.Animation(
#         #     duration=1100, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         # ),
#         animate_opacity=animation.Animation(
#             duration=500, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         animate_offset=animation.Animation(
#             duration=1100, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         opacity=0.8,
#         gradient=LinearGradient(
#             begin=alignment.top_left,
#             end=alignment.bottom_right,
#             colors=["#F5E0DC", "#F5D5E9"],
#         ),
#         content=infomation_display,
#     )

#     page2 = Container(
#         alignment=alignment.center,
#         offset=transform.Offset(0, 0),
#         animate_opacity=animation.Animation(
#             duration=1000, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         gradient=LinearGradient(
#             begin=alignment.top_left,
#             end=alignment.bottom_right,
#             colors=["#AC8A8C", "#F5D5E9"],
#         ),
#         content=Text('PAGE 2', size=50)
#     )

#     page3 = Container(
#         alignment=alignment.center,
#         offset=transform.Offset(0, 0),

#         animate_offset=animation.Animation(
#             duration=1100, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         animate_opacity=animation.Animation(
#             duration=500, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         gradient=LinearGradient(
#             begin=alignment.top_left,
#             end=alignment.bottom_right,
#             colors=["#F5E0DC", "#AC8A8C"],
#         ),
#         content=Text('PAGE 3', size=50, color='white')
#     )

#     page4 = Container(
#         alignment=alignment.center,
#         animate_offset=animation.Animation(
#             duration=1100, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         animate_opacity=animation.Animation(
#             duration=500, curve=AnimationCurve.FAST_OUT_SLOWIN,
#         ),
#         gradient=LinearGradient(
#             begin=alignment.top_left,
#             end=alignment.bottom_right,
#             colors=["#C49EA0", "#AC8AAC"],
#         ),
#         content=Text('PAGE 4', size=50)
#     )

#     sidebar = ModernNavBar(page, page1, page2, page3, page4)

#     page.add(
#         Container(
#             expand=True,
#             content=Row(
#                 spacing=0,
#                 controls=[
#                     Container(
#                         content=sidebar,
#                     ),
#                     Container(
#                         expand=True,
#                         alignment=alignment.center,
#                         content=Stack(
#                             controls=[
#                                 page1,
#                                 page2,
#                                 page3,
#                                 page4,
#                             ]
#                         )
#                     )
#                 ]
#             )
#         )
#         # monitor.Montior(),

#     )


# # app(target=main)

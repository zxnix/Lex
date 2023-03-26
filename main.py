from sidebar import *
from monitor import *
from chat_page import *

def main(page: Page):
    page.window_title_bar_hidden = True
    page.window_opacity = 1
    page.padding = 0
    page.theme_mode = ThemeMode.LIGHT
    monitor_memory = Monitor('memory')
    monitor_disk = Monitor('disk')
    monitor_cpu = Monitor('cpu')

    def page_resize(e):
        if page.window_width < 800:
            sidebar.view.width = 0
        else:
            sidebar.view.width = 250
        sidebar.update()
    page.on_resize = page_resize

    def update_all_information(e):
        monitor_cpu.update_information(e)
        monitor_disk.update_information(e)
        monitor_memory.update_information(e)


    def send_message_click(e):
        if new_message.value != "":
            message = Message("Z", new_message.value, "hello")
            m = UsrMessage(message)
            if len(new_message.value) > 65:
                m.controls[1].controls[0].width = 450
            chat.controls.append(m)
            completion = new_message.value
            new_message.value = ""
            new_message.focus()
            chat.auto_scroll = True
            chat.update()
            prev_text = ""
            prompt = completion
            message.completion = prev_text
            GPT = GPTMessage(message)
            chat.controls.append(GPT)
            chat.update()
            flag = False
            for data in chatbot.ask(prompt):
                chat.update()
                completion = data["message"][len(prev_text) :]
                prev_text = data["message"]
                if len(prev_text) > 65 and flag == False:
                    flag = True
                    GPT.controls[1].width = 450
                    GPT.controls[1].update()
                message.completion = completion
                GPT.controls[1].content.value = prev_text
                chat.auto_scroll = True
                GPT.controls[1].update()
                chat.update()
                chat.auto_scroll = False
                page.update()


    new_message.on_submit = send_message_click

    page1 = Container(
        alignment=alignment.center,
        animate_opacity=animation.Animation(
            duration=500, curve=AnimationCurve.DECELERATE,
        ),
        offset=transform.Offset(0, 0),
        bgcolor='#ffffff',
        content=Container(
            alignment=alignment.center,
            content=Column(
                controls=[
                    Container(
                        padding=padding.only(right=20),
                        height=50,
                        content=Row(
                            alignment='end',
                            controls=[
                                IconButton(
                                    icon=icons.REFRESH_OUTLINED,
                                    icon_size=23,
                                    icon_color='#bbbbbb',
                                    on_click=lambda e:update_all_information(
                                        e),
                                    style=ButtonStyle(
                                        shape={
                                            "": RoundedRectangleBorder(radius=7),
                                        },
                                    ),
                                ),
                            ]
                        ),
                    ),
                    Container(
                        alignment=alignment.center,
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=20,
                            controls=[
                                monitor_cpu,
                                monitor_disk,
                                monitor_memory,
                            ]
                        )
                    )
                ]
            )
        ),
    )
    

    page2 = Container(
        #margin=10,
        alignment=alignment.center,
        offset=transform.Offset(0, 0),
        animate_opacity=animation.Animation(
            duration=1000, curve=AnimationCurve.DECELERATE,
        ),
        bgcolor='#ffffff',
        content=Column(
            run_spacing=20,
            controls=[
                Container(
                    bgcolor='#ffffff',
                    expand=True,
                    padding=padding.only(top=10, right=10, left=10),
                    content=chat,
                ),
                Container(
                    padding=padding.only(bottom=10, left=10, right=10),
                    alignment = alignment.center,
                    content=Container(
                        border_radius=10,
                        bgcolor='#ffffff',
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color='#10100000',
                        ),
                        content=new_message,
                    )
                )
            ]
        )
    )

    page3 = Container(
        alignment=alignment.center,
        offset=transform.Offset(0, 0),
        animate_opacity=animation.Animation(
            duration=500, curve=AnimationCurve.DECELERATE,
        ),
        bgcolor='#ffffff',
        content=Text('PAGE 3', size=50, color='white')
    )

    page4 = Container(
        alignment=alignment.center,
        offset=transform.Offset(0, 0),
        animate_opacity=animation.Animation(
            duration=500, curve=AnimationCurve.DECELERATE,
        ),
        gradient=LinearGradient(
            begin=alignment.top_left,
            end=alignment.bottom_right,
            colors=["#C49EA0", "#AC8AAC"],
        ),
        content=Text('PAGE 4', size=50)
    )

    sidebar = ModernNavBar(page, page1, page2, page3, page4)

    page.add(
        Container(
            expand=True,
            content=Row(
                spacing=0,
                controls=[
                    Container(
                        content=sidebar,
                    ),
                    Container(
                        expand=True,
                        alignment=alignment.center,
                        content=Stack(
                            controls=[
                                page1,
                                page2,
                                page3,
                                page4,
                            ]
                        )
                    )
                ]
            )
        )
        # monitor.Montior(),

    )


app(target=main)

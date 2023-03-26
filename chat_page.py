from flet import *
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "zxnixis@gmail.com",
  "password": "sx051001"
})

class Message():
    def __init__(self, user_name, text, completion):
        self.user_name = user_name
        self.text = text
        self.completion = completion


class GPTMessage(Row):
    def __init__(self, message: Message):
        super().__init__()
        self.controls = [
            Container(
                margin=margin.only(bottom=10, top=10),
                alignment=alignment.center,
                width=50,
                height=32,
                bgcolor='#ffffff',
                border_radius=10,
                shadow=BoxShadow(
                    spread_radius=1,
                    blur_radius=5,
                    color='#10100000',
                ),
                content=Text(
                    value="GPT",
                    size=12,
                )
            ),
            Container(
                bgcolor='#ffffff',
                border=border.all(0.7, '#eaeaea'),
                border_radius=10,
                padding=10,
                shadow=BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color='#10100000',
                ),
                margin=margin.only(bottom=10, top=10),
                content=Markdown(
                    value=message.completion,
                    selectable=True,
                    code_style=TextStyle(font_family="DankMono Nerd Font"),
                    code_theme="atom-one-light",
                    extension_set=MarkdownExtensionSet.GITHUB_WEB,

                )
            ),
        ]


class UsrMessage(Row):
    def __init__(self, message: Message):
        super().__init__()
        self.alignment = MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = MainAxisAlignment.END
        self.controls = [
            Container(),
            Row(
                controls=[
                    Container(
                        margin=margin.only(bottom=10, top=10),
                        bgcolor='#ffffff',
                        border=border.all(0.7, '#eaeaea'),
                        border_radius=10,
                        padding=10,
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color='#10100000',
                        ),
                        content=Text(
                            value=message.text,
                            size=14,
                            selectable=True,
                        ),
                        animate=animation.Animation(
                            duration=500, curve=AnimationCurve.DECELERATE,
                        ),
                    ),
                    Container(
                        margin=margin.only(bottom=10, top=10),
                        alignment=alignment.center,
                        width=32,
                        height=32,
                        bgcolor='#ffffff',
                        border_radius=5,
                        padding=10,
                        shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color='#10100000',
                        ),
                        content=Text(
                            value=message.user_name,
                            size=12,
                        ),
                        animate=animation.Animation(
                            duration=500, curve=AnimationCurve.DECELERATE,
                        ),
                    ),
                ]
            )
        ]


chat = ListView(
    expand=True,
    padding=10,
    auto_scroll=False,
)

new_message = TextField(
    border_radius=12,
    content_padding=padding.only(left=20, right=20),
    hint_text="Write a message...",
    suffix_icon=icons.SEND,
    focused_border_width=1,
    focused_border_color='#dadada',
    text_size=13,
    autofocus=True,
    shift_enter=True,
    min_lines=1,
    max_lines=5,
    expand=True,
    border_color='#eaeaea',
)



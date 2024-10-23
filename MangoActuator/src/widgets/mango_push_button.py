# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description:
# @Time   : 2024-08-16 17:05
# @Author : 毛鹏
from src import *

style = '''
QPushButton {{
	border: 1px solid {border};
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''


# PY PUSH BUTTON

class MangoPushButton(QPushButton):
    def __init__(
            self,
            text,
            radius=8,
            parent=None,
            color=THEME.text_foreground,
            bg_color=THEME.dark_one,
            bg_color_hover=THEME.dark_three,
            bg_color_pressed=THEME.dark_four
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            border=THEME.dark_four,
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed
        )
        self.setStyleSheet(custom_style)
        self.setMinimumHeight(35)
        self.setMinimumWidth(60)
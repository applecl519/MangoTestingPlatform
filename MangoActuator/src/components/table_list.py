from functools import partial

from PySide6.QtCore import Signal
from PySide6.QtGui import QCursor, Qt, QAction
from PySide6.QtWidgets import *

from src.widgets import *


class TableList(QWidget):
    clicked = Signal(object)
    released = Signal(object)

    def __init__(self, row_column: list[dict], row_ope: list[dict] = None):
        super().__init__()
        self.row_column = row_column
        self.row_ope = row_ope
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.table_widget = PyTableWidget()
        self.table_widget.setColumnCount(len(row_column))
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setHorizontalHeaderLabels([i.get('name') for i in self.row_column])
        self.layout.addWidget(self.table_widget)
        self.pagination = MangoPagination()
        self.layout.addWidget(self.pagination)
        self.setLayout(self.layout)

    def set_data(self, data: list[dict]):
        for row, item in enumerate(data):
            self.table_widget.insertRow(row)
            for row1, column in enumerate(self.row_column):
                if column.get('key') != 'ope':
                    if isinstance(item[column.get('key')], dict):
                        item1 = item[column.get('key')]['name']
                    else:
                        item1 = item[column.get('key')]
                    self.table_widget.setItem(row, row1, QTableWidgetItem(item1))
            if self.row_ope:
                action_widget = QWidget()
                action_layout = QHBoxLayout()
                action_widget.setLayout(action_layout)
                for ope in self.row_ope:
                    if ope.get('son', None) is None:
                        but = QPushButton(ope['name'])
                        but.clicked.connect(partial(self.but_clicked, {'action': ope['action'], 'row': item}))
                        but.setStyleSheet(
                            'QPushButton { background-color: transparent; border: none; padding: 0; color: blue; font-size: 11px; }')
                        but.setCursor(QCursor(Qt.PointingHandCursor))
                        action_layout.addWidget(but)
                    else:
                        menu_button = QPushButton(ope['name'])
                        menu_button.setStyleSheet(
                            'QPushButton { background-color: transparent; border: none; padding: 0; color: blue; font-size: 11px; }')
                        menu_button.setCursor(QCursor(Qt.PointingHandCursor))
                        action_layout.addWidget(menu_button)

                        # 创建菜单
                        menu = QMenu()
                        for ope1 in ope.get('son'):
                            action = QAction(ope1['name'], self)
                            action.triggered.connect(partial(self.but_clicked, {'action': ope1['action'], 'row': item}))
                            menu.addAction(action)

                        # 显示菜单
                        menu_button.clicked.connect(lambda: menu.exec_(QCursor.pos()))

                self.table_widget.setCellWidget(row, len(self.row_column) - 1, action_widget)

    def but_clicked(self, data):
        self.clicked.emit(data)

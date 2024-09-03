import math

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QComboBox


class MangoPagination(QWidget):
    clicked = Signal(object)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.common = 0
        self.page = 1
        self.number_part = 10

        # 创建左右箭头图标按钮（使用 QPushButton 并设置样式）
        self.current_page_label1 = QLabel(f"共 {self.common} 条")

        self.prev_icon_button = QPushButton()
        self.prev_icon_button.setMaximumWidth(30)
        self.prev_icon_button.setEnabled(False)
        self.prev_icon_button.setText('<')

        self.next_icon_button = QPushButton()
        self.next_icon_button.setMaximumWidth(30)
        self.next_icon_button.setText('>')

        # 创建当前页显示的标签
        self.current_page_label = QLabel(f"{self.page}")
        self.items_per_page_combo = QComboBox()
        self.items_per_page_combo.addItems(["10 条/页", "20 条/页", "30 条/页", "50 条/页", "100 条/页"])

        # 布局设置
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(self.current_page_label1)
        layout.addWidget(self.prev_icon_button)
        layout.addWidget(self.current_page_label)
        layout.addWidget(self.next_icon_button)
        layout.addWidget(self.items_per_page_combo)

        self.setLayout(layout)

        # 连接左右箭头按钮的点击信号到相应的槽函数（示例，需自定义具体逻辑）
        self.prev_icon_button.clicked.connect(self.on_prev_page)
        self.next_icon_button.clicked.connect(self.on_next_page)

        # 连接下拉选择框的信号到槽函数，以处理每页展示条数的变化
        self.items_per_page_combo.currentIndexChanged.connect(self.on_items_per_page_changed)
        self.button_enabled()

    def on_prev_page(self):
        self.page -= 1
        self.clicked.emit({'action': 'prev', 'page': self.page})
        self.current_page_label.setText(str(self.page))
        self.button_enabled()

    def on_next_page(self):
        self.page += 1
        self.clicked.emit({'action': 'next', 'page': self.page})
        self.current_page_label.setText(str(self.page))
        self.button_enabled()

    def on_items_per_page_changed(self, index):
        selected_text = self.items_per_page_combo.itemText(index)
        self.number_part = int(selected_text.split(" ")[0])
        self.clicked.emit({'action': 'per_page', 'page': self.number_part})

    def set_total_size(self, total_size: str):
        self.current_page_label1.setText(f"共 {total_size} 条")
        if total_size:
            self.common = int(total_size)

    def button_enabled(self):
        if self.page > 1:
            self.prev_icon_button.setEnabled(True)
        else:
            self.prev_icon_button.setEnabled(False)
        if self.page >= math.ceil(self.common / self.number_part):
            self.next_icon_button.setEnabled(False)
        else:
            self.next_icon_button.setEnabled(True)

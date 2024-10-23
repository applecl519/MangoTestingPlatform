# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2024-08-28 16:30
# @Author : 毛鹏
import copy

from src import *
from src.components import *
from src.models.gui_model import *
from src.models.network_model import ResponseModel
from src.network import Http
from .page_steps_dict import *


class PageStepsPage(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.page = 1
        self.page_size = 10
        self.params = {}
        self.title_data = [TitleDataModel(**i) for i in title_data]
        self.form_data = [FormDataModel(**i) for i in form_data]
        for i in self.form_data:
            if i.key == 'project_product':
                i.select = settings.base_dict

        self.table_column = [TableColumnModel(**i) for i in table_column]
        self.table_menu = [TableMenuItemModel(**i) for i in table_menu]

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = TitleWidget(self.title_data)
        self.titleWidget.clicked.connect(self.search)
        self.layout.addWidget(self.titleWidget)

        self.right_data = [
            {'name': '新增', 'theme': THEME.blue, 'func': self.add}
        ]
        self.right_but = RightButton(self.right_data)
        self.layout.addWidget(self.right_but)
        self.table_widget = TableList(self.table_column, self.table_menu, )
        self.table_widget.pagination.clicked.connect(self.pagination_clicked)
        self.table_widget.clicked.connect(self.handle_button_click)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

    def show_data(self, is_refresh=False):
        response_model: ResponseModel = Http.get_page_steps(self.page, self.page_size, self.params)
        self.table_widget.set_data(response_model.data, response_model.totalSize)
        if is_refresh:
            response_message(self, response_model)

    def handle_button_click(self, data):
        getattr(self, data['action'])(data['row'])

    def sub_options(self, data: DialogCallbackModel, is_refresh=True):
        if data.key == 'module':
            init_data = set_product_module(self, data)
            if is_refresh:
                data.input_object.set_select(init_data, True)
            else:
                return init_data

    def add(self, row):
        form_data = copy.deepcopy(self.form_data)
        dialog = DialogWidget('新建页面', form_data)
        dialog.clicked.connect(self.sub_options)
        dialog.exec()  # 显示对话框，直到关闭
        if dialog.data:
            response_model: ResponseModel = Http.post_page_steps(dialog.data)
            response_message(self, response_model)
            self.show_data()

    def edit(self, row):
        form_data = copy.deepcopy(self.form_data)
        for i in form_data:
            if isinstance(row[i.key], dict):
                i.value = row[i.key].get('id', None)
            else:
                i.value = row[i.key]
        for i in form_data:
            if i.subordinate:
                result = next((item for item in form_data if item.key == i.subordinate), None)
                select = get_product_module_label(int(i.value))
                result.select = [ComboBoxDataModel(id=children.value, name=children.label) for children in select]
        dialog = DialogWidget('编辑页面', form_data, )
        dialog.exec()  # 显示对话框，直到关闭
        if dialog.data:
            data = dialog.data
            data['id'] = row['id']
            response_model: ResponseModel = Http.put_page_steps(data)
            response_message(self, response_model)
            self.show_data()

    def add_step(self, row):
        self.parent.set_page('page_steps_detailed', row)

    def copy(self, row):
        print('点击了复制', row)

    def delete(self, row):
        response_model: ResponseModel = Http.delete_page_steps(row.get('id'))
        response_message(self, response_model)
        self.show_data()

    def pagination_clicked(self, data):
        if data['action'] == 'prev':
            self.page = data['page']
        elif data['action'] == 'next':
            self.page = data['page']
        elif data['action'] == 'per_page':
            self.page_size = data['page']
        self.show_data()

    def search(self, data):
        self.params = data
        self.show_data(True)
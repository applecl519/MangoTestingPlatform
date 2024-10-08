# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-09-01 下午8:57
# @Author : 毛鹏
import copy

from mango_ui import *
from mango_ui.init import *

from src.models.gui_model import *
from src.models.network_model import ResponseModel
from src.network import Http
from .case_dict import *


class CasePage(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.page = 1
        self.page_size = 10
        self.params = {}
        self.search_data = [SearchDataModel(**i) for i in search_data]
        self.form_data = [FormDataModel(**i) for i in form_data]
        self.table_column = [TableColumnModel(**i) for i in table_column]
        self.table_menu = [TableMenuItemModel(**i) for i in table_menu]
        self.right_data = [RightDataModel(**i) for i in right_data]

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = SearchWidget(self.search_data)
        self.titleWidget.clicked.connect(self.search)
        self.layout.addWidget(self.titleWidget)

        self.right_but = RightButton(self.right_data)
        self.right_but.clicked.connect(self.callback)
        self.layout.addWidget(self.right_but)

        self.table_widget = TableList(self.table_column, self.table_menu, )
        self.table_widget.pagination.clicked.connect(self.pagination_clicked)
        self.table_widget.clicked.connect(self.callback)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

    def show_data(self, is_refresh=False):
        response_model: ResponseModel = Http.get_case(self.page, self.page_size, self.params)
        self.table_widget.set_data(response_model.data, response_model.totalSize)
        if is_refresh:
            response_message(self, response_model)

    def callback(self, data):
        if data.get('row'):
            getattr(self, data['action'])(data.get('row'))
        else:
            getattr(self, data['action'])()

    def sub_options(self, data: DialogCallbackModel, is_refresh=True):
        if data.key == 'module':
            init_data = set_product_module(self, data)
            if is_refresh:
                data.input_object.set_select(init_data, True)
            else:
                return init_data

    def add(self):
        form_data = copy.deepcopy(self.form_data)
        dialog = DialogWidget('新建页面', form_data)
        dialog.clicked.connect(self.sub_options)
        dialog.exec()  # 显示对话框，直到关闭
        if dialog.data:
            response_model: ResponseModel = Http.post_page(dialog.data)
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
            response_model: ResponseModel = Http.put_page(data)
            response_message(self, response_model)
            self.show_data()

    def add_ele(self, row):
        self.parent.set_page('page_element', row)

    def copy(self, row):
        print('点击了复制', row)

    def delete(self, row):
        response_model: ResponseModel = Http.delete_page(row.get('id'))
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

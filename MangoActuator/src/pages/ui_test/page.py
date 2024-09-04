# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2024-08-28 16:30
# @Author : 毛鹏
import copy

from src import *
from src.components import *
from src.models.gui_model import TitleDataModel, FormDataModel, TableColumnModel, TableMenuItemModel
from src.models.network_model import ResponseModel
from src.network.http_ui import HttpUi


class PagePage(QWidget):
    title_data = [TitleDataModel(**i) for i in [
        {'title': 'ID', 'placeholder': '请输入页面ID', 'key': 'id', 'input': None},
        {'title': '页面名称', 'placeholder': '请输入页面名称', 'key': 'name', 'input': None},
        {'title': '产品', 'placeholder': '请选择项目产品', 'key': 'project_product', 'input': None},
        {'title': '模块', 'placeholder': '请选择产品模块', 'key': 'module', 'input': None}
    ]]
    from_data = [FormDataModel(**i) for i in [
        {'title': '项目/产品', 'placeholder': '请选择项目产品', 'key': 'project_product', 'input': None, 'text': None, 'type': 1},
        {'title': '模块', 'placeholder': '请选择模块', 'key': 'module', 'input': None, 'text': None, 'type': 1},
        {'title': '页面名称', 'placeholder': '请输入页面名称', 'key': 'name', 'input': None, 'text': None,'type': 0},
        {'title': '页面地址', 'placeholder': '请输入页面地址', 'key': 'url', 'input': None, 'text': None, 'type': 0},
    ]]
    table_column = [TableColumnModel(**i) for i in [
        {'key': 'id', 'name': 'ID', 'item': ''},
        {'key': 'update_time', 'name': '更新时间', 'item': ''},
        {'key': 'module', 'name': '模块名称', 'item': 'module,name'},
        {'key': 'project_product', 'name': '项目产品名称', 'item': 'project_product,name'},
        {'key': 'create_Time', 'name': '创建时间', 'item': ''},
        {'key': 'name', 'name': '页面名称', 'item': ''},
        {'key': 'url', 'name': 'URL', 'item': ''},
        {'key': 'ope', 'name': '操作', 'item': ''},
    ]]
    table_menu = [TableMenuItemModel(**i) for i in [
        {'name': '编辑', 'action': 'edit'},
        {'name': '添加元素', 'action': 'add_ele'},
        {'name': '···', 'action': '', 'son': [{'name': '复制', 'action': 'copy'},
                                              {'name': '删除', 'action': 'delete'}]}
    ]]

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.page = 1
        self.page_size = 10
        self.params = {}
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
        response_model: ResponseModel = HttpUi.get_page(self.page, self.page_size, self.params)
        self.table_widget.set_data(response_model.data, response_model.totalSize)
        if is_refresh:
            response_message(self, response_model)

    def handle_button_click(self, data):
        action = data['action']
        row = data['row']
        if action == 'edit':
            self.edit(row)
        elif action == 'add_ele':
            self.add_ele(row)
        elif action == 'copy':
            self.copy(row)
        elif action == 'delete':
            self.delete(row)

    def add(self, row):
        from_data = copy.deepcopy(self.from_data)
        dialog = DialogWidget('新建页面', from_data)
        dialog.exec()  # 显示对话框，直到关闭
        if dialog.data:
            response_model: ResponseModel = HttpUi.post_page(dialog.data)
            response_message(self, response_model)
        self.show_data()

    def edit(self, row):
        from_data = copy.deepcopy(self.from_data)
        for i in from_data:
            print(type(i))
            if isinstance(row[i.key], dict):
                i.text = row[i.key].get('name', None)
            else:
                i.text = row[i.key]
        dialog = DialogWidget('编辑页面', from_data)
        dialog.exec()  # 显示对话框，直到关闭
        if dialog.data:
            data = dialog.data
            data['id'] = row['id']
            response_model: ResponseModel = HttpUi.put_page(data)
            response_message(self, response_model)
        self.show_data()

    def add_ele(self, row):
        self.parent.set_page('page_element', row)

    def copy(self, row):
        print('点击了复制', row)

    def delete(self, row):
        response_model: ResponseModel = HttpUi.delete_page(row.get('id'))
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

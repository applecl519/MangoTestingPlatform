# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: user子路由
# @Time   : 2023-03-01 20:37
# @Author : 毛鹏

from django.urls import path

from .views.project import ProjectCRUD, ProjectViews
from .views.project_file import ProjectFileViews
from .views.project_module import ProjectModuleViews, ProjectModuleCRUD
from .views.role import RoleCRUD, RoleViews
from .views.user import UserCRUD, UserViews
from .views.user_logs import UserLogsCRUD

urlpatterns = [
    #
    path("role", RoleCRUD.as_view()),
    path("role/all", RoleViews.as_view({'get': 'get_all_role'})),
    #
    path("project", ProjectCRUD.as_view()),
    path("project/all", ProjectViews.as_view({'get': 'get_all_items'})),
    #
    path("user/logs", UserLogsCRUD.as_view()),
    #
    path("info", UserCRUD.as_view()),
    path("nickname", UserViews.as_view({'get': 'get_nickname'})),
    path("project/put", UserViews.as_view({'put': 'put_project'})),
    path("environment", UserViews.as_view({'put': 'put_environment'})),
    path("password", UserViews.as_view({'put': 'put_password'})),
    path("project/environment", UserViews.as_view({'get': 'get_user_project_environment'})),
    #
    path("project/module", ProjectModuleCRUD.as_view()),
    path("project/module/get/all", ProjectModuleViews.as_view({'get': 'get_module_name_all'})),
    #
    path("files/test", ProjectFileViews.as_view({'get': 'test'})),
    path("files/all/list", ProjectFileViews.as_view({'get': 'get_project_all_list'})),
    path("files/upload", ProjectFileViews.as_view({'post': 'upload_files'})),
    path("files/download", ProjectFileViews.as_view({'get': 'download_file'})),
    path("files/delete", ProjectFileViews.as_view({'delete': 'delete_file'})),
]

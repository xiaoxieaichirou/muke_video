# condig:utf-8

from django.urls import path, include
from app.dashboard.views.base import Index
from app.dashboard.views.auth import Login, Logout, Admin

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
    path('logout', Logout.as_view(), name='logout'),
    # path('base', Index.as_view())
    path('admin/manger', Admin.as_view(), name='admin_manger'),
]
# condig:utf-8

from django.urls import path, include
from app.dashboard.views.base import Index
from app.dashboard.views.auth import Login

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
]
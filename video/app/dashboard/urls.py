# condig:utf-8

from django.urls import path, include
from app.dashboard.views.base import Base

urlpatterns = [
    path('base', Base.as_view())
]
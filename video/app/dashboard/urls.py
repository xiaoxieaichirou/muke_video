# condig:utf-8

from django.urls import path, include
from app.dashboard.views.base import Index
from app.dashboard.views.auth import Login, Logout, AdminManger, UpdateAdminStatus
from app.dashboard.views.video import ExternalVideo, VideoSub

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manger', AdminManger.as_view(), name='admin_manger'),
    path('admin/manger/update/status', UpdateAdminStatus.as_view(), name='admin_update_status'),
    path('video/external', ExternalVideo.as_view(), name='external_video'),
    path('video/videosub/<int:video_id>', VideoSub.as_view(), name='video_sub'),
]
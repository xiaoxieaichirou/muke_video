# condig:utf-8

from django.urls import path
from app.dashboard.views.base import Index
from app.dashboard.views.auth import Login, Logout, AdminManger, UpdateAdminStatus
from app.dashboard.views.video import ExternalVideo, VideoSubViews, VideoStarView, StarDelete, SubDelete

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manger', AdminManger.as_view(), name='admin_manger'),
    path('admin/manger/update/status', UpdateAdminStatus.as_view(), name='admin_update_status'),
    path('video/external', ExternalVideo.as_view(), name='external_video'),
    path('video/videosub/<int:video_id>', VideoSubViews.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>', StarDelete.as_view(), name='star_delete'),
    path('video/sub/delete/<int:videosub_id>/<int:video_id>', SubDelete.as_view(), name='sub_delete')
]
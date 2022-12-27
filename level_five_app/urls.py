from django.urls import re_path
from level_five_app import views

app_name = 'level_five_app'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='user_login'),
    re_path(r'^logout/$', views.user_logout, name='user_logout')
]
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),

    # Users
    url(r'^users/$', views.user_list, name='users_list'),
    url(r'^users/register/', views.register, name='register'),

    # Login / Logout URLs
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

]

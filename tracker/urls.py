from django.urls import path
from . import views

urlpatterns = [
    path('login/<int:campaign_id>/', views.fake_login, name='fake_login'),
    path('warning/', views.warning, name='warning'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
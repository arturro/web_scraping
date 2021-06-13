from django.urls import path

from . import views

urlpatterns = [
    # simple vies
    path('current_datetime', views.current_datetime, name='current_datetime'),
    path('view_1_0', views.view_1_0, name='view_1_0'),
    path('view_1_0_try', views.view_1_0_try, name='view_1_0_try'),
]

from django.urls import path

from . import views

from django.urls import path


app_name = 'hello'

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),

]

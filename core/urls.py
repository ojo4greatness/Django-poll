from django.urls import path


from . import views

app_name = 'core'

from . import views

urlpatterns = [
    path('', views.home),
]
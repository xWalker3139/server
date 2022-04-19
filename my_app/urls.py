from django.conf.urls import url
from my_app import views

app_name = 'my_app'

urlpatterns = [
    url(r'^sign_up/$', views.sign_up, name="sign_up"),
]
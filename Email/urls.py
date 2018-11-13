from django.conf.urls import url
from django.urls import path
from .views import Email_View


urlpatterns = [
    path('', Email_View.Home_View, name='Home'),
    path('about/', Email_View.About_View, name='About'),
    path('register/', Email_View.email_send, name='Register'),
    path('show/', Email_View.Show_Details, name='Show')
]

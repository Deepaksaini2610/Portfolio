from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginpage,name= 'loginpage'),
    path('logout/',views.logout,name= 'logout'),
    path("re/",views.registeration,name='registeration')
]

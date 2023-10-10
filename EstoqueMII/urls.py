
from django.contrib import admin
from django.urls import path
from estoque_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('pratos/',views.pratos, name='pratos')
]

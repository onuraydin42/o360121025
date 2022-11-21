from django.contrib import admin
from django.urls import path
from projectapp import views as projectappViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projectappViews.home, name='home'),
    path('signin/', projectappViews.signin, name='signin'),
    path('base/', projectappViews.base, name='base'),
]

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name='home'),
    path('about', views.about, name='about'),
    path('calci', views.calci, name='calci'),
    path('contact', views.contact, name='contact'),
    # path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),

]

urlpatterns+= staticfiles_urlpatterns()
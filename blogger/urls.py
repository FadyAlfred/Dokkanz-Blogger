from django.conf.urls import url
from blogger import views

urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
]
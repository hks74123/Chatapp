from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hloo),
    path('sgn',views.shsgn),
    path('lgn',views.shlgn),
    path('login',views.login),
    path('signup',views.signup),
    path('join_grp/',views.join_grp),
] 

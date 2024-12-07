from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('add_train/', views.add_train, name='add_train'),
    path('book_seat/', views.book_seat, name='book_seat'),
]

from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('blog',views.blog,name="blog"),
    path('fullBlog/<int:id>',views.fullBlog,name="fullBlog"),
    path('loginPage',views.loginPage,name="loginpage"),
    path('signupPage',views.signupPage,name="signuppage"),
    path("HandleSignup",views.handlesignup, name="handlesignup"),
    path("HandleLogin",views.handlelogin,name="handlelogin"),
    path("logoutPage",views.handlelogout,name='handlelogout'),
    path("category/<str:id>",views.categoryPage,name="category")
]

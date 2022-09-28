from django.contrib import admin
from django.urls import path
from  home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('contact',views.contact,name="contact"),
    path('feedback',views.feedback,name="feedback"),
    path("login",views.login1,name="login"),
    path("searchProduct",views.search,name="products"),
    path("userLogin/searchProduct",views.search,name="products"),
    path('result',views.result,name="searchedresult"),
    path('register',views.register,name="register"),
    path('signup',views.signup,name="signup"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userLogin/userDashboard',views.userDashboard,name="userDashboard"),
    path('userlogout',views.userlogout,name="userlogout"),

]
admin.site.site_header = "PriceGrabber Admin"
admin.site.site_title = "Purchase here"
admin.site.index_title = "Welcome to PriceGrabber Portal😊"
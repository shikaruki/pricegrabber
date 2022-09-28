from django.contrib import admin
from django.urls import path
from  userLogin import views


urlpatterns = [
   # path('',views.userLogged,name="userLogin"),
   path('userhome',views.userhome,name='home'),
   path('subscribe', views.save, name='save'),
   path('allProduct', views.getAllProduct, name='subscribed'),
   path('logout', views.userlogout, name='logout'),
   path('delete/<int:item_id>',views.delete,name='delete'),
   path('refresh/<int:item_id>',views.refresh,name='refresh'),
]
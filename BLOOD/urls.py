from django.urls import path

from.import views
urlpatterns = [
    path('donoraddblood/', views.donoraddblood, name='donoraddblood'),
    path('bloodupdate/<int:pk>/', views.bloodupdate, name='bloodupdate'),
    path('deleteblood/<int:pk>/', views.deleteblood, name='deleteblood'),
    
    path('status/<int:pk>/', views.orderstatus, name='completed'),
    
    path('myuser/', views.myuser, name='alluser'),
    path('managemyuser/<int:pk>/', views.managemyuser, name='managemyuser'),
    path('userdeact_act/<int:pk>/', views.userdeact_act, name='userdeact_act'),
    path('dashboard/', views.dashboard,  name='dashboard'),
    
    # for users
    path('', views.userindex,  name='userpage'),
    path('searchblood/', views.searchblood,  name='search'),
    # path('donor/', views.userindex,  name='userpage'),
    
]

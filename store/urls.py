from django.urls import path
from . import views
app_name ='store'
urlpatterns = [

    path('createcategory/', views.createcategory, name='createcategory'),
    path('readcategory/', views.readcategory, name='readcategory'),
    path('updatecategory<int:id>/', views.updatecategory, name='updatecategory'),
    path('deletecategory<int:id>/', views.deletecategory, name='deletecategory'),
    path('createproduct/', views.createproduct, name='createproduct'),
    path('readproduct/', views.readproduct, name='readproduct'),
    path('updateproduct<int:id>/', views.updatecategory, name='updateproduct'),
    path('deleteproduct<int:id>/', views.deleteproduct, name='deleteproduct'),
    path('createorder/', views.createorder, name='createorder'),
    path('readorder/', views.readorder, name='readorder'),
    path('updateorder<int:id>/', views.updateorder, name='updateorder'),
    path('deleteorder<int:id>/', views.deleteorder, name='deleteorder'),
]

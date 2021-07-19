from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('p/<str:pk>',views.read,name='read'),
    path('create',views.create,name='create'),
    path('update/<str:id>',views.update,name='update'),
]
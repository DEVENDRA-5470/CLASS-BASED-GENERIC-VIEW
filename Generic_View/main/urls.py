from django.urls import path
from .views import *
urlpatterns=[
    path('',Create_data.as_view(),name="Create_data"),
    path('list/',List_data.as_view(),name="list_data"),
    path('<pk>/delete/',Delete_data.as_view(),name="delete_data"),
    path('<pk>/update/',Update_data.as_view(),name="update_data"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateOption.as_view(), name='create_option'),
    path('<int:pk>/', views.RetrieveOption.as_view(), name='get_option'),
    path('', views.ListOption.as_view(), name='list_option'),
    path('<int:pk>/update', views.UpdateOption.as_view(), name='update_option'),
    path('<int:pk>/destroy', views.DestroyOption.as_view(), name='destroy_option'),
]

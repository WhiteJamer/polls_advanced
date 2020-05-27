from django.urls import path
from . import views

urlpatterns = [
    path('questions/create/', views.CreateQuestion.as_view(), name='create_question'),
    path('questions/<int:pk>/', views.RetrieveQuestion.as_view(), name='get_question'),
    path('questions/', views.ListQuestion.as_view(), name='list_question'),
    path('questions/<int:pk>/update', views.UpdateQuestion.as_view(), name='update_question'),
    path('questions/<int:pk>/destroy', views.DestroyQuestion.as_view(), name='destroy_question'),
]

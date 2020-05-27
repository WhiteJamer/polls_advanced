from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreatePoll.as_view(), name='create_poll'),
    path('<int:pk>/', views.RetrievePoll.as_view(), name='get_poll'),
    path('', views.ListPoll.as_view(), name='list_poll'),
    path('<int:pk>/update', views.UpdatePoll.as_view(), name='update_poll'),
    path('<int:pk>/destroy', views.DestroyPoll.as_view(), name='destroy_poll'),

    path('questions/create/', views.CreateQuestion.as_view(), name='create_question'),
    path('questions/<int:pk>/', views.RetrieveQuestion.as_view(), name='get_question'),
    path('questions/', views.ListQuestion.as_view(), name='list_question'),
    path('questions/<int:pk>/update', views.UpdateQuestion.as_view(), name='update_question'),
    path('questions/<int:pk>/destroy', views.DestroyQuestion.as_view(), name='destroy_question'),
]

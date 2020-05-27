from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateQuestion.as_view(), name='create_question'),
    path('<int:pk>/', views.RetrieveQuestion.as_view(), name='get_question'),
    path('', views.ListQuestion.as_view(), name='list_question'),
    path('<int:pk>/update/', views.UpdateQuestion.as_view(), name='update_question'),
    path('<int:pk>/destroy/', views.DestroyQuestion.as_view(), name='destroy_question'),
    path('<int:pk>/vote/', views.VoteForOption.as_view(), name='vote')
]

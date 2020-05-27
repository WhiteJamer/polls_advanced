from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.RetrieveAnswer.as_view(), name='get_answer'),
    path('', views.ListAnswer.as_view(), name='list_answer'),
    path('user/<int:owner_id>', views.PersonalAnswersList.as_view(), name='personal_list')
]

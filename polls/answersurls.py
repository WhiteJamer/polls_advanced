from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.RetrieveAnswer.as_view(), name='get_answer'),
    path('', views.ListAnswer.as_view(), name='list_answer')
]

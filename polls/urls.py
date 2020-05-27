from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreatePoll.as_view(), name='create'),
    path('<int:id>/', views.RetrievePoll.as_view(), name='get'),
    path('/', views.RetrievePoll.as_view(), name='list'),
    path('/<int:id>/update', views.UpdatePoll.as_view(), name='update'),
    path('/<int:id>/destroy', views.DestroyPoll.as_view(), name='destroy'),
]

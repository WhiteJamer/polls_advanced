from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework import permissions
from .models import Poll
from .serializers import PollCreateSerializer, PollUpdateSerializer, PollSerializer

# CRUD для опросов

class CreatePoll(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Poll.objects.all()
    serializer_class = PollCreateSerializer

class RetrievePoll(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ListPoll(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class UpdatePoll(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Poll.objects.all()
    serializer_class = PollUpdateSerializer

class DestroyPoll(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Poll.objects.all()

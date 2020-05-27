from rest_framework.generics import \
    CreateAPIView,\
    UpdateAPIView,\
    DestroyAPIView,\
    RetrieveAPIView,\
    ListAPIView
from rest_framework import permissions
from .models import Poll, Question
from .serializers import \
    PollCreateSerializer,\
    PollUpdateSerializer, \
    PollSerializer,\
    QuestionCreateSerializer,\
    QuestionUpdateSerializer, \
    QuestionSerializer

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


# CRUD для вопросов

class CreateQuestion(CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class RetrieveQuestion(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ListQuestion(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UpdateQuestion(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionUpdateSerializer

class DestroyQuestion(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()

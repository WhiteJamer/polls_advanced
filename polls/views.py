from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import \
    CreateAPIView,\
    UpdateAPIView,\
    DestroyAPIView,\
    RetrieveAPIView,\
    ListAPIView
from rest_framework import permissions
from .models import Poll, Question, Option, Answer
from .serializers import \
    PollCreateSerializer,\
    PollUpdateSerializer, \
    PollSerializer,\
    QuestionCreateSerializer,\
    QuestionUpdateSerializer, \
    QuestionSerializer,\
    OptionCreateSerializer,\
    OptionUpdateSerializer,\
    OptionSerializer,\
    AnswerSerializer

# CRUD для опросов

class CreatePoll(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Poll.objects.all()
    serializer_class = PollCreateSerializer

class RetrievePoll(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ListPoll(APIView):
    def get(self, request, format=None): # Пользователи имеют доступ только к активным опросам
        if(request.user.is_staff):
            polls = Poll.objects.all()
            serializer = PollSerializer(polls, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            polls = Poll.objects.filter(is_active=True)
            serializer = PollSerializer(polls, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


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

# CRUD для вариантов

class CreateOption(CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Option.objects.all()
    serializer_class = OptionSerializer



class RetrieveOption(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class ListOption(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class UpdateOption(UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Option.objects.all()
    serializer_class = OptionUpdateSerializer

class DestroyOption(DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Option.objects.all()

# answers

class RetrieveAnswer(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ListAnswer(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class VoteForOption(APIView):
    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        if question.type == 'TEXT':
            new_answer = Answer(question=question, text=request.POST.text, owner_id=request.POST.owner_id)
            new_answer.full_clean() # Валидируем
            new_answer.save()
            return new_answer
        if question.type == 'ONE' or question.type == 'MANY':
            new_answer = Answer(question=question, owner_id=request.POST['owner_id'])
            new_answer.save()
            try:
                new_answer.options.add(request.POST['options'])
                new_answer.full_clean()  # Валидируем
                new_answer.bulk_create()
                return new_answer
            except:
                    new_answer.delete()

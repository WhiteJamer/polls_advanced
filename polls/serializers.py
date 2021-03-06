from rest_framework import serializers
from .models import Poll, Question, Option, Answer

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class OptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class OptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Poll
        fields = '__all__'

class PollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__' # доступны все поля

class PollUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        exclude = ('start_date',) # доступны для изменения все поля кроме start_date

class AnswerSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = '__all__'


